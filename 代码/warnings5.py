import warnings


def __myshowwarning(message, category, filename, lineno, file=None, line=None):
    if isinstance(message, Warning):
        category = message.__class__
    msg = (str(category) + ": " + str(message) + "\n"
            + filename + ", line " + str(lineno) + "\n")
    if line is not None:
        msg = msg + "  " + line + "\n"
    print(msg)


warnings.showwarning = __myshowwarning


def f(a, b, c):
    warnings.warn('Using this function should be warned!')
    return a*b-c
