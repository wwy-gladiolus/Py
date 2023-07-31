#!/usr/bin/env python3

import sys


#该程序判断一个正整数是否是质数。
def main():
    while True:
        try:
            #从标准输入读取整数。
            n = int(input())
            if n < 0:
                raise RuntimeError()
            if n == 0 or n == 1:
                #将结果写入标准输出。
                print(f"{n} is not a prime.")
                continue
            for m in range(2, n):
                if n % m == 0:
                    #将结果写入标准输出。
                    print(f"{n} is not a prime, it equals {n//m}*{m}.")
                    break
            #将结果写入标准输出。
            if m == n-1:
                print(f"{n} is a prime.")
        except Exception:
            #将错误信息写入标准出错。
            sys.stderr.write("Only accept natural number or -1!\n")
            sys.stderr.flush()
    return 0

if __name__ == '__main__':
    sys.exit(main())
