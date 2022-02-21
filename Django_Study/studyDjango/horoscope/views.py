from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def aries(request):
    return HttpResponse("Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")


def taurus(request):
    return HttpResponse("Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")
