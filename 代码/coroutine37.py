#!/usr/bin/env python3

import asyncio
import time
import sys


#该函数模拟需要执行阻塞I/O的函数。
def blocked_io(oprand1, oprand2, operator):
    #阻塞3秒。
    time.sleep(3)
    return eval(str(oprand1) + str(operator) + str(oprand2))


async def main():
    print(f'start at {time.strftime("%X")}.')
    #创建四个线程分别执行blocked_io()的一次调用。
    coro1 = asyncio.to_thread(blocked_io, 35, 17, "+")
    coro2 = asyncio.to_thread(blocked_io, 35, 17, "-")
    coro3 = asyncio.to_thread(blocked_io, 35, 17, "*")
    coro4 = asyncio.to_thread(blocked_io, 35, 17, "/")
    #使这四个线程并行执行。
    result = await asyncio.gather(coro1, coro2, coro3, coro4)
    print(f'{time.strftime("%X")}: 35+17={result[0]}')
    print(f'{time.strftime("%X")}: 35-17={result[1]}')
    print(f'{time.strftime("%X")}: 35*17={result[2]}')
    print(f'{time.strftime("%X")}: 35/17={result[3]}')
    sys.exit(0)

if __name__ == '__main__':
    asyncio.run(main())
