import typing
import time


class Message(typing.TypedDict):
    uid: int
    time: typing.NotRequired[time.struct_time]
    content: str


print(f"Message.__total__ == {Message.__total__}")
print(f"Message.__required_keys__ == {Message.__required_keys__}")
print(f"Message.__optional_keys__ == {Message.__optional_keys__}")

#该赋值语句不会报错。
msg1 = Message(uid=0, content="Hello")
#该赋值语句不会报错。
msg2 = Message(uid=0, time=time.localtime(), content="Hello")
#该赋值语句会因却缺少content属性而报错。
msg3 = Message(uid=0, time=time.localtime())
#该赋值语句会因却缺少uid属性而报错。
msg4 = Message(content="Hello")
#该赋值语句会因却多出了data属性而报错。
msg5 = Message(uid=0, content="Hello", data=0)

