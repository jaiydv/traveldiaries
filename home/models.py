from typing import Iterable, Optional
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_verified =models.BooleanField(default=False)
    token=models.CharField(max_length=100)

    


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000,null=True,blank=True)
    image = models.ImageField(upload_to="blog")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        from .helpers import generate_slug
        self.slug=generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)
