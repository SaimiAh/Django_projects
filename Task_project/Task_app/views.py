from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello I am in views")

def help(request):
    helpdic = {'help_insert':'Help Page'}
    return render(request,'Task_app/help.html',context=helpdic)