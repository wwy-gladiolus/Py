#!/usr/bin/env python3

import asyncio
import time
import sys


async def main():
    #显示开始执行的时间。
    print(f'start at {time.strftime("%X")}.')
    #创建三个子进程分别以不同的参数执行coroutine38.py。  子进程proc1将a1.txt拷贝
    # 到b1.txt。
    proc1 = await asyncio.create_subprocess_exec("./coroutine38.py", "a1.txt", "b1.txt")
    #proc1 = await asyncio.create_subprocess_shell("./coroutine38.py a1.txt b1.txt")
    #子进程proc2将a2.txt拷贝到b2.txt。
    proc2 = await asyncio.create_subprocess_exec("./coroutine38.py", "a2.txt", "b2.txt")
    #proc2 = await asyncio.create_subprocess_shell("./coroutine38.py a2.txt b2.txt")
    #子进程proc3将a3.txt拷贝到b3.txt。
    proc3 = await asyncio.create_subprocess_exec("./coroutine38.py", "a3.txt", "b3.txt")
    #proc3 = await asyncio.create_subprocess_shell("./coroutine38.py a3.txt b3.txt")
    #等待三个子进程都执行完成。
    result = await asyncio.gather(proc1.wait(), proc2.wait(), proc3.wait(), return_exceptions=True)
    #显示三个子进程的退出状态。
    print(result)
    #显示执行完成的时间。
    print(f'end at {time.strftime("%X")}.')
    sys.exit(0)

if __name__ == '__main__':
    asyncio.run(main())
