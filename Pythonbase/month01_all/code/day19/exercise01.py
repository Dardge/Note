"""
    练习：参照下列代码，自定义MyRange类，实现以下效果。
"""


# for item in range(5):
#     print(item)


class MyRangeIterator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 0

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration()
        temp = self.start
        self.start += 1
        return temp


class MyRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return MyRangeIterator(self.stop)


for item in MyRange(5):
    print(item)  # 0  1   2   3 4

# iter01 = MyRange(5).__iter__()
# while True:
#     try:
#         item = iter01.__next__()
#         print(item)
#     except:
#         break
