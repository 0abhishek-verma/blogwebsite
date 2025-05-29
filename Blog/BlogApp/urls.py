from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('create/', create_blog, name='create_blog'),
    path('blogs/', view_blogs, name='view_blogs'),
    path('update/<int:id>/', update_blog, name='update_blog'),
    path('delete/<int:id>/',delete_blog, name='delete_blog'),
    path('signup/', user_signup, name='user_signup'),
    path('login/', user_login, name='user_login'),
    path('forget-password/', forget_password, name='forget_password'),
    path('reset-password/', reset_password, name='reset_password'),    
    path('logout/', user_logout, name='user_logout'),
]
