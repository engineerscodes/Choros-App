from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from rest_framework import status

from .forms import vd_form
from .models import videoUpload, Marks
from datetime import date
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.views import APIView
from django.utils.encoding import force_text, force_bytes
from django.apps import apps
from django.http import JsonResponse
# from django.db.models import Q
from .serializers import  videoUploadSerializer,MarksSerializer,SubmitVideo
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
Mode = apps.get_model('Moderator', 'Mode')
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser


def PUTVD(request):


    if request.method =="GET":
        user = request.user
        if (user.is_authenticated == False):
            return redirect('/account/login')

        form = vd_form()
    return render(request, "upload.html", {"form": form})


def allVideos(request):
    if (request.user.is_authenticated == False):
        return redirect('/account/login')
    if request.method == 'GET':
        allmp4 = videoUpload.objects.all()

        # for i in allmp4 :
        # video=videoUpload.objects.get(pk=i.id)
        # video.url_64encoding=urlsafe_base64_encode(force_bytes(i.id))
        # print(video.url_64encoding)
        # video.save()

        return render(request, 'gallery.html', {'data': allmp4})



def getSingleVideo(request, uuid):
    if (request.user.is_authenticated == False):
        return redirect('/account/login')
    if request.method == 'GET':
        try:
            id = force_text(urlsafe_base64_decode(uuid))
            video = videoUpload.objects.get(pk=id)
        except Exception:
            video = None

        if video is not None:
            try:
                mode_team = Mode.objects.get(email=request.user.email)
            except Exception:
                mode_team = None

            if mode_team is not None and mode_team.username == request.user.username and mode_team.mode_active:
                current_video_marks = Marks.objects.filter(videoId=id)
                # print(current_video_marks,'###################################')
                return render(request, 'video.html', {'data': video, 'MODES': True, 'Marks': current_video_marks})
            elif request.user.is_staff:
                current_video_marks = Marks.objects.filter(videoId=id)
                return render(request, 'video.html', {'data': video, 'MODES': False, 'Marks': current_video_marks})
            else:
                return render(request, 'video.html', {'data': video, 'MODES': False})
        else:
            return redirect('/videos/')

    if request.method == 'POST':
        try:
            id_post = force_text(urlsafe_base64_decode(uuid))
            video_post = videoUpload.objects.get(pk=id_post)
        except Exception:
            video_post = None
        if request.POST['video_marks'] == '':
            return redirect(f'/videos/{uuid}')
        try :
            neg=int(request.POST['video_marks'])
            if neg<0:
                messages.info(request,"MARKS CANNOT BE LESS THAN ZERO")
                return redirect(f'/videos/{uuid}')
        except ValueError :
            messages.info(request, "NO STRING ALLOWED")
            return redirect(f'/videos/{uuid}')
        if video_post != None and request.POST['video_marks'] !='':
            try:
                check_marks = Marks.objects.get(videoId=id_post, moderator_email=request.user.email)
                #print(video_post.total_marks())

            except Exception:
                check_marks = None
            if check_marks is not None and neg>=0:
                #print(neg,'$$$$$$$$$$$$$$$$',check_marks.marks)
                video_post.Total_marks = int(video_post.Total_marks) +(int(-check_marks.marks) + neg)
                #print(video_post.total_marks(),"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",video_post.Total_marks)
                video_post.save()
                check_marks.marks = request.POST['video_marks']
                check_marks.date = date.today().strftime('%Y-%m-%d')
                check_marks.save()
                return redirect(f'/videos/{uuid}')
            if check_marks is None and neg>=0:
                video_post.Total_marks = int(video_post.Total_marks) + neg
                #print(video_post.total_marks(), "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                video_post.save()
                video_marks = Marks()

                video_marks.videoId = id_post
                video_marks.video_link = uuid
                video_marks.by_email = video_post.username

                video_marks.moderator_email = request.user.email
                video_marks.date = date.today().strftime('%Y-%m-%d')
                video_marks.marks = request.POST['video_marks']
                video_marks.verfiyed = True
                video_marks.save()
                return redirect(f'/videos/{uuid}')
        else:
            return redirect('/videos')


'''from moviepy.editor import *
clip = VideoFileClip("example.mp4")
clip=clip.resize(width=800)
clip.save_frame("thumbnail.jpg",t=0.10)'''


def homePage(request):
    if request.method == 'GET':
     if request.user.is_authenticated:
        videos = videoUpload.objects.all()
        return render(request, 'HomePage.html', {'videos': videos})
     else :
         return redirect('/account/login')


def Moderator(request):
    if (request.user.is_authenticated == False):
        return redirect('/account/login')
    if request.method == 'GET':

        try:
            mode_team = Mode.objects.get(email=request.user.email)
        except Exception:
            mode_team = None

        if mode_team is not None and mode_team.username == request.user.username and mode_team.mode_active:
            allmark_user = Marks.objects.filter(moderator_email=request.user.email)
            allmark_user_id = allmark_user.values_list('videoId')
                #return JsonResponse({"allmarks":allmark_user})
            # print(allmark_user_id,"######################################")
            # print(allmark_user)
            # print(type(allmark_user))
            left_out_video = videoUpload.objects.exclude(pk__in=allmark_user_id)
            # print(left_out_video,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

            return render(request, 'allmarks.html', {'marks': allmark_user, 'LeftOver': left_out_video})
        if request.user.is_staff:
            return redirect('/videos')
        else :
            return redirect('/')
        # return HttpResponse("MODERATIONS")






def GodMode(request) :
    if (request.user.is_authenticated == False):
        return redirect('/account/login')
    if request.method=='GET' and request.user.is_staff:
       Allvideo_mod=videoUpload.objects.order_by('Total_marks').reverse()

       return render(request,'getmarks.html',{'data':Allvideo_mod})
    if request.method =='GET':
        return redirect('/videos')


@api_view(['GET'])
def ajaxModeration(request):
    if request.method == 'GET':

        try:
            mode_team = Mode.objects.get(email=request.user.email)
        except Exception:
            mode_team = None

        if mode_team is not None and mode_team.username == request.user.username and mode_team.mode_active:
            allmark_user = Marks.objects.filter(moderator_email=request.user.email)
            allmark_user_id = allmark_user.values_list('videoId')
            if request.is_ajax():
              if request.GET['videos']=="verified" :
                cur_marked=MarksSerializer(allmark_user,many=True)
                return Response({"data": cur_marked.data})
              if  request.GET['videos']=="unseen":
                left_out_video = videoUpload.objects.exclude(pk__in=allmark_user_id)
                left_cur_marked =videoUploadSerializer(left_out_video,many=True)
                return Response({"data":left_cur_marked.data})
        else :
            return Response ({"data":"Acess DENIED LOL"})





class  ajaxsubmitVideo(APIView):
   parser_classes = [MultiPartParser, FormParser,FileUploadParser]

   def post(self, request, format=None):

       serializerss = SubmitVideo(data=request.data)
       #print(request.POST.get('captions'))

       if serializerss.is_valid():
           #print(serializerss.validated_data[''])

           form = vd_form(data=request.POST, files=request.FILES)
           if form.is_valid():
               new_form = form.save(commit=False)
               new_form.username =request.user.email
               new_form.date = date.today().strftime('%Y-%m-%d')
               new_form.save()
               video = videoUpload.objects.get(pk=new_form.id)
               video.url_64encoding = urlsafe_base64_encode(force_bytes(new_form.id))
               video.thumbnail = serializerss.validated_data['thumbnail']
               video.save()
           #serializerss.save(username=request.user.email,date= date.today().strftime('%Y-%m-%d'))
           #print(videoUpload.objects.filter(pk=serializerss))




           return Response("VIDEO SUMBITTED", status=status.HTTP_200_OK)
       else:
           return Response(serializerss.errors, status=status.HTTP_400_BAD_REQUEST)



