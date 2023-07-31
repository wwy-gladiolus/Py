import random
import asyncio
import sys


#定义第一个异步生成器函数。
async def async_gen1():
    await asyncio.sleep(0.3)
    print("A")
    yield 1
    await asyncio.sleep(0.3)
    print("B")
    yield 2
    await asyncio.sleep(0.3)
    print("C")
    yield 3
    await asyncio.sleep(0.3)
    print("D")
    return


#定义用于支持异步生成器表达式的异步迭代器类。
class MyAsyncIterator:
    def __init__(self, n):
        self.max_n = int(n)
        self.n = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        await asyncio.sleep(0.3)
        if self.n >= self.max_n:
            raise StopAsyncIteration()
        self.n += 1
        return self.n - 1


#定义第三个异步生成器函数。
async def async_gen3(start, upper_limit):
    n = start
    while n < upper_limit:
        await asyncio.sleep(0.3)
        print(n)
        n *= (yield n)


#定义第四个异步生成器函数。
async def async_gen4():
    try:
        while True:
            await asyncio.sleep(0.3)
            n = random.random()
            yield n
    except RuntimeError:
        return


#定义第五个异步生成器函数。
async def async_gen5():
    try:
        while True:
            await asyncio.sleep(0.3)
            n = random.random()
            yield n
    except Exception:
        print("Stop generates random numbers.")
        return


async def main():
    #验证第一个异步生成器函数。
    ag1 = async_gen1()
    print("ag1:")
    print(type(ag1))
    try:
        for i in range(4):
            print(await anext(ag1))
    except StopAsyncIteration as e:
        print(repr(e))
    finally:
        print("")
    #验证异步生成器表达式。
    ag2 = ((x, y) async for x in MyAsyncIterator(2) for y in (x, 2))
    print("ag2:")
    print(type(ag2))
    async for coordinate in ag2:
        print(coordinate)
    print("")
    #验证第三个异步生成器函数。
    ag3 = async_gen3(2, 100000)
    print("ag3:")
    try:
        n = await ag3.asend(None)
        while True:
            n = await ag3.asend(n)
    except StopAsyncIteration:
        print("Bigger than upper limit!")
    finally:
        print("")
    #验证第四个异步生成器函数。
    ag4 = async_gen4()
    print("ag4:")
    for i in range(3):
        print(await ag4.asend(None))
    try:
        await ag4.athrow(RuntimeError())
    except Exception as e:
        print(repr(e))
    finally:
        print("")
    #验证第五个异步生成器函数。
    ag5 = async_gen5()
    print("ag5:")
    for i in range(2):
        print(await ag5.asend(None))
    await ag5.aclose()
    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())


