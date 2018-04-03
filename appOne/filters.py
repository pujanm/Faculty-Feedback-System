import django_filters
from django import forms
from .models import TeacherProfile


class TeacherProfileFilter(django_filters.FilterSet):
    fname = django_filters.CharFilter(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'fname'}))
    lname = django_filters.CharFilter(label='Last Name',widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lname'}))
    class Meta:
        model = TeacherProfile
        fields = ['fname', 'lname']
