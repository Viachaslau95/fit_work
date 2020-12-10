from django.shortcuts import render


def register(request):
    return render(request,'main/register.html')


def login(request):
    return render(request, 'main/login.html')


def index(request):
    data = {
        'title': 'Home page',
        'values': ['some', 'hello', ]
    }
    return render(request, 'main/index.html', data)


def workouts(request):
    return render(request, 'main/workouts.html')

