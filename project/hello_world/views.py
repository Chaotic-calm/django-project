from django.shortcuts import render,HttpResponse

def show(request):
    return HttpResponse('hello world')
