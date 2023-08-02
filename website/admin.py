from django.contrib import admin
from .models import Record, Category, Item, Purchase

admin.site.register(Record)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Purchase)