#!/usr/bin/env python3

import asyncio
import random
import time
import sys


#该协程函数创建的协程代表徒步旅行者。
async def hiker(name, barrier):
    try:
        #该徒步旅行者随机花费0.5~7.0秒走到屏障前。
        t = random.uniform(0.5, 7.0)
        await asyncio.sleep(t)
        #显示该徒步旅行者走到屏障前的时间，以及屏障的状态。
        print(f"{name}: I meet the barrier at {time.strftime('%X')}.")
        print(f"{name}: n_waiting == {barrier.n_waiting}, broken == {barrier.broken}")
        #等待所有徒步旅行者到齐。  如果屏障已经损坏，则立刻抛出
        # asyncio.BrokenBarrierError异常。
        await barrier.wait()
        #显示该徒步旅行者翻越屏障的时间，以及屏障的状态。
        print(f"{name}: I cross the barrier at {time.strftime('%X')}.")
        print(f"{name}: n_waiting == {barrier.n_waiting}, broken == {barrier.broken}")
    except asyncio.BrokenBarrierError:
        #显示该旅行者意识到屏障已经损坏的时间，以及屏障的状态。
        print(f"{name}: The barrier collapses before {time.strftime('%X')}. Hooray!")
        print(f"{name}: n_waiting == {barrier.n_waiting}, broken == {barrier.broken}")


#该协程函数创建的协程代表锤子。  它会在5秒钟后破坏屏障。
async def hammer(barrier):
    await asyncio.sleep(5)
    await barrier.abort()
    #await barrier.reset()


async def main():
    #创建一个屏障。
    barrier = asyncio.Barrier(3)
    #创建四个任务并将它们聚集成一个任务。  只有hiker1、hiker2和hiker3需要翻越屏障。
    #  hammer0将破坏屏障。
    hiker1 = asyncio.create_task(hiker("hiker1", barrier))
    hiker2 = asyncio.create_task(hiker("hiker2", barrier))
    hiker3 = asyncio.create_task(hiker("hiker3", barrier))
    hammer0 = asyncio.create_task(hammer(barrier))
    #显示这次徒步旅行开始的时间，然后开始旅行。
    print(f"Start at {time.strftime('%X')}")
    await asyncio.gather(hiker1, hiker2, hiker3, hammer0)
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
