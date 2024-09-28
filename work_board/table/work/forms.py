from django import forms
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from .models import Profile, Announcement

#authentication user
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#registration user
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email',]

    #Compare password
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already registered.')
        return data

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id) \
            .filter(email=data)
        if qs.exists():
            raise forms.ValidationError(' Email already in use.')
        return data

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'city', 'country',
                  'description', 'experience', 'category']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['category', 'title', 'price',
                  'country', 'city', 'description',
                  'experience', 'company', 'address', 'tags']
