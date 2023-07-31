#!/usr/bin/env python3

import asyncio
import sys


#foo()创建的协程会以1秒为间隔打印0~4。
async def foo():
    for i in range(5):
        print("foo:", i)
        await asyncio.sleep(1)
    return i


#bar()创建的协程会以1秒为间隔打印0~2，然后被取消。
async def bar():
    for i in range(5):
        print("bar:", i)
        if i > 1:
            asyncio.current_task().cancel()
        await asyncio.sleep(1)


#baz()创建的协程会以1秒为间隔打印0~3，然后抛出RuntimeError异常。
async def baz():
    for i in range(5):
        print("baz:", i)
        if i > 2:
            raise RuntimeError()
        await asyncio.sleep(1)


async def main():
    result = None
    try:
        #聚集foo()、bar()和baz()。
        task = asyncio.gather(foo(), bar(), baz())
        #task = asyncio.gather(foo(), bar(), baz(), return_exceptions=True)
        await task
    except RuntimeError as e:
        print("RuntimeError")
    except asyncio.CancelledError as e:
        print("CancelledError")
    #等待3秒钟，以确保所有被聚集的任务执行完。
    await asyncio.sleep(3)
    #检查task的状态。
    print("task.cancelled() ==", task.cancelled())
    print("task.done() ==", task.done())
    try:
        print("task.result() ==", task.result())
    except BaseException as e:
        print("task.result() ==", repr(e))
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
