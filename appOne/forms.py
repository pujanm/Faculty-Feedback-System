from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, TeacherProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name')

    class Meta():
        model = UserProfile
        fields = ('fname', 'lname')


class TeacherProfileForm(forms.ModelForm):
    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name')

    class Meta():
        model = TeacherProfile
        fields = ('fname', 'lname')
