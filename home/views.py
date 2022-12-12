from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import FileFilter
from json import dumps
# Create your views here.


@login_required(login_url='/accounts/login')
def home(request):
    files = File.objects.all()
    fileFilter = FileFilter(request.GET, queryset=files)
    countries = list(Country.objects.values())
    products = list(Product.objects.values())
    productIds = list(File.objects.values('productId'))
    print(productIds)
    files = fileFilter.qs
    context = {
        'files': files,
        'countries': dumps(countries),
        'products': dumps(products),
        'productIds': dumps(productIds),
        'fileFilter': fileFilter
    }
    return render(request, 'home.html', context)


def filterProject(request, country, product):

    files = File.objects.filter(country=country).filter(product=product)
    context = {
        'files': files,
    }
    return render(request, 'filter.html', context)
