def f(a):
    try:
        return 'str:' + a
    except TypeError:
        return 'str:Please enter a string!'
