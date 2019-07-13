"""
    经理：[曹操,刘备,孙权]。 技术员：[曹操,刘备,张飞,关羽]。
    使用两个列表分别存储经理与技术员。
    使用集合计算：
    1. 既是经理也是技术员的有谁？
    2. 是经理，但不是技术员都有谁？
    3. 是技术员，但不是经理都有谁？
    4. 张飞是经理吗？
    5. 身兼一职的都有谁？
    6. 经理和技术员共有几个人？
"""
list_manager = ["曹操","刘备","孙权"]
list_techs = ["曹操","刘备","张飞","关羽"]

set_manager = frozenset(list_manager)
set_techs = frozenset(list_techs)

print("即是经理也是技术员的有:",set_manager & set_techs)
print("是经理，但不是技术员都有:",set_manager - set_techs)
print("是技术员，但不是经理都有:",set_techs -set_manager )
print("张飞是经理吗？",  "张飞" in set_manager)
print("身兼一职的都有谁？",set_manager ^ set_techs)
print("经理和技术员共有几个人",len(set_manager | set_techs))