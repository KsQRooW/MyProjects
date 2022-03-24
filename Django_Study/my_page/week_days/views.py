from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse

days = {"monday": "понедельник", "tuesday": "вторник", "wednesday": "среду", "thursday": "четверг", "friday": "пятницу",
        "saturday": "субботу", "sunday": "воскресенье"}


def get_info(request, day: str):
    # description = days.get(day, None)
    response = render_to_string('week_days/greeting.html')
    # if description:
    return HttpResponse(response)
    # return HttpResponseNotFound(f"Не существует дня недели {day}")

    # # альтернатива - использовать функцию render (по умолчанию импортирована в файле)
    # # from django.shortcuts import render - первый параметр получает всегда request

    # # return render(request, 'week_days/greeting.html')


def get_info_by_number(request, day: int):
    names_week_days = list(days)
    if 1 <= day <= len(names_week_days):
        redirect_url = reverse('todo_week_str', args=[names_week_days[day - 1]])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Неверный номер дня - {day}")


def get_info_by_kianu(request):
    kianu_info = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны'
    }
    return render(request, 'week_days/kianu.html', context=kianu_info)
