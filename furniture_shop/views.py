from django.shortcuts import render


def index(request):
    return render(request, 'furniture_shop/index.html')


def contact(request):
    return render(request, 'furniture_shop/contact.html')
