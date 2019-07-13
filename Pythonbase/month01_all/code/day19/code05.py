"""
    生成器
"""


"""生成器本质
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


class MyGenerator:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
         return MyRangeIterator(self.stop)

for item in MyGenerator(5):
    print(item)
    
g01 = MyGenerator(5)
iter01 = g01.__iter__()
while True:
    try:
        print(iter01.__next__())
    except:
        break
"""

def my_range(stop):
    start = 0
    while start < stop:
        yield start
        start += 1

for item in my_range(5):
    print(item)  # 0  1   2   3 4













