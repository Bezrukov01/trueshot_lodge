from django.shortcuts import render
from .models import Character, Specialization


def home(request):
    return render(request, 'home.html')


def character(request, name='BM'):
    args = {}
    hero = Specialization.objects.get(name=name)
    args.update({'character': hero})
    return render(request, 'character.html', args)
