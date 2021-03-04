from django.shortcuts import render,redirect
from django.contrib.auth.models import  auth,User
from django.contrib import messages
from .Token_Gen import Token_generator
from django.core.mail import send_mail

from django.http import HttpResponse

# Create your views here.

def login(request) :

     if request.method =='GET':
          return render(request,'login.html')
     if request.method =='POST' :
          username =request.POST['user-name']
          Password =request.POST['passwordcnf']

          User=auth.authenticate(username=username,password=Password)

          if User is not None :
               if User.is_active ==False :
                   return HttpResponse("<h1> Verfiy Mail </h1>")
               else :
                   auth.login(request,User)
                   return HttpResponse("<h1> logged in </h1>")

          else :
               messages.info(request, "Invalid userNAME  or Password ")
               return redirect('/account/login')


def reg(request) :

     if request.method =='GET' :

          return render(request,'reg.html')
     if request.method =='POST' :

          userName=request.POST['names']
          password =request.POST['password_cfn']
          email =request.POST['emails']

          if User.objects.filter(username=userName).exists() :
                 messages.info(request," UserName is not Available")
                 return redirect('/account/reg/')
          else :
                user=User.objects.create_user(username=userName,password=password,email=email)
                user.is_active=False
                user.save()
                # PasswordResetTokenGenerator use it to verfiy and create token also
                Useract_token = Token_generator()
                Useract_token.make_token(user)
                print(Useract_token)
                send_mail(
                    'THANKS FOR REG',
                    f'HELLO ITS DJANGO MESSAGE TEST With Toeken {Useract_token}',
                    'naveennoob95@gmail.com',
                    [email],
                    fail_silently=False,
                )

                messages.info(request, "DONE ")
                return redirect('/account/reg/')

