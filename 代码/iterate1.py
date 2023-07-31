#这是一个用while语句迭代序列的例子。
def print_sequence(seq):
    #取得序列的长度。
    length = len(seq)
    #基于索引遍历序列中的元素。
    i = 0
    while i < length:
        print(seq[i])
        i += 1
    else:
        print("Totally " + str(length) + " elements.")
