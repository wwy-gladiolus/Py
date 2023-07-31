#!/usr/bin/env python3

import asyncio
import sys


async def foo():
    for i in range(5):
        print("foo:", i)
        await asyncio.sleep(1)
    return i


async def bar():
    for i in range(5):
        print("bar:", i)
        if i > 1:
            asyncio.current_task().cancel()
        await asyncio.sleep(1)


async def baz():
    for i in range(5):
        print("baz:", i)
        if i > 2:
            raise RuntimeError()
        await asyncio.sleep(1)


async def main():
    #创建任务时设置了任务名字。
    task1 = asyncio.create_task(foo(), name="foo")
    task2 = asyncio.create_task(bar(), name="bar")
    task3 = asyncio.create_task(baz(), name="baz")
    #将三个任务合并成一个协程来运行。
    coro = asyncio.wait([task1, task2, task3])
    #coro = asyncio.wait([task1, task2, task3], return_when=asyncio.FIRST_COMPLETED)
    #coro = asyncio.wait([task1, task2, task3], return_when=asyncio.FIRST_EXCEPTION)
    #coro = asyncio.wait([task1, task2, task3], timeout=1.5)
    done, pending = await coro
    #查看已完成或已取消任务。
    print(f"\n{len(done)} tasks done:")
    for task in done:
        print(f"{task.get_name()}.cancelled() == {task.cancelled()}")
        print(f"{task.get_name()}.done() == {task.done()}")
        try:
            print(f"{task.get_name()}.result() == {task.result()}\n")
        except BaseException as e:
            print(f"{task.get_name()}.result() == {repr(e)}\n")
    #查看未完成任务。
    print(f"\n{len(pending)} tasks pending:")
    for task in pending:
        print(f"{task.get_name()}.cancelled() == {task.cancelled()}")
        print(f"{task.get_name()}.done() == {task.done()}")
        try:
            print(f"{task.get_name()}.result() == {task.result()}\n")
        except BaseException as e:
            print(f"{task.get_name()}.result() == {repr(e)}\n")
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
