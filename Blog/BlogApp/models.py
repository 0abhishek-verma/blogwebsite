from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blogs',null=True, blank=True)
    # ForeignKey to User model, allowing each blog to be associated with a user
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    

    def __str__(self):
        return self.title
    
class Forget_Password(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='forget_password',null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    
    
    def __str__(self):
        return f"Forget Password for {self.user.username if self.user else 'Unknown User'}"