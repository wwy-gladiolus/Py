#!/usr/bin/env python3

import asyncio
import sys

task1 = None
task2 = None


async def n(bound):
    for i in range(bound):
        print('n:', i)
        await asyncio.sleep(1)


async def n_square(bound):
    for i in range(bound):
        print('n square:', i * i)
        await asyncio.sleep(1)


async def print_square_table(bound):
    global task1, task2
    try:
        task1 = asyncio.create_task(n(bound))
        task2 = asyncio.create_task(n_square(bound))
        await task1
        await task2
    except asyncio.CancelledError:
        task1.cancel()
        task2.cancel()
        raise


async def main():
    global task1, task2
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        bound = int(sys.argv[1])
        task = asyncio.create_task(print_square_table(bound))
        #使得等待task完成的时间不超过2.9秒。
        waited_task = asyncio.wait_for(task, 2.9)
        await waited_task
    #这里需要处理的是asyncio.TimeoutError异常而非asyncio.CancelledError异常。
    except asyncio.TimeoutError:
        pass
    print("task.cancelled():", task.cancelled())
    print("task.done():", task.done())
    print("task1.cancelled():", task1.cancelled())
    print("task1.done():", task1.done())
    print("task2.cancelled():", task2.cancelled())
    print("task2.done():", task2.done())
    while not task1.done() or not task2.done():
        await asyncio.sleep(1)
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
