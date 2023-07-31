#该函数接收一个异常组，将其自动抛出，然后以except子句对异常组进行处理。
def eg_handler(eg):
    try:
        raise(eg)
    except ExceptionGroup as e:
        print("An ExceptionGroup!")
        print(e.message)
        n = len(e.exceptions)
        i = 0
        while i < n:
            print(repr(e.exceptions[i]))
            i = i + 1
    except BaseExceptionGroup as e:
        print("An BaseExceptionGroup!")
        print(e.message)
        n = len(e.exceptions)
        i = 0
        while i < n:
            print(repr(e.exceptions[i]))
            i = i + 1
    return None
