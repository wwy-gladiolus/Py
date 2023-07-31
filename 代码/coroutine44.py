#!/usr/bin/env python3
#改写自coroutine18.py

import asyncio
import random
import sys


async def stars(cond):
    #将监视器当成异步上下文管理器来使用。
    async with cond:
        while True:
            await cond.wait()
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("*")
                sys.stdout.flush()
            print("")


async def dollars(cond):
    #将监视器当成异步上下文管理器来使用。
    async with cond:
        while True:
            await cond.wait()
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("$")
                sys.stdout.flush()
            print("")


async def num_gen(lock, cond1, cond2):
    while True:
        #将锁当成异步上下文管理器来使用。
        async with lock:
            n = random.randrange(100)
            if n % 2 == 0:
                cond1.notify()
            else:
                cond2.notify()
            await asyncio.sleep(0)


async def main():
    lock = asyncio.Lock()
    cond1 = asyncio.Condition(lock)
    cond2 = asyncio.Condition(lock)
    task_num_gen = asyncio.create_task(num_gen(lock, cond1, cond2))
    task_stars = asyncio.create_task(stars(cond1))
    task_dollars = asyncio.create_task(dollars(cond2))
    task = asyncio.gather(task_num_gen, task_stars, task_dollars)
    try:
        await asyncio.wait_for(task, 2)
    except asyncio.TimeoutError:
        pass
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
