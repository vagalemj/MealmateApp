from django.contrib import admin
from .models import Customer, Restaurants, Menu

# Register your models here.
admin.site.register(Customer)
admin.site.register(Restaurants)
admin.site.register(Menu)