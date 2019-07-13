"""
    对列表常用操作的模块
    微软 Linq 框架
"""
class ListHelper:
    """
        列表助手类:定义对列表的通用操作
    """
    @staticmethod
    def find_all(list_target, func_condition):
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(list_target,func_condition):
        for item in list_target:
            # if item.age < 30:
            if func_condition(item):
                return item

    @staticmethod
    def count(list_target,func_condition):
        int_count = 0
        for item in list_target:
            if func_condition(item):
                int_count += 1
        return int_count

    # def condition01(item):
    #     return item.score

    # def condition01(item):
    #     return item.age

    @staticmethod
    def get_max(list_target, func_condition):
        value_max = list_target[0]
        for i in range(1, len(list_target)):
            # if value_max.score <  list_stu[i].score:
            if func_condition(value_max)<func_condition(list_target[i]):
                value_max = list_target[i]
        return value_max

    @staticmethod
    def sum(list_target,func_condition):
        value_sum = 0
        for item in list_target:
            # value_sum += item.age
            value_sum += func_condition(item)
        return value_sum

    @staticmethod
    def select(list_stu,func_condition):
        for item in list_stu:
            # yield item.score
            yield func_condition(item)

    @staticmethod
    def order_by(list_target,func_condition):
        """
            对象列表，进行升序排列。
        :param list_target: 对象列表
        :param func_condition: 排序条件
        """
        for r in range(len(list_target) - 1):
            for c in range(r+1,len(list_target)):
                # if list_target[r].score > list_target[c].score:
                if func_condition(list_target[r]) > func_condition(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]








