import asyncio
import sys


#定义用于实现异步推导式的异步迭代器类。
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
        return self.n


async def main():
    #验证异步列表推导式。
    l = [x*y async for x in MyAsyncIterator(3) for y in 'ab' + 'c' if not (x==2 and y=='b')]
    print(l)
    #验证异步集合推导式。
    st = {(x, y) async for x in MyAsyncIterator(9) if x%3 !=0 for y in range(x, 10) if y*x > 50}
    print(st)
    #验证异步字典推导式。
    d = {x-1: (x-1)**2 async for x in MyAsyncIterator(10)}
    print(d)
    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
