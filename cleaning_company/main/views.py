from django.shortcuts import render
from .models import Clients, Orders

from django.conf import settings

# Данные о типах уборки
type_cleaning = [{"price:"},{},{}]

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def account(request):
    if request.method == 'POST' and 'login-app' in request.POST:
        user = request.POST['username']
        password = request.POST['password']
        if user in Clients.objects.all():
            settings.CURRENT_USER = Clients.objects.get(name=user)
            return render(request, 'account.html', )
    return render(request, 'account.html')


def services(request):
    if request.method == 'POST' and 'get-services' in request.POST:
        if isinstance(settings.CURRENT_USER, str):
            client = Clients()
            client.name = settings.CURRENT_USER
            client.


    return render(request, 'services.html')
