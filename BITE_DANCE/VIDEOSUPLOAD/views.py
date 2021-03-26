from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import vd_form
def PUTVD(request):

    if request.method =='POST':
        form=vd_form(data=request.POST,files=request.FILES)
        if form.is_valid() :
            form.save()
            return HttpResponse("DONE UPLOADED ")
    else :
        form=vd_form()
    return render(request,"upload.html",{"form":form})