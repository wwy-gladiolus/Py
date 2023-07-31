import asyncio
import sys


#自定义一个异步迭代器类。
class MyAsyncIterator:
    def __init__(self, n):
        self.max_n = int(n)
        self.n = 0

    #满足异步迭代器协议对__aiter__的要求。
    def __aiter__(self):
        return self

    #满足异步迭代器协议对__anext__的要求。
    async def __anext__(self):
        await asyncio.sleep(0.3)
        if self.n >= self.max_n:
            raise StopAsyncIteration()
        self.n += 1
        return self.n


async def main():
    #验证第一个异步可迭代对象。
    my_aiter1 = MyAsyncIterator(3)
    try:
        print("my_aiter1:")
        for i in range(4):
            print(await anext(my_aiter1))
    except StopAsyncIteration as e:
        print(repr(e))
    finally:
        print("")
    #验证第二个异步可迭代对象。
    my_aiter2 = MyAsyncIterator(2)
    print("my_aiter2:")
    for i in range(4):
        print(await anext(my_aiter2, -1))
    print("")
    #验证第三个异步可迭代对象。
    my_aiter3 = MyAsyncIterator(-10)
    print("my_aiter3:")
    for i in range(4):
        print(await anext(my_aiter3, False))
    print("")
    #验证async for语句。
    print("async for:")
    async for n in MyAsyncIterator(5):
        print(n)
    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())


