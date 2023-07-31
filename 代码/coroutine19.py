#!/usr/bin/env python3

import asyncio
import random
import time
import sys

#该全局变量被用于表示该监视器涉及的两种条件。  当其引用True时，代表生成了偶数。  当其
# 引用False时，代表生成了奇数。
even_number = None


async def stars(cond):
    try:
        while True:
            #申请获得底层锁，进入临界区。
            await cond.acquire()
            #仅当event_number引用False时等待监视器，并释放底层锁，离开临界区。  否
            # 则会继续执行。
            await cond.wait_for(lambda: even_number)
            #仅当event_number引用True时申请获得底层锁，进入临界区。
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("*")
                sys.stdout.flush()
            print("")
            #释放底层锁，离开临界区。
            cond.release()
    except asyncio.CancelledError:
        cond.release()
        raise


async def dollars(cond):
    try:
         while True:
            #申请获得底层锁，进入临界区。
            await cond.acquire()
            #仅当event_number引用True时等待监视器，并释放底层锁，离开临界区。  否则
            # 会继续执行。
            await cond.wait_for(lambda: not even_number)
            #仅当event_number引用False时申请获得底层锁，进入临界区。
            for i in range(3):
                await asyncio.sleep(0.1)
                sys.stdout.write("$")
                sys.stdout.flush()
            print("")
            #释放底层锁，离开临界区。
            cond.release()
    except asyncio.CancelledError:
        cond.release()
        raise


#该协程函数创建的协程通过监视器来获得和释放底层锁，但并不等待监视器。
async def num_gen(cond):
    #声明全局变量。
    global even_number
    while True:
        #申请获得底层锁，进入临界区。
        await cond.acquire()
        n = random.randrange(100)
        if n % 2 == 0:
            #设置even_number引用True。
            even_number = True
        else:
            #设置even_number引用False。
            even_number = False
        #通知所有等待监视器的任务。
        cond.notify_all()
        #释放底层锁，离开临界区。
        cond.release()
        await asyncio.sleep(0)


async def main():
    #直接创建一个监视器，并将自动创建的底层锁关联到标准输出。
    cond = asyncio.Condition()
    task_num_gen = asyncio.create_task(num_gen(cond))
    task_stars = asyncio.create_task(stars(cond))
    task_dollars = asyncio.create_task(dollars(cond))
    task = asyncio.gather(task_num_gen, task_stars, task_dollars)
    try:
        await asyncio.wait_for(task, 2)
    except asyncio.TimeoutError:
        pass
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
