from django.apps import apps
from django.shortcuts import render, redirect

from .forms import vd_form

# from django.db.models import Q
Mode = apps.get_model('Moderator', 'Mode')


def PUTVD(request):


    if request.method =="GET":
        user = request.user
        if (user.is_authenticated == False):
            return redirect('/account/login')

        form = vd_form()
    return render(request, "upload.html", {"form": form})
#just for refernces

'''if request.method == 'POST':
           user = request.user
           # request.POST.get('THUMBNAILIMAGE',False)
           if (user.is_authenticated):
               form = vd_form(data=request.POST, files=request.FILES)
               # print(user.is_authenticated)
               if form.is_valid():
                   new_form = form.save(commit=False)
                   new_form.username = user.email
                   new_form.date = date.today().strftime('%Y-%m-%d')
                   new_form.save()
                   video = videoUpload.objects.get(pk=new_form.id)
                   video.url_64encoding = urlsafe_base64_encode(force_bytes(new_form.id))
                   video.thumbnail = request.POST['thumbIMG']
                   video.save()


   '''

def ajaxsubmitVideo2(request):

    if request.method=='GET':

        form = vd_form()
        return render(request,'testgetvdieo.html',{"form": form})
    if request.method=='POST':
        form = vd_form()
        return render(request,'testgetvdieo.html',{"form": form})

        #return HttpResponse("DONE UPLOADED ")
           #if (user.is_authenticated == False):
              # return redirect('/account/login')