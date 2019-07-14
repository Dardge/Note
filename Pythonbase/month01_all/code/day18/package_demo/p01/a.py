print("a模块")

import sys
print(sys.path)

from p01.p02 import b
b.fun02()



def fun01():
    print("a -- fun01")
