#!/usr/bin/env python3

import asyncio
import sys

#该全局变量控制着协程是否抛出异常。
#fail = False
fail = True


#该协程可能执行完成，也可能抛出异常。
async def coro():
    if fail:
        raise RuntimeError()


#该函数分析任务包装协程的栈。
def show_stack(task, l):
    #获得该任务包装协程的栈框架并显示。
    stack = task.get_stack(limit=l)
    print(f"{task.get_name()}'s stack frames:")
    print(stack)
    print("")
    #显示该任务包装协程的栈框架相关信息。
    print(f"{task.get_name()}'s stack info:")
    task.print_stack(limit=l)
    print("")


async def main():
    #创建任务task1，但未执行。
    task1 = asyncio.create_task(coro(), name="task1")
    show_stack(task1, 3)
    #执行该任务到它正常返回或抛出异常。
    try:
        await task1
        show_stack(task1, 3)
    except Exception:
        show_stack(task1, 3)
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())

