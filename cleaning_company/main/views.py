from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def account(request):
    return render(request, 'account.html')


def services(request):
    return render(request, 'services.html')
