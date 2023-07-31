#这是一个用for语句迭代字典的视图例子。


#迭代键构成的视图。
def print_dictionary_keys(dict):
    #遍历字典中的键。
    for key in dict.keys():
        print(key)
    else:
        print("Traversal finished.")


#迭代值构成的视图。
def print_dictionary_values(dict):
    #遍历字典中的值。
    for value in dict.values():
        print(value)
    else:
        print("Traversal finished.")


#迭代键值对构成的视图。
def print_dictionary_items(dict):
    #遍历字典中的键值对。
    for item in dict.items():
        print(item)
    else:
        print("Traversal finished.")
