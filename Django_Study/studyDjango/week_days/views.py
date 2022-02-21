from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def monday(request):
    return HttpResponse("Список дел запланированных на понедельник:")


def tuesday(request):
    return HttpResponse("Список дел запланированных на вторник:")
