from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

def PUTVD(request):
    if request.method == 'GET':
        return HttpResponse("COOL");