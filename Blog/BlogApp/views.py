from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *
 
# Create your views here.
def index(request):
    return render(request, 'blogapp/index.html')


def user_signup(request):
    if request.method == 'GET':
        user_form = UserSignUpForm()
        # messages.add_message(request, messages.SUCCESS, 'CREATE A NEW USER')
        return render(request, 'blogapp/user_signup.html', {'user_form': user_form})
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        if user_form.is_valid():
            user_form.save()  # Now save the user
            
            # messages.add_message(request, messages.SUCCESS, 'User created successfully')
            return redirect('/login/')
        return render(request, 'blogapp/user_signup.html', {'user_form': user_form})
    
def user_login(request):
    if request.method == 'GET':
        user_form = UserSignInForm()
        # messages.add_message(request, messages.INFO, 'LOGIN TO YOUR ACCOUNT')
        return render(request, 'blogapp/user_login.html', {'user_form': user_form})
    if request.method == 'POST':
        user_form = UserSignInForm(request,request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Login successful')
                return redirect('/blogs/')
        # messages.add_message(request, messages.ERROR, 'Invalid username or password')
        return render(request, 'blogapp/view_blogs.html', {'user_form': user_form})
    
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        # messages.add_message(request, messages.SUCCESS, 'Logout successful')
        return redirect('/login/')
    return redirect('/login/')


@login_required  # Redirects to your login view if not authenticated
def create_blog(request):
    if request.method == 'GET':
        blog_form = BlogForm()
        # messages.add_message(request,messages.INFO,'CREATE A NEW BLOG')
        return render(request, 'blogapp/create_blog.html', {'blog_form': blog_form})
    elif request.method == 'POST':
        blog_form = BlogForm(request.POST,request.FILES)
        if blog_form.is_valid():
            blog= blog_form.save(commit=False)  # Don't save to the database yet
            blog.user = request.user
            blog.save()
            # messages.add_message(request, messages.SUCCESS, 'Blog created successfully')
            return redirect('/blogs/')
        messages.add_message(request, messages.ERROR, 'ERROR creating blog')
        return render(request, 'blogapp/create_blog.html', {'blog_form': blog_form})


@login_required
def view_blogs(request):
        blogs= Blog.objects.filter(user=request.user)
        # blogs = Blog.objects.all()
        return render(request, 'blogapp/view_blogs.html', {'blogs': blogs})
    
    
@login_required
def update_blog(request, id):
    blog = Blog.objects.filter(id=id).first()
    if not blog:
        # messages.add_message(request, messages.ERROR, 'Blog not found')
        return render(request, 'blogapp/view_blogs.html', {'blogs': Blog.objects.all()})
    if blog.user != request.user:
        # messages.add_message(request, messages.ERROR, 'You do not have permission to update this blog')
        return redirect('/blogs/')
    if request.method == 'GET':
        blog_form = BlogForm(instance=blog)
        # messages.add_message(request, messages.INFO, 'UPDATE YOUR BLOG')
        return render(request, 'blogapp/update_blog.html', {'blog_form': blog_form})
    elif request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES, instance=blog)
        if blog_form.is_valid():
            blog_form.save()
            # messages.add_message(request, messages.success, 'Blog updated successfully')
            return redirect('/blogs/')
        # messages.add_message(request, messages.ERROR, 'ERROR updating blog')
        return render(request, 'blogapp/update_blog.html', {'blog_form': blog_form})
    
@login_required
def delete_blog(request, id):
    blog = Blog.objects.filter(id=id).first()
    if blog.user != request.user:
        print("User does not match")
        # messages.add_message(request, messages.ERROR, 'Blog not found')
        return redirect('/blogs/')
    if request.method == 'GET':
        blog.delete()
        # messages.add_message(request, messages.success, 'Blog deleted successfully')
        return redirect('/blogs/')
    return render(request, 'blogapp/view_blogs.html', {'blog': blog})




