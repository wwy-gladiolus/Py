#!/usr/bin/env python3

import asyncio
import sys


async def foo():
    for i in range(5):
        print("foo:", i)
        await asyncio.sleep(1)
    return i


async def bar():
    for i in range(3):
        print("bar:", i)
        #if i > 0:
        #    asyncio.current_task().cancel()
        await asyncio.sleep(1)
    return i


async def baz():
    for i in range(4):
        print("baz:", i)
        #if i > 2:
        #    raise RuntimeError()
        await asyncio.sleep(1)
    return i


async def main():
    task1 = asyncio.create_task(foo(), name="foo")
    task2 = asyncio.create_task(bar(), name="bar")
    task3 = asyncio.create_task(baz(), name="baz")
    try:
        #并行运行三个任务。
        for coro in asyncio.as_completed([task1, task2, task3]):
        #for coro in asyncio.as_completed([task1, task2, task3], timeout=1.5):
            #取得任务执行结果并显示。
            result = await coro
            print(result)
    except (asyncio.CancelledError, asyncio.TimeoutError, RuntimeError) as e:
        #如果抛出异常，则显示。
        print(repr(e))
    finally:
        #取得迭代停止时三个任务的信息，然后取消未完成的任务。
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
