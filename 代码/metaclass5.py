class A():
    #@classmethod
    def __init_subclass__(cls):
        raise Exception("class A cannot be used as a base class!")

class B(A):
    pass
