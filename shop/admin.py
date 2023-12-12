from django.contrib import admin
from .models import *
# Register your models here.
class catoadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, catoadmin)

class proadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','image']
    list_editable = ['price','price','stock','image']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Products, proadmin)