from django import forms


class ChangeForm(forms.Form):
    '''登录验证表单'''

    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


