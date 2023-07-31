#!/usr/bin/env python3
#改写自coroutine17.py

import asyncio
import sys


async def stars(lock):
    while True:
        #将锁当成异步上下文管理器来使用。
        async with lock:
            print(f"\nstars: locked == {lock.locked()}")
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("*")
                sys.stdout.flush()


async def dollars(lock):
    while True:
        #将锁当成异步上下文管理器来使用。
        async with lock:
            print(f"\ndollars: locked == {lock.locked()}")
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("$")
                sys.stdout.flush()


async def main():
    lock = asyncio.Lock()
    task_stars = asyncio.create_task(stars(lock))
    task_dollars = asyncio.create_task(dollars(lock))
    task = asyncio.gather(task_stars, task_dollars)
    try:
        print(f"\nlocked == {lock.locked()}")
        await asyncio.wait_for(task, 1.1)
    except asyncio.TimeoutError:
        print(f"\n\nlocked == {lock.locked()}")
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
