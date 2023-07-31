import functools
import sys


#定义通过递归计算斐波那契数列的函数。
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#生成斐波那契数列的前15项，并记录内存使用情况。
seq = []
n = 0
#清理内部的类型缓存。
sys._clear_type_cache()
#显示初始状态下数列的值、占用内存和已分配块数。
print(f'seq: {seq}')
print(f'seq size: {sys.getsizeof(seq)}')
print(f'block number: {sys.getallocatedblocks()}')
while n < 15:
    #向数列中插入一项。
    seq.append(fibonacci(n))
    #显示当前状态下数列的值、占用内存和已分配块数。
    print(f'seq: {seq}')
    print(f'seq size: {sys.getsizeof(seq)}')
    print(f'block number: {sys.getallocatedblocks()}')
    n += 1

