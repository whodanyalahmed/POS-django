from django.contrib import admin
from .models import inventory,Sells,Product

# Register your models here.

admin.site.register([inventory,Sells,Product])



