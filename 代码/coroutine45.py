#!/usr/bin/env python3
#改写自coroutine19.py

import asyncio
import random
import time
import sys

even_number = None


async def stars(cond):
    while True:
        #将监视器当成异步上下文管理器来使用。
        async with cond:
            await cond.wait_for(lambda: even_number)
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("*")
                sys.stdout.flush()
            print("")


async def dollars(cond):
     while True:
        #将监视器当成异步上下文管理器来使用。
        async with cond:
            await cond.wait_for(lambda: not even_number)
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("$")
                sys.stdout.flush()
            print("")


async def num_gen(cond):
    global even_number
    while True:
        #将监视器当成异步上下文管理器来使用。
        async with cond:
            n = random.randrange(100)
            if n % 2 == 0:
                even_number = True
            else:
                even_number = False
            cond.notify_all()
        await asyncio.sleep(0)


async def main():
    cond = asyncio.Condition()
    task_num_gen = asyncio.create_task(num_gen(cond))
    task_stars = asyncio.create_task(stars(cond))
    task_dollars = asyncio.create_task(dollars(cond))
    task = asyncio.gather(task_num_gen, task_stars, task_dollars)
    try:
        await asyncio.wait_for(task, 2)
    except asyncio.TimeoutError:
        pass
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
