from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def padre_template(request):
    today = datetime.today()
    context = {
        'name':'Sergio',
        'last_name':'Locura',
        'edad': '55',
        'today': today
    }
    return render(request, 'template_2.html', context=context)

def madre_template(request):
    today = datetime.today()
    context = {
        'name':'Silvana',
        'last_name':'Menez',
        'edad': '50',
        'today': today
    }
    return render(request, 'template_3.html', context=context)

def hijo_template(request):
    today = datetime.today()
    context = {
        'name':'Ignacio',
        'last_name':'Farruggia',
        'edad': '20',
        'today': today
    }
    return render(request, 'template_4.html', context=context)