#!/usr/bin/env python3

import asyncio
import random
import sys


#该协程函数创建的协程是生产者。  它们不停地随机生成一个0~100内的整数，并将其插入
# 异步队列。  当队列变满时，它会挂起自身直到队列被清空。
async def producer(queue):
    while True:
        try:
            n = random.randrange(100)
            queue.put_nowait(n)
        except asyncio.QueueFull:
            await queue.join()


#该协程函数创建的协程是消费者。  它们每隔0.5秒从异步队列取出整数，并检查其是否是7的
# 倍数，如果是则抛出记录有尝试次数消息的Exception异常。
async def comsumer(queue):
    trial = 0
    while True:
        trial = trial + 1
        n = await queue.get()
        #取出数据项后一定要通知异步队列。
        queue.task_done()
        sys.stdout.write(str(n) + " ")
        sys.stdout.flush()
        if n % 7 == 0:
            raise Exception(f"Found after {trial} trials!")
        await asyncio.sleep(0.5)


async def main():
    #创建生产者和消费者共享的异步队列，其容量是5。
    q = asyncio.LifoQueue(5)
    p_task = asyncio.create_task(producer(q))
    c_task = asyncio.create_task(comsumer(q))
    try:
        await asyncio.gather(p_task, c_task)
    except Exception as e:
        p_task.cancel()
        c_task.cancel()
        print("\n" + e.args[0])
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
