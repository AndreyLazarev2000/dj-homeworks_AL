import os
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    context = {'pages': pages}
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().strftime('%H:%M:%S %d.%m.%Y')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir(settings.BASE_DIR)
    files_str = '<br>'.join(files)
    return HttpResponse(f'<h3>Содержимое рабочей директории:</h3>{files_str}')