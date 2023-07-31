from typing import TypeGuard, Tuple


#该TypeGuard结构表明，当is_record()返回True时，通过data参数传入的是一个(str, int)
# 格式的二元组。
def is_record(data: tuple) -> TypeGuard[Tuple[str, int]]:
    if len(data) != 2:
        return False
    if isinstance(data[0], str) and isinstance(data[1], int):
        return True
    else:
        return False


print(is_record((0, 1)))    #显示False。
print(is_record(('abc', 0, 1)))    #显示False。
print(is_record(('abc', 0)))    #显示True。
print(is_record((b'abc', 0.0)))    #显示False。

