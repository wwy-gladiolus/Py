#!/usr/bin/env python3

import asyncio
import random
import sys


async def producer(stack, sem1, sem2, name):
    while True:
        t = random.random()
        await asyncio.sleep(t)
        n = random.randrange(100)
        #申请获得限制生产者的信号量。
        await sem1.acquire()
        stack.append((name, n))
        print(f"append ({name}, {n})")
        print(f"  stack size: {len(stack)}")
        #释放限制消费者的信号量。
        sem2.release()


async def comsumer(stack, sem1, sem2, name):
    while True:
        t = random.random()
        await asyncio.sleep(t)
        #申请获得限制消费者的信号量。
        await sem2.acquire()
        data = stack.pop()
        print(f"{name}: pop ({data[0]}, {data[1]})")
        print(f"  stack size: {len(stack)}")
        #释放限制生产者的信号量。
        sem1.release()


async def main():
    q = list()
    #创建限制生产者的信号量，其计数器的初始值是4。
    s1 = asyncio.Semaphore(4)
    #创建限制消费者的信号量，其计数器的初始值是0。
    s2 = asyncio.Semaphore(0)
    #创建生产者任务。
    p1 = asyncio.create_task(producer(q, s1, s2, "p1"))
    p2 = asyncio.create_task(producer(q, s1, s2, "p2"))
    #创建消费者任务。
    c1 = asyncio.create_task(comsumer(q, s1, s2, "c1"))
    task = asyncio.gather(p1, p2, c1)
    try:
        await asyncio.wait_for(task, 5)
    except asyncio.TimeoutError:
        task.cancel()
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
