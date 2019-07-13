"""
    异常处理
"""


# 分苹果
def div_apple(apple_cout):
    person_count = int(input("请输入人数："))  # ValueError
    result = apple_cout / person_count  # ZeroDivisionError
    print("每人分了%d个苹果" % result)


# 尝试执行，可能出错的代码。
# try:
#     div_apple(10)
# # 定义出错后的业务逻辑
# except Exception as e:
#     print("错误啦:", e)


# 针对不同错误，做出相应处理。
# try:
#     div_apple(10)
#
# except ValueError:
#     print("输入有误")
# except ZeroDivisionError:
#     print("不能没人分苹果")

# try:
#     div_apple(10)
# except ValueError:
#     print("输入有误")
# except ZeroDivisionError:
#     print("不能没人分苹果")
# else:# 如果没有发生异常，执行else中的语句
#     print("苹果分配成功")
# finally:
#     print("无论是否发生异常，一定可以执行的代码")
#
# print("后续逻辑")

def fun01():
    try:
        div_apple(10)
    except Exception:
        print("fun01有错误")


list01 = [1]
print(list01[2])


try:
    fun01()
except Exception:
    print("有错误")

print("后续逻辑")









