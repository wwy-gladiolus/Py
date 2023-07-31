#!/usr/bin/env python3

import asyncio
import random
import sys

resource = ['*', '$', '#']
resource_lock = asyncio.Lock()
#排队锁，不论执行读操作还是写操作都要先获得该锁，在获得资源锁后释放。
queue_lock = asyncio.Lock()
read_count = 0


async def writer(data, name):
    global resource, resource_lock, queue_lock
    #申请获得排队锁。
    await queue_lock.acquire()
    await resource_lock.acquire()
    #释放排队锁。
    queue_lock.release()
    for i in range(3):
        t = random.random()
        await asyncio.sleep(t)
        resource[i] = data[i]
        print(f"{name}: write {data[i]}, now {resource[0] + resource[1] + resource[2]}")
    resource_lock.release()


async def reader(name):
    global resource, resource_lock, read_count, queue_lock
    #申请获得排队锁。
    await queue_lock.acquire()
    read_count = read_count + 1
    if read_count == 1:
        await resource_lock.acquire()
    #释放排队锁。
    queue_lock.release()
    for i in range(3):
        t = random.random()
        await asyncio.sleep(t)
        print(f"{name}: read {resource[i]}")
    read_count = read_count - 1
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
