#定义一个重复字符串的函数，并通过标注说明：
#  形式参数s需被传入一个字符串。
#  形式参数n需被传入一个整数。
#  返回值是一个字符串。
def str_multiplier(s: str, n: int = 2) -> str:
    return s * n

#调用该函数，并按标注的要求传入实际参数。
print(str_multiplier("abc"))

#调用该函数，给s传入一个二进制串。
print(str_multiplier(b"01", 3))

#调用该函数，给s传入一个整数，给n传入一个浮点数。
print(str_multiplier(10, 4.5))
