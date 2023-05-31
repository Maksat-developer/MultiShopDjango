from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Product, BasketQuerySet, Basket



@login_required
def basket_add(request, slug):
    product = Product.objects.get(slug=slug)
    baskets = Basket.objects.filter(user=request.user, product=product)


    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def basket_remove_all(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_one(request, id):
    basket = Basket.objects.get(id=id)
    basket.quantity -= 1
    basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def cart(request):
    baskets = Basket.objects.filter(user=request.user)
    context = {
        "baskets": baskets
    }
    return render(request, template_name='blog/cart.html', context=context)



