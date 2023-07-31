#!/usr/bin/env python3

import asyncio
import random
import sys


#该协程函数创建的协程是生产者。  它们随机睡眠0~1秒的时间，然后随机生成一个0~100内的
# 整数n，最后将元组(name, n)插入无长度限制的LIFO队列stack。
async def producer(stack, sem, name):
    while True:
        t = random.random()
        await asyncio.sleep(t)
        n = random.randrange(100)
        #生成数据项。
        stack.append((name, n))
        print(f"append ({name}, {n})")
        print(f"  stack size: {len(stack)}")
        #释放信号量，唤醒被挂起的消费者，否则使计数器加1。
        sem.release()


#该协程函数创建的协程是消费者。  它们随机睡眠0~1秒的时间，然后从LIFO队列stack中取出
# 第一个元素是name的元组。
async def comsumer(stack, sem, name):
    while True:
        t = random.random()
        await asyncio.sleep(t)
        #申请获得信号量，当计数器值为0时被挂起，否则使计数器减1。
        await sem.acquire()
        #取出数据项。
        data = stack.pop()
        print(f"{name}: pop ({data[0]}, {data[1]})")
        print(f"  stack size: {len(stack)}")


async def main():
    #创建生产者和消费者共享的LIFO队列。
    q = list()
    #创建信号量。
    s = asyncio.Semaphore(0)
    #创建生产者任务。
    p1 = asyncio.create_task(producer(q, s, "p1"))
    p2 = asyncio.create_task(producer(q, s, "p2"))
    #创建消费者任务。
    c1 = asyncio.create_task(comsumer(q, s, "c1"))
    c2 = asyncio.create_task(comsumer(q, s, "c2"))
    c3 = asyncio.create_task(comsumer(q, s, "c3"))
    #将多个任务聚集成一个。
    task = asyncio.gather(p1, p2, c1, c2, c3)
    #task = asyncio.gather(p1, p2, c1)
    try:
        #启动任务，运行5秒。
        await asyncio.wait_for(task, 5)
    except asyncio.TimeoutError:
        #取消任务。
        task.cancel()
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
