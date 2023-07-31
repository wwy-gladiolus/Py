import math
import asyncio
import sys


#自定义一个异步上下文管理器类。
class MyAsyncContextManager():
    async def __aenter__(self):
        await asyncio.sleep(1)
        def f(x, y):
            return math.sqrt(x)/y
        return f

    async def __aexit__(self, exc_type, exc_value, traceback):
        if exc_type == TypeError:
            print('Please enter two numbers!')
            return True
        elif exc_type == ValueError:
            print('x must be non-negative!')
            return True
        else:
            return False


#该协程函数通过async with语句使用自定义异步上下文管理器。
async def g(x, y):
    async with MyAsyncContextManager() as f:
        print(f(x, y))


async def main():
    await g(1, 2)
    await g('a', 'b')
    await g(-1, 2)
    await g(1, 0)
    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())

