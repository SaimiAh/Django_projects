from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    mydic = {'insert_me': "Hi this Is my page!"}
    return render(request,'Second_app/index.html',context=mydic)

# Create your views here.
