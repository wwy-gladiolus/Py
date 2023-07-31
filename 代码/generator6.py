import random

def gen5():
    try:
        while True:
            n = random.random()
            yield n
    except Exception:
        print("Stop generates random numbers.")
        return 0
