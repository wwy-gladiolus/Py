#!/usr/bin/env python3

import asyncio
import sys


async def stopwatch(sec):
    n = 0
    while n < sec:
        sys.stdout.write(str(sec - n) + ' ')
        sys.stdout.flush()
        n = await asyncio.sleep(1, n + 1)
    sys.stdout.write('0\n')
    sys.stdout.flush()


async def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        sec = int(sys.argv[1])
        await stopwatch(sec)
        sys.exit(0)
    except Exception:
        sys.exit(1)


#使用Runner对象代替asyncio.run()函数。
if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(main())
