from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    mydic = {'insert_me': "Hi this Is my page!"}
    return render(request,'index.html',context=mydic)

# Create your views here.
