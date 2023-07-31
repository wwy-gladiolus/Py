import re


#定义函数number_sign_game()。  该函数没有形式参数。
def number_sign_game():
    print("这是一个判断整数符号的小游戏。\n")

    while True:
        s = input("请输入一个整数：")

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

    print("你已经退出了游戏。\n")


#调用函数number_sign_game()。
number_sign_game()

