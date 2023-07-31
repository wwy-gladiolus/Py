#!/usr/bin/env python3

import asyncio
import sys

#引用两个子任务的全局变量。
task1 = None
task2 = None


#该协程函数用于输出平方表的自变量。
async def n(bound):
    for i in range(bound):
        print('n:', i)
        await asyncio.sleep(1)


#该协程函数用于输出平方表的因变量。
async def n_square(bound):
    for i in range(bound):
        print('n square:', i * i)
        await asyncio.sleep(1)


#该协程函数输出平方表，并将前两个协程函数作为子任务。
async def print_square_table(bound):
    #global task1, task2
        global task1, task2
    #try:
        task1 = asyncio.create_task(n(bound))
        task2 = asyncio.create_task(n_square(bound))
        await task1
        await task2
        #await asyncio.shield(task1)
        #await asyncio.shield(task2)
    #except asyncio.CancelledError:
        #task1.cancel()
        #task2.cancel()
        #raise


#该协程函数在2.9秒后取消输出平方表的任务。
async def cancel_print(task):
    await asyncio.sleep(2.9)
    task.cancel()


#主协程函数将第一个命令行参数解读为输出到平方表的第几项。
async def main():
    global task1, task2
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        bound = int(sys.argv[1])
        #创建输出平方表的任务。
        task = asyncio.create_task(print_square_table(bound))
        #创建取消输出平方表的任务。
        cancel_task = asyncio.create_task(cancel_print(task))
        await task
        await cancel_task
    except asyncio.CancelledError:
        pass
    #在接收到asyncio.CancelledError后显示输出平方表的任务和它的两个子任务的当前
    # 状态。
    print("task.cancelled():", task.cancelled())
    print("task.done():", task.done())
    print("task1.cancelled():", task1.cancelled())
    print("task1.done():", task1.done())
    print("task2.cancelled():", task2.cancelled())
    print("task2.done():", task2.done())
    #让主协程持续运行到task1和task2的状态都变成“已完成”或“已取消”。
    while not task1.done() or not task2.done():
        await asyncio.sleep(1)
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
