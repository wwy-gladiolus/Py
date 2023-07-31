import re

print("这是一个判断整数符号的小游戏。\n")

#对变量s赋初始值并保证其逻辑值检测的结果为True。  这样才能避免循环在第一次计算条件
# 表达式时终止。
s = "begin"

#只要读取到的字符串不是“quit”，就会继续读取。  而当读取到“quit”后，则输出游戏结束
# 的提示。
while s != "quit":
    #由于每次循环都读取了不同的字符串，而“quit”会使条件表达式的值的逻辑值检测结果
    # 为False，所以该循环不会是死循环。
    s = input("请输入一个整数：")

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
else:
    print("你已经退出了游戏。\n")
