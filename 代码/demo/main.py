import re
from .factorial_sequence import *

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

