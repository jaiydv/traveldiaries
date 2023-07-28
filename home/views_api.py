from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from .helpers import *

class LoginView(APIView):
    
    
    def post(self,request):
        response={}
        response['status']=500
        response['message']='Something went Wrong'

        try:
            data=request.data

            if data.get('username') is None:
                response['message']='key username is not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message']='key password is not found'
                raise Exception('key password not found')
            
            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user is None:
                response['message']="invalid username"
                raise Exception('invalid username not found')
            print("yha tak")
            if not Profile.objects.filter(user=check_user).first().is_verified:
                response['message']="Your profile is not verified"
                raise Exception('profile not verified')

            user_obj=authenticate(username=data.get('username'),password=data.get('password'))
            if user_obj:
                login(request,user_obj)
                response['status']=200
                response['message']="welcome"
            else:
                response['message']='invalid password'
                raise Exception('invalid password')
        except Exception as e:
            print(e)
        
        return Response(response)

LoginView=LoginView.as_view()
    
class RegisterView(APIView):

    def post(self,request):
        response={}
        response['status']=500
        response['message']='Something went Wrong'

        try:
            data=request.data

            if data.get('username') is None:
                response['message']='key username is not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message']='key password is not found'
                raise Exception('key password not found')
            
            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user:
                response['message']="username already taken"
                raise Exception('username already taken')

            user_obj = User.objects.create(username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            token=generate_random_string(20)
            email=data.get('username')
            Profile.objects.create(user=user_obj,is_verified=True,token=token)

           
            # send_mail_to_user(token,email)

            response['message']="user created suuccessfully"
            response['status']=200
            response['token']=token
            
        except Exception as e:
            print(e)
        
        return Response(response)

RegisterView=RegisterView.as_view()