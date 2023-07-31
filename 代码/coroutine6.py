#!/usr/bin/env python3

import asyncio
import time
import sys


#该任务将通过msg传入的消息在延迟sec秒后写入标准输出。
async def delayed_sender(sec, msg, tag):
    try:
        await asyncio.sleep(sec)
        print(f"{tag}: {msg} at {time.strftime('%X')}")
    except asyncio.CancelledError as e:
        print(f"{tag}: Sending message is cancelled at {time.strftime('%X')}.")
        print(e.args)
        #raise


async def main():
    task1 = asyncio.create_task(delayed_sender(1, "Message1", "sender1"))
    task2 = asyncio.create_task(delayed_sender(2, "Message2", "sender2"))
    task3 = asyncio.create_task(delayed_sender(3, "Message3", "sender3"))
    #开始并行执行任务队列中的三个任务。
    await asyncio.sleep(0.5)
    #取消task2。
    task2.cancel("Cancelling task2 ...")
    await task1
    await task2
    await task3
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
