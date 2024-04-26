from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password']

    def save(self):
        s = super().save(commit=False)
        s.password = make_password(self.cleaned_data['password'])
        s.save()
        return s
    
class Login(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = '__all__'
        exclude = ['date_added']

class OTP_generation(forms.Form):
    Email = forms.EmailField()
        