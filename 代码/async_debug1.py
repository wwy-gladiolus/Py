#!/usr/bin/env python3

import asyncio
import sys


async def coro():
    pass


async def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        #根据第一个命令行参数设置协程溯源的深度。
        d = int(sys.argv[1])
        sys.set_coroutine_origin_tracking_depth(d)
        #创建一个任务并执行。
        task = asyncio.create_task(coro())
        await task
        #取得该任务包装的协程。
        cr = task.get_coro()
        #取得并显示当前协程溯源的深度。
        otd = sys.get_coroutine_origin_tracking_depth()
        print(f"origin tracking depth: {otd}")
        #显示协程溯源信息。
        print(f"cr_origin: {cr.cr_origin}")
        sys.exit(0)
    except Exception:
        sys.exit(1)


if __name__ == '__main__':
    asyncio.run(main())

