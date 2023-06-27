from django.http import HttpResponse
from django.shortcuts import render
from datetime import time

def helloview(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my first project')

def now_date(request):
    datetime = time()
    if request.method == 'GET':
        return HttpResponse(datetime)


def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby, user')