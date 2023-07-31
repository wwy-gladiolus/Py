#!/usr/bin/env python3

import asyncio
import sys


#该任务基于正整数n生成一个数列并写入标准输出。
async def seq_gen(n):
    try:
        #终止条件是n小于等于0。
        while n > 0:
            sys.stdout.write(str(n) + " ")
            sys.stdout.flush()
            #如果n是19的倍数，则抛出RuntimeError异常。
            if n % 19 == 0:
                raise RuntimeError()
            #如果n是11的倍数，则取消该任务。
            if n % 11 == 0:
                #调用自身的cancel()。
                asyncio.current_task().cancel()
            #数列的推导公式是a(n) = int(a(n-1)/7) - 1。
            n = n // 7 - 1
            await asyncio.sleep(1)
    finally:
        print("\n")
    return n


#该函数通过访问任务的属性获得任务相关信息。
def show_task_result(task):
    #确定任务的当前状态。
    print("task.cancelled() ==", task.cancelled())
    print("task.done() ==", task.done())
    try:
        #取得任务的结果，注意这可能导致抛出异常。
        print("task.result() ==", task.result())
        print("task.exception() ==", task.exception())
    except BaseException as e:
        print("task.result() ==", repr(e))
        print("task.exception() ==", repr(e))


#主协程函数将第一个命令行参数视为数列的起始项。
async def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        task = asyncio.create_task(seq_gen(n))
        await task
    except (asyncio.CancelledError, RuntimeError):
        #数列未完全生成。
        print("The sequence is truncated!")
        show_task_result(task)
    except Exception:
        sys.exit(1)
    else:
        #数列完全生成。
        print("The sequence is fully generated.")
        show_task_result(task)
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
