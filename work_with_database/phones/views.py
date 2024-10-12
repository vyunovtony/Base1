from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Phone


def index(request: HttpRequest):
    return redirect('catalog')


def show_catalog(request: HttpRequest):
    sort_param = request.GET.get('sort', '')
    template = 'catalog.html'
    match sort_param:
        case 'min_price':
            context = {'phones': Phone.objects.all().order_by('price')}
        case 'max_price':
            context = {'phones': Phone.objects.all().order_by('-price')}
        case 'name':
            context = {'phones': Phone.objects.all().order_by('name')}
        case _:
            context = {'phones': Phone.objects.all()}

    return render(request, template, context)


def show_product(request: HttpRequest, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
