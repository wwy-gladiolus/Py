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
    task1 = asyncio.create_task(n(bound))
    task2 = asyncio.create_task(n_square(bound))
    #将task1和task2聚集成一个任务。
    await asyncio.gather(task1, task2)


async def cancel_print(task):
    await asyncio.sleep(2.9)
    task.cancel()


async def main():
    global task1, task2
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        bound = int(sys.argv[1])
        task = asyncio.create_task(print_square_table(bound))
        cancel_task = asyncio.create_task(cancel_print(task))
        await task
        await cancel_task
    except asyncio.CancelledError:
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
