#!/usr/bin/env python3

import io
import time
import sys


#主函数先睡眠3秒，然后将第一个命令行参数指定的文件的内容拷贝到第二个命令行参数指定的
# 文件。
def main():
    time.sleep(3)
    if len(sys.argv) < 3:
        #如果命令行参数少于2个，则通过标准出错报错。
        sys.stderr.write("Not enough arguments.\n")
        sys.stderr.flush()
        return 1
    try:
        source = io.FileIO(sys.argv[1])
        target = io.FileIO(sys.argv[2], 'w')
        pair = io.BufferedRWPair(source, target)
        content = pair.read(10)
        while content:
            pair.write(content)
            content = pair.read(10)
        pair.close()
        #如果拷贝成功，则通过标准输出给出提示信息。
        sys.stdout.write(f"Successfully copy from {sys.argv[1]} to {sys.argv[2]}.\n")
        sys.stdout.flush()
    except Exception as e:
        #如果抛出了异常，则通过标准出错报错。
        sys.stderr.write(repr(e) + "\n")
        sys.stderr.flush()
        return 2
    return 0

if __name__ == '__main__':
    sys.exit(main())
