"""
    练习：改造MyRange --- yield 实现
         惰性查找
"""


# class MyRangeIterator:
#     def __init__(self, stop):
#         self.stop = stop
#         self.start = 0
#
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration()
#         temp = self.start
#         self.start += 1
#         return temp


# class MyRange:
#     def __init__(self, stop):
#         self.stop = stop
#
#     def __iter__(self):
#         start = 0
#         while start < self.stop:
#             yield start
#             start += 1

# for item in MyRange(5):
#     print(item)  # 0  1   2   3 4

# iter01 = my_range(5)
# while True:
#     try:
#         item = iter01.__next__()
#         print(item)
#     except :
#         break

def my_range(stop):
    start = 0
    while start < stop:
        yield start
        start += 1

g01 = my_range(5)
iter01 = g01.__iter__()
while True:
    try:
        iter01.__next__()
    except:
        break
print(g01)



# # 延迟(惰性)操作: 按需(当调用__next__方法时)计算
# for item in my_range(5):
#     print(item)  # 0  1   2   3 4












