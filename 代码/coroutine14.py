#!/usr/bin/env python3

import asyncio
import sys

#用一个全局变量来引用动态增添的任务。
task3 = None


#该协程函数的参数tg需被传入一个TaskGroup对象。
async def foo(tg):
    global task3
    for i in range(5):
        #取得当前所有未完成的任务。
        unfinished_tasks = asyncio.all_tasks()
        #显示所有未完成任务的名字。
        s = "unfinished tasks: "
        for t in unfinished_tasks:
            s += t.get_name() + " "
        print(s)
        #1秒后动态给任务组增添任务baz。
        if i == 1:
            task3 = tg.create_task(baz(), name="baz")
        print("foo:", i)
        await asyncio.sleep(1)
    return i


async def bar():
    for i in range(3):
        print("bar:", i)
        #2秒后取消任务bar。
        if i == 2:
            asyncio.current_task().cancel()
        await asyncio.sleep(1)
    return i


async def baz():
    for i in range(4):
        print("baz:", i)
        #if i == 2:
            #raise RuntimeError()
            #raise KeyboardInterrupt()
        await asyncio.sleep(1)
    return i


async def main():
    try:
        #创建一个任务组，使其包含任务foo和bar。
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(foo(tg), name="foo")
            task2 = tg.create_task(bar(), name="bar")
    except (KeyboardInterrupt, BaseExceptionGroup, ExceptionGroup) as e:
        #截获TaskGroup对象抛出的异常并显示。
        print(repr(e))
    finally:
        #显示任务组完成时各任务的状态。
        for i in range(1, 4):
            codes = f"""
print(f'\\n{{task{i}.get_name()}}.cancelled() == {{task{i}.cancelled()}}')
print(f'{{task{i}.get_name()}}.done() == {{task{i}.done()}}')
try:
    print(f'{{task{i}.get_name()}}.result() == {{task{i}.result()}}')
except BaseException as e:
    print(f'{{task{i}.get_name()}}.result() == {{repr(e)}}')
if not task{i}.cancelled():
    task{i}.cancel()"""
            exec(codes)
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
