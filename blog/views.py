from django.shortcuts import render
from .models import Product, Category
from django.views.generic import ListView, DetailView
from django.views.generic.base import View


class ProductCategoryView(View):

    def get(self, request):
        category = Category.objects.all()
        product = Product.objects.filter(rating=5)

        context = {
            "categories": category,
            "products": product
        }
        return render(request=request, template_name="blog/index.html", context=context)


def checkout(request):
    return render(request, template_name='blog/checkout.html')


def contact(request):
    return render(request, template_name='blog/contact.html')


def detail(request):
    return render(request, template_name='blog/detail.html')

class ShopDetail(DetailView):
    model = Product
    template_name = 'blog/detail.html'
    context_object_name = 'product'

class ShopListView(ListView):
    model = Product
    template_name = "blog/shop.html"
    context_object_name = 'products'
