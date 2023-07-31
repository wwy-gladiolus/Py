#!/usr/bin/env python3

import asyncio
import random
import sys

resource = ['*', '$', '#']
#资源锁，在进行读操作和写操作期间都需要一直持有该锁。
resource_lock = asyncio.Lock()
#记录当前读者数量的计数器。
read_count = 0


async def writer(data, name):
    global resource, resource_lock
    #申请获得资源锁。
    await resource_lock.acquire()
    for i in range(3):
        t = random.random()
        await asyncio.sleep(t)
        resource[i] = data[i]
        print(f"{name}: write {data[i]}, now {resource[0] + resource[1] + resource[2]}")
    #释放资源锁。
    resource_lock.release()


async def reader(name):
    global resource, resource_lock, read_count
    #读者的数量加1。
    read_count = read_count + 1
    #如果该读者是第一个，则申请获得资源锁。
    if read_count == 1:
        await resource_lock.acquire()
    for i in range(3):
        t = random.random()
        await asyncio.sleep(t)
        print(f"{name}: read {resource[i]}")
    #读者的数量减1。
    read_count = read_count - 1
    #如果该读者是最后一个，则释放资源锁。
    if read_count == 0:
        resource_lock.release()


async def main():
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
