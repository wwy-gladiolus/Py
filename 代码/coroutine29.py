#!/usr/bin/env python3

import asyncio
import random
import sys


#该协程函数创建的协程是生产者。  它们每隔0.5秒随机生成一个0~100内的整数，并将其插入
# 异步队列。
async def producer(queue):
    while True:
        n = random.randrange(100)
        await queue.put(n)
        await asyncio.sleep(0.5)


#该协程函数创建的协程是消费者。  它们不停地从异步队列取出整数，并检查其是否是7的倍数，
# 如果是则抛出记录有尝试次数消息的Exception异常。
async def consumer(queue):
    trial = 0
    while True:
        trial = trial + 1
        n = await queue.get()
        sys.stdout.write(str(n) + " ")
        sys.stdout.flush()
        if n % 7 == 0:
            raise Exception(f"Found after {trial} trials!")


async def main():
    #创建生产者和消费者共享的异步队列。
    q = asyncio.Queue()
    #创建生产者任务。
    p_task = asyncio.create_task(producer(q))
    #创建消费者任务。
    c_task = asyncio.create_task(consumer(q))
    try:
        #启动任务。
        await asyncio.gather(p_task, c_task)
    except Exception as e:
        #取消任务。
        p_task.cancel()
        c_task.cancel()
        #显示异常携带的消息。
        print("\n" + e.args[0])
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
