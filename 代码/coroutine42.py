#!/usr/bin/env python3
#改写自coroutine15.py

import asyncio
import random
import time
import sys


async def hiker(name, barrier):
    try:
        t = random.uniform(0.5, 7.0)
        await asyncio.sleep(t)
        print(f"{name}: I meet the barrier at {time.strftime('%X')}.")
        print(f"{name}: n_waiting == {barrier.n_waiting}, broken == {barrier.broken}")
        #以异步上下文管理器的方式使用屏障。
        async with barrier:
            print(f"{name}: I cross the barrier at {time.strftime('%X')}.")
            print(f"{name}: n_waiting == {barrier.n_waiting}, broken == {barrier.broken}")
    except asyncio.BrokenBarrierError:
        print(f"{name}: The barrier collapses before {time.strftime('%X')}. Hooray!")
        print(f"{name}: n_waiting == {barrier.n_waiting}, broken == {barrier.broken}")


async def hammer(barrier):
    await asyncio.sleep(5)
    await barrier.abort()
    #await barrier.reset()


async def main():
    barrier = asyncio.Barrier(3)
    hiker1 = asyncio.create_task(hiker("hiker1", barrier))
    hiker2 = asyncio.create_task(hiker("hiker2", barrier))
    hiker3 = asyncio.create_task(hiker("hiker3", barrier))
    hammer0 = asyncio.create_task(hammer(barrier))
    print(f"Start at {time.strftime('%X')}")
    await asyncio.gather(hiker1, hiker2, hiker3, hammer0)
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
