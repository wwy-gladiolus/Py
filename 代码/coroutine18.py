#!/usr/bin/env python3

import asyncio
import random
import sys


#该协程函数创建的协程以0.1秒为间隔连续显示三个“*”。  但它等待的是监视器而非锁。
async def stars(cond):
    try:
        #申请获得底层锁，进入临界区。
        await cond.acquire()
        while True:
            #等待监视器，并释放底层锁，离开临界区。
            await cond.wait()
            #在这里会重新申请获得底层锁，进入临界区。
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("*")
                sys.stdout.flush()
            print("")
    except asyncio.CancelledError:
        #在任务被取消时释放底层锁。
        cond.release()
        raise


#该协程函数创建的协程以0.1秒为间隔连续显示三个“$”。  但它等待的是监视器而非锁。
async def dollars(cond):
    try:
        #申请获得底层锁，进入临界区。
        await cond.acquire()
        while True:
            #等待监视器，并释放底层锁，离开临界区。
            await cond.wait()
            #在这里会重新申请获得底层锁，进入临界区。
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("$")
                sys.stdout.flush()
            print("")
    except asyncio.CancelledError:
        #在任务被取消时释放底层锁。
        cond.release()
        raise


#该协程函数创建的协程直接通过lock获得和释放底层锁，只要获得了底层锁就会随机生成一个
# 0~100内的整数。  如果该整数是偶数，则通知等待cond1的任务执行。  如果该整数是奇数，
# 则通知等待cond2的任务执行。
async def num_gen(lock, cond1, cond2):
    while True:
        #申请获得底层锁，进入临界区。
        await lock.acquire()
        n = random.randrange(100)
        if n % 2 == 0:
            #通知等待cond1的任务。
            cond1.notify()
        else:
            #通知等待cond2的任务。
            cond2.notify()
        #释放底层锁，离开临界区。
        lock.release()
        await asyncio.sleep(0)


async def main():
    #创建一个关联到标准输出的锁。
    lock = asyncio.Lock()
    #创建一个以lock为底层锁，代表生成了偶数的监视器。
    cond1 = asyncio.Condition(lock)
    #创建一个以lock为底层锁，代表生成了奇数的监视器。
    cond2 = asyncio.Condition(lock)
    #创建三个任务并将它们聚集成一个任务。
    task_num_gen = asyncio.create_task(num_gen(lock, cond1, cond2))
    task_stars = asyncio.create_task(stars(cond1))
    task_dollars = asyncio.create_task(dollars(cond2))
    task = asyncio.gather(task_num_gen, task_stars, task_dollars)
    try:
        #运行任务2秒。
        await asyncio.wait_for(task, 2)
    except asyncio.TimeoutError:
        pass
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
