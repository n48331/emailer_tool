from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import FileFilter
from json import dumps

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


@login_required(login_url='/accounts/login')
def home(request):
    files = File.objects.all()
    fileFilter = FileFilter(request.GET, queryset=files)
    countries = list(Country.objects.values())
    crmProducts = list(Product.objects.values())
    mysheetIds = list(File.objects.values('mysheetId'))
    files = fileFilter.qs
    context = {
        'files': files,
        'countries': dumps(countries),
        'crmProducts': dumps(crmProducts),
        'mysheetIds': dumps(mysheetIds),
        'fileFilter': fileFilter
    }
    return render(request, 'home.html', context)


def filterProject(request, country, crmProduct):

    files = File.objects.filter(country=country).filter(crmProduct=crmProduct)
    context = {
        'files': files,
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)