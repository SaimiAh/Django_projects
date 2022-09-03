from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is from the view.py file")

def help(request):
    helpdic = {'help_insert':'Help Page'}
    return render(request,'Task_app/help.html',context=helpdic)

def help(request):
    helpdic = {'help_insert':'Help Page'}
    return render(request,'Task_app/help.html',context=helpdic)