#!/usr/bin/env python3

import asyncio
import sys

async def console(proc):
    while True:
        try:
            #从标准输入读取数据。
            data = input("Please enter a natural number, -1 means quit: ")
            #当读取到-1时终止程序。
            if data == "-1":
                print("Closed!")
                #向子进程的标准输入写入EOF。
                proc.stdin.write_eof()
                try:
                    #先尝试正常终止子进程。
                    proc.terminate()
                except Exception:
                    #杀死子进程。
                    proc.kill()
                #跳出循环，终止程序。
                break
            #将读取到的数据写入子进程的标准输入。
            proc.stdin.write((data + "\n").encode())
            #创建一个任务从子进程的标准输出中读取一行。
            task1 = asyncio.create_task(proc.stdout.readline())
            #创建一个任务从子进程的标准出错中读取一行。
            task2 = asyncio.create_task(proc.stderr.readline())
            #等待两个任务之一完成。
            done, pending = await asyncio.wait([task1, task2], return_when=asyncio.FIRST_COMPLETED)
            #输出子进程返回的信息。
            for task in done:
                print(task.result().decode())
            #取消尚未完成的任务。
            for task in pending:
                task.cancel()
        except Exception as e:
            print(repr(e))
    return 0


async def main():
    #创建一个子进程执行coroutine40.py。
    proc = await asyncio.create_subprocess_exec("./coroutine40.py", stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    #proc = await asyncio.create_subprocess_shell("./coroutine40.py", stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    #将控制该子进程的Process对象传给console，创建相应协程并等待。
    await console(proc)
    sys.exit(0)

if __name__ == '__main__':
    asyncio.run(main())
