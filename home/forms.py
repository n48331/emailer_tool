from .models import *
from django.forms import ModelForm


class SearchFile(ModelForm):
    class Meta:
        model = File
        fields = ['country', 'product']
