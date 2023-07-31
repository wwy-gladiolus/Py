#!/usr/bin/env python3
#
#这是一个用于展示规范格式的Python脚本。

"""This module defines a factorial sequence generator.

    The function factorial_sequence() generate the sequence and return it as a list.

    When runs as the main module, it asks the user to enter an integer, then print the according factorial sequence.
"""

import sys
import re

__all__ = ['factorial_sequence']


#该函数根据参数n生成序列[1!, 2!, ..., n!]。
def factorial_sequence(n):
    """This function is the factorial sequence generator."""

    l = []
    i = 1
    factorial = 1

    while i <= n:
        factorial = factorial * i
        i = i + 1
        l.append(factorial)

    return l


#入口点函数。
def main():
    """This function is called when this script runs in the top-level environment."""

    print("这是一个生成阶乘序列的工具。输入“quit”退出。\n")

    while True:
       s = input("请输入一个正整数：")
       if s == "quit":
           break
       if re.match(r"^[1-9][0-9]*$", s):
           n = int(s)
           print(factorial_sequence(n))
       else:
           print("您输入的并非正整数。")

    return 0


#判断脚本是否在顶层环境中被执行。
if __name__ == '__main__':
    sys.exit(main())


