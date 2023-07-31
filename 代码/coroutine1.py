#!/usr/bin/env python3

import asyncio
import sys


#该协程函数创建的协程代表秒表。  sec参数传入需计时的秒数。
async def stopwatch(sec):
    n = 0
    while n < sec:
        #输出当前剩余秒数并立即显示。
        sys.stdout.write(str(sec - n) + ' ')
        sys.stdout.flush()
        #等待一个耗时1秒的协程执行完成。
        n = await asyncio.sleep(1, n + 1)
    #输出剩余秒数0并立即显示。
    sys.stdout.write('0\n')
    sys.stdout.flush()


#该主协程函数将第一个命令行参数解读为需计时的秒数。
async def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        sec = int(sys.argv[1])
        #等待stopwatch()返回的协程执行完成。
        await stopwatch(sec)
        sys.exit(0)
    except Exception:
        sys.exit(1)


#执行主协程函数创建的主协程。
if __name__ == '__main__':
    asyncio.run(main())
