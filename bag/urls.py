from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name='shopping_cart'),
    path('add/<item_id>/', views.cart_add, name='cart_add'),
    path('update/<item_id>/', views.cart_update, name='cart_update'),
    path('remove/<item_id>/', views.item_remove, name='item_remove'),
]