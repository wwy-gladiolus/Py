#该函数以冒泡排序算法对列表进行排序，其参数compare需被传入一个返回布尔值的函数，
# 而该函数自身的返回值是排好序的列表。
def bubble_sort(lt, compare=lambda a, b: a < b):
    #如果传入列表的成员数少于2，直接返回该列表。
    lt_len = len(lt)
    if lt_len < 2:
        return lt

    #创建一个新列表，然后依次取出原列表的成员，与新列表的已有成员基于回调函数进行
    # 比较，在回调函数第一次返回True的索引处插入该成员。
    nlt = [lt[0]]
    i = 1
    while i < lt_len:
        nlt_len = len(nlt)
        j = 0
        while j < nlt_len: 
            if compare(lt[i], nlt[j]):
                nlt.insert(j, lt[i])
                break
            j = j + 1
        else:
            nlt.append(lt[i])
        i = i + 1

    return nlt

