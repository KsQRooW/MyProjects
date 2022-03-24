from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

zodiac = {
    'aries':
        {'description': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
         'types': 'fire',
         'day_start': 21,
         'month_start': 3,
         'day_finish': 20,
         'month_finish': 4
         },
    'taurus':
        {'description': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
         'types': 'earth',
         'day_start': 21,
         'month_start': 4,
         'day_finish': 21,
         'month_finish': 5
         },
    'gemini':
        {'description': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
         'types': 'air',
         'day_start': 22,
         'month_start': 5,
         'day_finish': 21,
         'month_finish': 6
         },
    'cancer':
        {'description': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
         'types': 'water',
         'day_start': 22,
         'month_start': 6,
         'day_finish': 22,
         'month_finish': 7
         },
    'leo':
        {'description': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
         'types': 'fire',
         'day_start': 23,
         'month_start': 7,
         'day_finish': 21,
         'month_finish': 8
         },
    'virgo':
        {'description': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
         'types': 'earth',
         'day_start': 22,
         'month_start': 8,
         'day_finish': 23,
         'month_finish': 9
         },
    'libra':
        {'description': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
         'types': 'air',
         'day_start': 24,
         'month_start': 9,
         'day_finish': 23,
         'month_finish': 10
         },
    'scorpio':
        {'description': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
         'types': 'water',
         'day_start': 24,
         'month_start': 10,
         'day_finish': 22,
         'month_finish': 11
         },
    'sagittarius':
        {'description': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
         'types': 'fire',
         'day_start': 23,
         'month_start': 11,
         'day_finish': 22,
         'month_finish': 12
         },
    'capricorn':
        {'description': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
         'types': 'earth',
         'day_start': 23,
         'month_start': 12,
         'day_finish': 20,
         'month_finish': 1
         },
    'aquarius':
        {'description': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
         'types': 'air',
         'day_start': 21,
         'month_start': 1,
         'day_finish': 19,
         'month_finish': 2
         },
    'pisces':
        {'description': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
         'types': 'water',
         'day_start': 20,
         'month_start': 2,
         'day_finish': 20,
         'month_finish': 3
         }
}


def index(request):
    names_zodiac = list(zodiac)
    # f'<li><a href={redirect_url}>{name.title()}</a></li>'
    context = {
        'zodiacs': names_zodiac
    }
    return render(request, 'horoscope/index.html', context=context)


def types(request):
    element_types = set(map(lambda x: x['types'], zodiac.values()))
    li_elements = ''
    for i in element_types:
        redirect_url = reverse('horoscope_type', args=[i])
        li_elements += f'<li><a href={redirect_url}>{i.title()}</a></li>'
    responce = f'''
        <ul>
            {li_elements}
        </ul>
        '''
    return HttpResponse(responce)


def get_info(request, sign_zodiac: str):
    description = zodiac.get(sign_zodiac, sign_zodiac)
    context = {
        'description': description,
        'sign_zodiac': sign_zodiac
    }
    return render(request, 'horoscope/info_zodiac.html', context=context)


def get_info_by_number(request, sign_zodiac: int):
    names_zodiac = list(zodiac)
    if 0 < sign_zodiac < len(names_zodiac):
        redirect_url = reverse('horoscope-name', args=[names_zodiac[sign_zodiac - 1]])
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f"Не существует знака зодиака с номером {sign_zodiac}. Их всего 12.")


def get_info_by_type(request, element_type):
    signs_with_element_type = list(zodiac)
    li_elements = ''
    for i in signs_with_element_type:
        if zodiac[i]['types'] == element_type:
            redirect_url = reverse('horoscope-name', args=[i])
            li_elements += f'<li><a href={redirect_url}>{i.title()}</a></li>'
    responce = f'''
            <ul>
                {li_elements}
            </ul>
            '''
    return HttpResponse(responce)


def get_info_by_date(request, month, day):
    names_zodiac = list(zodiac)
    for name in names_zodiac:
        if zodiac[name]['month_start'] == month:
            if zodiac[name]['day_finish'] >= day:
                redirect_url = reverse('horoscope-name', args=[name])
                return HttpResponseRedirect(redirect_url)
        elif zodiac[name]['month_finish'] == month:
            if zodiac[name]['day_finish'] >= day:
                redirect_url = reverse('horoscope-name', args=[name])
                return HttpResponseRedirect(redirect_url)
