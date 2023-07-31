#!/usr/bin/env python3

import asyncio
import sys

#该函数创建指定类型的异步队列，然后以同步方式用指定的数据将其填满，最后再以同步方式取
#出所有数据。  队列的状态变化会被显示。
def dynamic_queue(data, priority, quetype="Queue"):
    #创建指定类型的异步队列，容量都是3。
    if quetype == "PriorityQueue":
        q = asyncio.PriorityQueue(3)
        print("\nq is a priority queue:")
    elif quetype == "LifoQueue":
        q = asyncio.LifoQueue(3)
        print("\nq is a LIFO queue (stack):")
    else:
        q = asyncio.Queue(3)
        print("\nq is a FIFO queue:")
    #显示队列的初始状态：
    print(f"q.maxsize == {q.maxsize}")
    print(f"q.empty() == {q.empty()}")
    #用指定的数据填满队列：
    n = 0
    while True:
        try:
            #对于FIFO队列和LIfO队列来说，数据项是一个元组。  对于优先级队列来说，
            # 元组的第一个元素是优先级，第二个元素才是数据项。
            q.put_nowait((priority[n], data[n]))
            print(f"q.qsize() == {q.qsize()}")
            n = n + 1
        #抛出asyncio.QueueFull异常说明队列已满。
        except asyncio.QueueFull:
            print(f"q.full() == {q.full()}")
            break
    #取出所有数据：
    while True:
        try:
            d = q.get_nowait()
            print(d)
            print(f"q.qsize() == {q.qsize()}")
        #抛出asyncio.QueueEmpty异常说明队列已空。
        except asyncio.QueueEmpty:
            print(f"q.empty() == {q.empty()}")
            break


def main():
    #准备好数据和优先级。
    data = 'abcd'
    priority = (20, 30, 10, 40)
    print(f'Data is "{data}".')
    print(f"Priorities is {priority}.")
    #验证队列的性质。
    dynamic_queue(data, priority)
    #验证栈的性质。
    dynamic_queue(data, priority, "LifoQueue")
    #验证优先级队列的性质。
    dynamic_queue(data, priority, "PriorityQueue")
    return 0


if __name__ == '__main__':
    sys.exit(main())
