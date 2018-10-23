from django.http import HttpResponse
def hello1(request):
   return HttpResponse("登录页面!！！！！！！test")
#直接输出到网页
from django.shortcuts import render
def hello(request):
    return render(request,'hello.html')
def login(request):
    return render(request,'loginwindow.html')
def ccs(request):
    return render(request,'fileccs.html')
