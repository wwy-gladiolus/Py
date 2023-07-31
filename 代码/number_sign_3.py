import re

s = input("请输入一个整数：")

if s != "quit":
    if re.match(r"^[+\-]?[0-9]+$", s):
        n = int(s)
        if n < 0:
            print("这是一个负数。")
        elif n > 0:
            print("这是一个正数。")
        else:
            print("这是零。")
    else:
        print("您输入的并非整数。")
