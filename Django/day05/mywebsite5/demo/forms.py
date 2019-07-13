from django import forms

LEVEL_CHOICE = (
    ('1', '好评'),
    ('2', '中评'),
    ('3', '差评')
)


# 创建class
class RemarkForm(forms.Form):
    # 一个属性对应大表单中就是一个控件
    # forms.BooleanField()  # <input type="checkbox"></input>
    # forms.CharField()  # <input type="text"></input>
    # forms.ChoiceField()  # <select></select>
    # forms.DateTimeField()  # <input type="date"></input>
    # forms.DecimalField()  # <input type="number"></input>
    # forms.EmailField()  # <input type="email"></input>
    # 1.评论标题
    # 2.email
    # 3.内容
    # 4.级别
    # 5.是否保存
    title = forms.CharField(max_length=10, label='评论标题')  # label 控件前面的文本
    email = forms.EmailField(label='电子邮箱')
    # 单独的input无法满足需求，需要添加控件 widget 将当前的控件变为多行文本域textarea
    content = forms.CharField(label='评论内容', widget=forms.Textarea)  # widget 将当前的控件便为多行文本域textarea
    # ChoiceField需要提供选项
    level = forms.ChoiceField(label='评论级别', choices=LEVEL_CHOICE)
    isSaved = forms.BooleanField(label='是否保存', required=False)  # 默认未选中(required是否为必填项)
