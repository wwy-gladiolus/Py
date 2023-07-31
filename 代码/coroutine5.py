#!/usr/bin/env python3

import asyncio
import time
import sys

#引用主协程的全局变量。
coro_main = None


#该协程函数创建的协程会显示自身的执行过程。  它会睡眠1秒，在睡眠前后分别输出提示信息。
#  它还会显示主协程的cr_await属性的当前值。
async def self_explain(tag):
    print(f"{tag}: sleep at {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"{tag}: awake at {time.strftime('%X')}")
    print(f"    {tag}: " + str(coro_main.cr_await))


#主协程函数混合使用了协程和任务。
async def main():
    await self_explain("coro1")
    task1 = asyncio.create_task(self_explain("task1"))
    task2 = asyncio.create_task(self_explain("task2"))
    await task2
    await self_explain("coro2")
    task3 = asyncio.create_task(self_explain("task3"))
    await task1
    await self_explain("coro3")
    await task3
    sys.exit(0)


if __name__ == '__main__':
    coro_main = main()
    asyncio.run(coro_main)
