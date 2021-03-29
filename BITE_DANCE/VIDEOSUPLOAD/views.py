from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import vd_form
from .models import videoUpload
from datetime import date
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.models import  auth,User
from django.template.loader import  render_to_string
from django.utils.encoding import  force_text,force_bytes,  DjangoUnicodeDecodeError
from django.contrib.sites.shortcuts import get_current_site

def PUTVD(request):

    if request.method =='POST':
        user = request.user
        if(user.is_authenticated) :
              form=vd_form(data=request.POST,files=request.FILES)
              print(user.is_authenticated)
              if form.is_valid():
                  new_form = form.save(commit=False)
                  new_form.username = user
                  new_form.date = date.today().strftime('%Y-%m-%d')
                  new_form.save()
                  video = videoUpload.objects.get(pk=new_form.id)
                  video.url_64encoding=urlsafe_base64_encode(force_bytes(new_form.id))
                  video.save()

                  return HttpResponse("DONE UPLOADED ")
        if(user.is_authenticated==False) :

            return redirect('/account/login')



    else :
        user = request.user
        if (user.is_authenticated == False):
            return redirect('/account/login')

        form=vd_form()
    return render(request,"upload.html",{"form":form})

def allVideos(request):

     if request.method =='GET':
         allmp4=videoUpload.objects.all()

         #for i in allmp4 :
             #video=videoUpload.objects.get(pk=i.id)
             # video.url_64encoding=urlsafe_base64_encode(force_bytes(i.id))
             # print(video.url_64encoding)
             # video.save()


         return  render(request,'gallery.html',{'data':allmp4})

def getSingleVideo(request,uuid):
    id=force_text(urlsafe_base64_decode(uuid))

    video=videoUpload.objects.get(pk=id)
    return render(request,'video.html',{'data':video})


