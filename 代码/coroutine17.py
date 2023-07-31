#!/usr/bin/env python3

import asyncio
import sys


#该协程函数创建的协程以0.1秒为间隔连续显示三个“*”。
async def stars(lock):
    try:
        while True:
            #申请获得锁，进入临界区。
            await lock.acquire()
            #显示锁的当前状态。
            print(f"\nstars: locked == {lock.locked()}")
            #显示“*”。
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("*")
                sys.stdout.flush()
            #释放锁，离开临界区。
            lock.release()
    except asyncio.CancelledError:
        lock.release()
        raise


#该协程函数创建的协程以0.1秒为间隔连续显示三个“$”。
async def dollars(lock):
    try:
        while True:
            #申请获得锁，进入临界区。
            await lock.acquire()
            #显示锁的当前状态。
            print(f"\ndollars: locked == {lock.locked()}")
            #显示“$”。
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("$")
                sys.stdout.flush()
            #释放锁，离开临界区。
            lock.release()
    except asyncio.CancelledError:
        lock.release()
        raise


async def main():
    #创建一个关联到标准输出的锁。
    lock = asyncio.Lock()
    #创建两个任务并将它们聚集成一个任务。
    task_stars = asyncio.create_task(stars(lock))
    task_dollars = asyncio.create_task(dollars(lock))
    task = asyncio.gather(task_stars, task_dollars)
    try:
        #显示锁的当前状态。
        print(f"\nlocked == {lock.locked()}")
        #运行任务1.1秒。
        await asyncio.wait_for(task, 1.1)
    except asyncio.TimeoutError:
        #显示锁的当前状态。
        print(f"\n\nlocked == {lock.locked()}")
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
