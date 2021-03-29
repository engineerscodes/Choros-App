from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import vd_form
from .models import videoUpload
from datetime import date

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
         return  render(request,'gallery.html',{'data':allmp4})