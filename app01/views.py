from django.shortcuts import render, HttpResponse


# Create your views here.
# "return render(request, "首页.html")"返回一个html文件

def home(request):
    return render(request, "首页.html")


def introduction(request):
    return render(request, "D1-1409简介.html")
