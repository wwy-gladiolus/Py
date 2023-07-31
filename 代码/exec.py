import re

a = 15
b = 6
c = 79

while True:
    expr = input("请输入一个以a、b和c中的两个作为参数的四则运算式（输入空串终止）：")
    if expr:
        if re.match(r"^[abc][\+\-\*\/][abc]$", expr):
            code = 'print("' + expr + '的结果为" + str(' + expr + ') + "。")'
            exec(code)
        else:
            print("请输入正确的运算式！")
    else:
        break

