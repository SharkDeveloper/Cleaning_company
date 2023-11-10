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
    if request.method == 'POST' and 'login-app' in request.POST:
        user = request.POST['username']
        password = request.POST['password']
        if user in Clients.objects.all():
            settings.CURRENT_USER = Clients.objects.filter(name=user, password=password).first()
            return render(request, 'account.html', settings.CURRENT_USER)
    return render(request, 'auth.html')


def services(request):
    if request.method == 'POST' and 'get-services' in request.POST:
        if isinstance(settings.CURRENT_USER, str):
            order = Orders()
            order.author = settings.CURRENT_USER
            order.data = date.today()
            order.type_cleaning = type_cleaning[request.POST["order-id"]]["name"]
            order.status = "Отправлен запрос"
            order.price = type_cleaning[request.POST["order-id"]]["price"]

    return render(request, 'services.html')
