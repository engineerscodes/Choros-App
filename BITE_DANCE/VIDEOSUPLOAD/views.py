from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import vd_form
from .models import videoUpload

def PUTVD(request):

    if request.method =='POST':
        form=vd_form(data=request.POST,files=request.FILES)
        if form.is_valid() :
            form.save()
            return HttpResponse("DONE UPLOADED ")
    else :
        form=vd_form()
    return render(request,"upload.html",{"form":form})

def allVideos(request):

     if request.method =='GET':
         allmp4=videoUpload.objects.all()
         return  render(request,'gallery.html',{'data':allmp4})