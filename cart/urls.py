from django.urls import path
from .views import basket_add, remove_one, cart, basket_remove_all


app_name = 'basket'


urlpatterns = [
    path('basket_add/<slug:slug>/', basket_add, name='basket_add'),
    path('remove_one/<int:id>/', remove_one, name='remove_one'),
    path('basket_remove_all/<int:id>/', basket_remove_all, name='basket_remove_all'),
    path('', cart, name='cart'),
]