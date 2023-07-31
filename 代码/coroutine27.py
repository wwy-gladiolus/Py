#!/usr/bin/env python3

import asyncio
import random
import sys

lock1 = asyncio.Lock()
lock2 = asyncio.Lock()


#该协程函数创建的协程显示“foo”之前必须同时获得lock1和lock2。
async def foo():
    #先申请获得lock1。
    await lock1.acquire()
    #挂起一瞬间。
    await asyncio.sleep(0)
    #再申请获得lock2。
    await lock2.acquire()
    print("foo")
    lock2.release()
    lock1.release()


#该协程函数创建的协程显示“bar”之前必须同时获得lock2和lock1。
async def bar():
    #先申请获得lock2。
    await lock2.acquire()
    #挂起一瞬间。
    await asyncio.sleep(0)
    #再申请获得lock1。
    await lock1.acquire()
    print("bar")
    lock1.release()
    lock2.release()


async def main():
    print("begin")
    await asyncio.gather(foo(), bar())
    print("end")
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
