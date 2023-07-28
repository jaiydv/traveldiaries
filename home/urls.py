

from django.urls import path,include
from .views import *

urlpatterns = [
    path('api/',include('home.urls_api')),
    path('',home,name="home"),
    
    path('login',login_view,name="login_view"),
    path('featured',featured,name="featured"),
    path('logout',logout_view,name="logout_view"),
    path('register', register_view ,name="register_view"),
    path('addblog',addblog_view,name="addblog_view"),
    path('blog_detail/<slug>',blog_detail,name="blog_detail"),
    path('see_blog',see_blog,name="see_blog"),
    path('blog_update/<slug>',blog_update,name="blog_update"),
    path('blog_delete/<id>',blog_delete,name="blog_delete"),
    path('verify/<token>',verify,name="verify")
]
