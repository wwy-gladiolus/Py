#!/usr/bin/env python3
#
#本脚本以同步编程的方式实现coroutine1.py的功能。

import time
import sys


#该函数代表秒表。  sec参数传入需计时的秒数。
def stopwatch(sec):
    n = 0
    while n < sec:
        sys.stdout.write(str(sec - n) + ' ')
        sys.stdout.flush()
        #强制等待1秒钟。
        time.sleep(1)
        n = n + 1
    sys.stdout.write('0\n')
    sys.stdout.flush()


#主函数将第一个命令行参数解读为需计时的秒数。
def main():
    if len(sys.argv) < 2:
        return 1
    try:
        sec = int(sys.argv[1])
        #stopwatch()是以同步方式运行的。
        stopwatch(sec)
        return 0
    except Exception:
        return 1


#调用主函数。
if __name__ == '__main__':
    sys.exit(main())
