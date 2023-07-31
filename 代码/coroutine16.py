#!/usr/bin/env python3

import asyncio
import random
import sys


#该协程函数创建的协程当even_event事件被设置时在0.4秒后显示“*”。
async def star(event):
    while True:
        #等待事件被设置。
        await event.wait()
        #这里等待0.4秒是人为添加的，其实不需要。
        await asyncio.sleep(0.4)
        #取消事件的设置。
        event.clear()
        #处理该事件的代码。
        sys.stdout.write("* ")
        sys.stdout.flush()


#该协程函数创建的协程当odd_event事件被设置时在0.4秒后显示“$”。
async def dollar(event):
    while True:
        #等待事件被设置。
        await event.wait()
        #这里等待0.4秒是人为添加的，其实不需要。
        await asyncio.sleep(0.4)
        #取消事件的设置。
        event.clear()
        #处理该事件的代码。
        sys.stdout.write("$ ")
        sys.stdout.flush()


#该协程函数创建的协程每隔0.5秒随机生成一个0~100内的整数。  如果该整数是偶数，则设置
# even_event事件；如果该整数是奇数，则设置odd_event事件。
async def num_gen(event1, event2):
    while True:
        n = random.randrange(100)
        if n % 2 == 0:
            #设置even_event事件。
            event1.set()
        else:
            #设置odd_event事件。
            event2.set()
        await asyncio.sleep(0.5)


async def main():
    #创建even_event事件，代表num_gen()生成了一个偶数。
    even_event = asyncio.Event()
    #创建odd_event事件，代表num_gen()生成了一个奇数。
    odd_event = asyncio.Event()
    #创建三个任务并将它们聚集成一个任务。
    task_star = asyncio.create_task(star(even_event))
    task_dollar = asyncio.create_task(dollar(odd_event))
    task_num_gen = asyncio.create_task(num_gen(even_event, odd_event))
    task = asyncio.gather(task_star, task_dollar, task_num_gen)
    try:
        #运行任务2.6秒。
        await asyncio.wait_for(task, 2.6)
    except asyncio.TimeoutError:
        print("")
        #判断任务运行完成时是否还有未处理的事件。
        if even_event.is_set():
            #even_event事件未处理。
            print("The cancelled symbol is *.")
        elif odd_event.is_set():
            #odd_event事件未处理。
            print("The cancelled symbol is $.")
        else:
            #所有事件都已经处理。
            print("No symbol is cancelled.")
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
