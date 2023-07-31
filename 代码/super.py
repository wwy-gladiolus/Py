class A:
    def who(self):
        return 'A'

class B(A):
    def who(self):
        return 'B'

    def parent(self):
        print ('My parent is ' + super().who())

class C(B):
    def who(self):
        return 'C'

class D(A):
    def who(self):
        return 'D'

class E(C, D):
    def who(self):
        return 'E'
