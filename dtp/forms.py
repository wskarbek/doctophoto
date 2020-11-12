from django import forms


class SignUpForm(forms.Form):
    email = forms.CharField(label='email', max_length=30)
    password = forms.CharField(label='pwd3')
    pow_password = forms.CharField(label='pwd4')
