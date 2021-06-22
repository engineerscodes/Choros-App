from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User, Group
from django.contrib import messages
from django.views import View
import re

from .Token_Gen import Token_generator
from django.core.mail import send_mail

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

from django.http import HttpResponse

from django.template.loader import  render_to_string

from django.utils.encoding import  force_text,force_bytes,  DjangoUnicodeDecodeError

from django.contrib.sites.shortcuts import get_current_site


import threading
import  time


class THREADEMAIL(threading.Thread):
    def __init__(self, message, email):
        self.message = message
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
            send_mail(
                'THANKS FOR REG',
                self.message,
                'naveennoob95@gmail.com',
                [self.email],
                fail_silently=False,

            )


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
                   return redirect('/')

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

          if re.search('^[a-zA-z]+\.[0-9a-zA-Z]+@vitap\.ac\.in$',email) is  None :
              #print(re.search('^[a-zA-z]+\.[0-9a-zA-Z]+@vitap\.ac\.in$',email),"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
              messages.info(request, "USE VITAP MAIL ONLY ")
              return redirect('/account/reg/')


          if User.objects.filter(username=userName).exists():
                 messages.info(request," UserName is not Available")
                 return redirect('/account/reg/')
          if  User.objects.filter(email=email).exists() :
              messages.info(request, " MAIL IS ALREADY REG")
              return redirect('/account/reg/')

          if re.search('^[a-zA-z]+\.[0-9a-zA-Z]+@vitap\.ac\.in$',email) is not  None  and User.objects.filter(username=userName).exists() ==False:

                user=User.objects.create_user(username=userName,password=password,email=email)
                user.is_active=False
                user.save()
                group = Group.objects.get(name='members')
                user.groups.add(group)
                # PasswordResetTokenGenerator use it to verfiy and create token also
                Useract_token = Token_generator()



                message=render_to_string('activate.html',
                {
                       'user':user,
                       'domain':get_current_site(request),
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                         'TOKEN': Useract_token.make_token(user)


                }
                )
                ''' send_mail(
                                   'THANKS FOR REG',
                                   message,
                                   'naveennoob95@gmail.com',
                                   [email],
                                   fail_silently=False,
                )'''

                THREADEMAIL(message,email).start()



                messages.info(request, " plz verfiy your email ")
                return redirect('/account/reg/')









def AUTHUSERNAME(request,uidb64,token):

     try:
          uid=force_text(urlsafe_base64_decode(uidb64))
          user=User.objects.get(pk=uid)
     except Exception as identifier :
         user=None
     Useract_token = Token_generator()
     if user is not None and Useract_token.check_token(user,token):
         user.is_active = True
         user.save()

         messages.info(request,"VALIDATED USER PLZ LOGIN ")

         return  redirect('/account/login')

     return render(request,'auth_failed.html',status=401)


def logout(request):

    auth.logout(request)

    return redirect('/account/login')
