from django import forms
from .models import User


# 创建class
class RegisterForm(forms.Form):
    # 一个属性对应大表单中就是一个控件
    # forms.BooleanField()  # <input type="checkbox"></input>
    # forms.CharField()  # <input type="text"></input>
    # forms.ChoiceField()  # <select></select>
    # forms.DateTimeField()  # <input type="date"></input>
    # forms.DecimalField()  # <input type="number"></input>
    # forms.EmailField()  # <input type="email"></input>

    uname = forms.CharField(max_length=50, label='用户名')
    upwd = forms.CharField(max_length=50, label='密码', widget=forms.PasswordInput)
    uemail = forms.EmailField(label='邮箱', widget=forms.EmailInput)
    uphone = forms.CharField(max_length=11, label='电话')
    isActive = forms.BooleanField(label='状态', required=False)


class LoginForm(forms.ModelForm):
    class Meta:
        model = User  # 指定关联的实体类
        # fields = '__all__'  # 指定要从models模型获取那些字段做控件(这里获取全部)
        fields = ['uphone', 'upwd']
        labels = {
            'uphone': '登陆账号',
            'upwd': '登陆密码',
        }
        widgets = {
            'uphone': forms.TextInput(
                attrs={'placeholder': '请输入手机号/邮箱/账号'}
            ),
            'upwd': forms.PasswordInput(
                attrs={
                    'placeholder': '请输入密码',
                    'class': 'from-control'
                }
            ),
        }
