#这是一个用for语句迭代字典的例子。
def print_dictionary(dict):
    #遍历字典中的元素。
    for key in dict:
        print(str(key) + ": " + str(dict[key]))
    else:
        print("Traversal finished.")
