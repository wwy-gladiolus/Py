import re

print("这是一个判断整数符号的小游戏。\n")

while True:
    s = input("请输入一个整数：")

    #当读取的字符串是“quit”时，跳出循环。
    if s == "quit":
        break

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

#本提示仅当循环语句执行完成后才会被输出。
print("你已经退出了游戏。\n")

