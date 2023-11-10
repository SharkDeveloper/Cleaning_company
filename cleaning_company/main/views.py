from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Clients, Orders
from datetime import date
from django.conf import settings

# Данные о типах уборки
type_cleaning = [{"name": "suface cleaning", "price": 55.95}, {"name": "basic cleaning", "price": 85.45},
                 {"name": "spring-cleaning", "price": 113.95}]


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def account(request):
    if not isinstance(settings.CURRENT_USER, str):
        contex = {
                "current-user":settings.CURRENT_USER
            }
        return render(request, 'account.html', context=contex )
    if request.method == 'POST' and 'login-app' in request.POST:
        
        user = request.POST['login']
        password = request.POST['password']
        if Clients.objects.filter(login=user, password=password).first():
            settings.CURRENT_USER = Clients.objects.filter(name=user, password=password).first()
            contex = {
                "current-user":settings.CURRENT_USER
            }
            return render(request, 'account.html', context=contex )
    if request.method == 'POST' and 'reg-app' in request.POST:
        client = Clients()
        client.login = request.POST["login"]
        client.email = request.POST["email"]
        client.phone = request.POST["phone number"]
        client.password = request.POST["password"]
        client.name = request.POST["username"]
        client.save()
        
    return render(request, 'auth.html')


def services(request):
    if request.method == 'POST' and 'get-services' in request.POST:
        order = Orders()
        order.author = settings.CURRENT_USER
        order.data = date.today()
        order.type_cleaning = type_cleaning[request.POST["order-id"]]["name"]
        order.status = "Отправлен запрос"
        order.price = type_cleaning[request.POST["order-id"]]["price"]
        order.save()
        return HttpResponseRedirect("/account")

    return render(request, 'services.html')
