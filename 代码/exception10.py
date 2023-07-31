print("这是一个判断整数符号的小游戏。\n")

while True:
    try:
        s = input("请输入一个整数：")
        if s == "quit":
            print("你已经退出了游戏。\n")
            break
        n = int(s)
    except ValueError:
        print("您输入的并非整数。")
    except Exception:
        print("发生了未知错误。")
    else:
        if n < 0:
            print("这是一个负数。")
        elif n > 0:
            print("这是一个正数。")
        else:
            print("这是零。")

