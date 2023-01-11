from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(File)
admin.site.register(Product)
admin.site.register(Country)
admin.site.site_header = "CEB Email Finder Admin"
admin.site.site_title = "CEB Email Finder Admin Portal"
admin.site.index_title = "Welcome to CEB Email Finder Portal"