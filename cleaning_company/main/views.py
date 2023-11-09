from django.shortcuts import render
from .models import Clients, Orders, Services


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def account(request):
    return render(request, 'account.html')


def services(request):
    # services = Services()
    # print(services.objects.get())

    return render(request, 'services.html')
