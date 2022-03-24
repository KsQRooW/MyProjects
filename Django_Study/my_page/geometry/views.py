from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def get_rectangle_area(request, width, height):
    # return HttpResponse(f"Площадь прямоугольника равна {width * height}")
    return render(request, 'geometry/rectangle.html')


def get_circle_area(request, radius):
    # return HttpResponse(f"Площадь круга равна {3.14 * radius * radius}")
    return render(request, 'geometry/circle.html')


def get_square_area(request, width):
    # return HttpResponse(f"Площадь квадрата равна {width * width}")
    return render(request, 'geometry/square.html')


def redirect_function(request, *args, **kwargs):
    redirect_url = reverse(request.path.split('/')[2].split('_')[1], args=request.path.split('/')[3:])
    return HttpResponseRedirect(redirect_url)
    # return HttpResponseRedirect(f"/calculate_geometry/{request.path.split('/')[2].split('_')[1]}/{'/'.join(request.path.split('/')[3:])}")
