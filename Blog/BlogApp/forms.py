from django import forms
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']
        widgets = {
            'username': forms.EmailInput(attrs={'class':'usernameclass', 'placeholder':'enter your email'}),}
        
        
class UserSignInForm(AuthenticationForm):
    class Meta:
        model: User
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields = ['title','content','image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'titltclass', 'placeholder':'enter your blog title'}),
            'content': forms.Textarea(attrs={'class':'content', 'placeholder':'enter your blog details','rows':10,'cols':50}),
            'image': forms.ClearableFileInput(attrs={'class':'imageclass'})

        }