from django import forms
from .models import Member
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(error_messages={
        'required':'아이디를 입력하세요!'
    },max_length=100, label="Username")
    password = forms.CharField(error_messages={
        'required':'비밀번호를 입력하세요!'
    },widget=forms.PasswordInput, max_length=100, label="Password")
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                member = Member.objects.get(username=username)
            except Member.DoesNotExist:
                self.add_error('username', '아이디가 없습니다!')
                return

        if not check_password(password, member.password):
            self.add_error('password', '비밀번호가 다릅니다!')
        else:
            self.user_id = member.id