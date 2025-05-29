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
        
class ForgetPasswordForm(forms.Form):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'emailclass', 'placeholder': 'Enter your email'}),
        label='Email'
    )
    otp = forms.CharField(
        max_length=6,
        required=False,  # initially not required
        widget=forms.TextInput(attrs={'class': 'otpclass', 'placeholder': 'Enter OTP'}),
        label='OTP'
    )

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'passwordclass', 'placeholder': 'Enter new password'}),
        label='New Password'    
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'passwordclass', 'placeholder': 'Confirm new password'}),
        label='Confirm Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
