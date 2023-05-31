from django.urls import path 
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', ProductCategoryView.as_view(), name='index'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('detail/', detail, name='detail'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('detail/<slug:slug>/', ShopDetail.as_view(), name='detail'),
]


