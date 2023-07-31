#!/usr/bin/env python3

import asyncio
import random
import sys

resource = ['*', '$', '#']
resource_lock = asyncio.Lock()
#写保护锁，在执行写操作期间需要一直持有该锁。  而在执行读操作时先要获得该锁，在获得
# 资源锁后释放。
write_lock = asyncio.Lock()
read_count = 0
#记录当前写者数量的计数器。
write_count = 0


async def writer(data, name):
    global resource, resource_lock, write_lock, write_count
    #写者的数量加1。
    write_count = write_count + 1
    #如果该写者是第一个，则申请获得写保护锁。
    if write_count == 1:
        await write_lock.acquire()
    await resource_lock.acquire()
    for i in range(3):
        t = random.random()
        await asyncio.sleep(t)
        resource[i] = data[i]
        print(f"{name}: write {data[i]}, now {resource[0] + resource[1] + resource[2]}")
    resource_lock.release()
    #写者的数量减1。
    write_count = write_count - 1
    #如果该写者是最后一个，则释放写保护锁。
    if write_count == 0:
        write_lock.release()


async def reader(name):
    global resource, resource_lock, read_count, write_lock
    #申请获得写保护锁。
    await write_lock.acquire()
    read_count = read_count + 1
    if read_count == 1:
        await resource_lock.acquire()
    #释放写保护锁。
    write_lock.release()
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
