#!/usr/bin/env python3

import asyncio
import random
import sys


async def producer(stack, sem, name):
    while True:
        t = random.random()
        await asyncio.sleep(t)
        try:
            n = random.randrange(100)
            stack.append((name, n))
            #该操作可能导致抛出ValueError异常。
            sem.release()
            print(f"append ({name}, {n})")
        except ValueError:
            #如果抛出了ValueError异常，则丢弃生成的数据项。
            stack.pop()
            print(f"fail to append ({name}, {n})")
        finally:
            print(f"  stack size: {len(stack)}")


async def comsumer(stack, sem, name):
    while True:
        t = random.random()
        await asyncio.sleep(t)
        await sem.acquire()
        data = stack.pop()
        print(f"{name}: pop ({data[0]}, {data[1]})")
        print(f"  stack size: {len(stack)}")


async def main():
    #被生产者和消费者共享的FIFO队列初始就被填满。
    q = [("init", -1), ("init", -2), ("init", -3), ("init", -4)]
    #创建限制消费者的受限信号量，其初始值和最大值都是4。
    s = asyncio.BoundedSemaphore(4)
    #创建生产者任务。
    p1 = asyncio.create_task(producer(q, s, "p1"))
    p2 = asyncio.create_task(producer(q, s, "p2"))
    #创建消费者任务。
    c1 = asyncio.create_task(comsumer(q, s, "c1"))
    task = asyncio.gather(p1, p2, c1)
    try:
        await asyncio.wait_for(task, 5)
    except asyncio.TimeoutError:
        task.cancel()
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
