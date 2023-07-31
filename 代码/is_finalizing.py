import sys

class Prophet:
    def __del__(self):
        #该类的实例因解释器关闭而被销毁。
        if sys.is_finalizing():
            print("I am dying with the world.")
        #该类的实例因其他原因被销毁。
        else:
            print("I am dying but the world goes on.")


