#!/usr/bin/env python3

import asyncio
import sys


#该协程函数使用了递归。
async def stopwatch(sec):
    await asyncio.sleep(1)
    if sec <= 0:
        sys.stdout.write('0\n')
        sys.stdout.flush()
        return
    else:
        sys.stdout.write(str(sec) + ' ')
        sys.stdout.flush()
        await(stopwatch(sec -1))


async def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        sec = int(sys.argv[1])
        await stopwatch(sec)
        sys.exit(0)
    except Exception:
        sys.exit(1)


if __name__ == '__main__':
    asyncio.run(main())
