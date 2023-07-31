#!/usr/bin/env python3

import asyncio
import random
import sys

#被读者和写者共享的资源。
resource = ['*', '$', '#']


#该协程函数创建的协程为写者。  它们会用data中的元素按顺序依次替换resource中的三个元素，
# 每次替换前随机等待0~1秒，替换后显示操作成功相关信息。
async def writer(data, name):
    global resource
    for i in range(3):
        t = random.random()
        await asyncio.sleep(t)
        resource[i] = data[i]
        print(f"{name}: write {data[i]}, now {resource[0] + resource[1] + resource[2]}")


#该协程函数创建的协程为读者。  它们会按顺序依次读取resource中的三个元素，每次读取前随机
# 等待0~1秒，读取后显示操作成功相关信息。
async def reader(name):
    global resource
    for i in range(3):
        t = random.random()
        await asyncio.sleep(t)
        print(f"{name}: read {resource[i]}")


async def main():
    #定义4个读者和2个写者，按照r1，w1，r2，r3，w2，r4的顺序执行读写操作。
    r1 = asyncio.create_task(reader("r1"))
    w1 = asyncio.create_task(writer("abc", "w1"))
    r2 = asyncio.create_task(reader("r2"))
    r3 = asyncio.create_task(reader("r3"))
    w2 = asyncio.create_task(writer("def", "w2"))
    r4 = asyncio.create_task(reader("r4"))
    await asyncio.gather(r1, w1, r2, r3, w2, r4)
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
