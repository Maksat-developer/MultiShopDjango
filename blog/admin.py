from django.contrib import admin
from .models import Product, Category, Contact, Review

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Review)