import sys

_old__interactivehook__ = sys.__interactivehook__

def echo():
    print("Interactive Mode!")
    if _old__interactivehook__:
        _old__interactivehook__()

sys.__interactivehook__ = echo

del echo
