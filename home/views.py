from django.shortcuts import redirect, render
from django.contrib.auth import logout


# Create your views here.
from .form import *
def home(request):
    context={'blogs':BlogModel.objects.all()}
    return render(request,"home.html",context=context)

def login_view(request):
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def see_blog(request):
    context={}
    try:
        blog_obj=BlogModel.objects.filter(user=request.user)
        context['blog_objs']=blog_obj
    except Exception as e:
        print(e)

    return render(request,'see_blog.html',context)

def blog_update(request,slug):
    context={}

    try:
        blog_obj=BlogModel.objects.get(slug=slug)
        if blog_obj.user!=request.user:
            return redirect("/")
        
        initial_dict={'content':blog_obj.content}
        form=BlogForm(initial=initial_dict)
        
        if request.method=='POST':
            print("hi")
            form=BlogForm(request.POST)
            image=request.FILES.get('image','')
            title=request.POST.get('title')
            user=request.user
            # print(image)
            if form.is_valid():
                print("valid")
                content=form.cleaned_data['content']
            print("title")
            blog_obj = BlogModel.objects.create(user=user, title=title,content=content, image=image
            )
            print("blog object",blog_obj)


        context['blog_obj']=blog_obj
        context['form']=form
        
    except Exception as e:
        print(e)
    return render(request,"blog_update.html",context=context)

def blog_delete(request,id):
    try:
        blog_obj=BlogModel.objects.get(id=id)
        if blog_obj.user==request.user:
            blog_obj.delete()
        
    except Exception as e:
        print(e)
    return redirect('/see_blog')

def blog_detail(request,slug):
    context={}
    try:
        blog_obj=BlogModel.objects.filter(slug=slug).first()
        context['blog_obj']=blog_obj
    except Exception as e:
        print(e)
    return render(request,'blog_detail.html',context=context)

def addblog_view(request):
    context = {'form' : BlogForm}
    try:
        if request.method=='POST':
            print("hi")
            form=BlogForm(request.POST)
            image=request.FILES.get('image','')
            title=request.POST.get('title')
            user=request.user
            # print(image)
            if form.is_valid():
                print("valid")
                content=form.cleaned_data['content']
            print("title")
            blog_obj = BlogModel.objects.create(user=user, title=title,content=content, image=image
            )
            print("blog object",blog_obj)
            return redirect('/addblog')
    except Exception as e:
        print(e)
    return render(request,"addblog.html",context)


def register_view(request):
    return render(request,"register.html")


def verify(request,token):
    try:
        profile_obj=Profile.objects.filter(token=token)

        if profile_obj:
            profile_obj.is_verified=True
            profile_obj.save()
        return redirect('/login')
    except Exception as e:
        print("e")
    return redirect("/login")