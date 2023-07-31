#!/usr/bin/env python3
#
#这是一个用来阐述如何进行调试的Python脚本。

"""This module illustrates how to debug with pdb.

    In this module, two functions to calculate factorial are defined, one uses loop and the other uses recursion.
"""

import sys, pdb

__all__ = ['factorial1', 'factorial2']


#这是一个通过循环实现阶乘的函数。
def factorial1(n):
    """This function calculates n! using loop."""

    product = 1
    while n > 1:
        #pdb.set_trace(header="start loop")
        product = product * n
        n = n-1
    return product


#这是一个通过递归实现阶乘的函数。
def factorial2(n):
    """This function calculates n! using recursion."""

    #breakpoint()
    if n > 1:
        return n * factorial2(n-1)
    else:
        return 1


#入口点函数。
def main():
    """This function is called when this script runs in the top-level environment."""

    result = factorial1(3)
    print(result)
    result = factorial2(3)
    print(result)

    return 0


#判断脚本是否在顶层环境中运行。
if __name__ == '__main__':
    sys.exit(main())
