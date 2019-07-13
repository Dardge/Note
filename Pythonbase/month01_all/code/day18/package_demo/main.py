
# import 包名.模块名
# import p01.a
# p01.a.fun01()


# import 包名.子包名.模块名
# import p01.p02.b
# p01.p02.b.fun02()

# from 包 import 模块
from p01 import a
a.fun01()


# from 包.子包.模块 import 成员
# from p01.p02.b import fun02
# fun02()

# from 包 import  *
# __all__ = ["模块名"]

# from p01.p02 import  *
# b.fun02()
# c.fun03()
