"""
创建汽车类car,具有类型type，速度speed等数据
	                 启动start，停止stop，行驶run等方法。
	  创建对象：
			宝马
		    比亚迪

"""
class Car:
    def __init__(self,type,speed):
        self.type = type
        self.speed = speed

    def start(self):
        print("启动啦")

    def stop(self):
        print("停止啦")

    def run(self):
        print("移动啊")

c01 = Car("宝马",180)
c01.start()
c01.run()
c01.stop()


c01 = Car("比亚迪",100)
c01.start()
c01.run()
c01.stop()