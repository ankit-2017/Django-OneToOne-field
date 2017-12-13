from django import forms
from .models import *


class useremp(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
                               max_length=50, required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
                                 max_length=30, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
                                max_length=30, required=False)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email address'}),
        max_length=50,
        required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ]


class emp(forms.ModelForm):
    department = forms.CharField(max_length=250)
    image = forms.FileField()

    class Meta:
        model = Emp
        fields = ['department','image']