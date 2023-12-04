from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_products,name='products'),
    path('<int:product_id>/', views.product_view, name='product_view'),
    path('add/', views.product_add, name='product_add'),
    path('edit/<int:product_id>/', views.product_edit, name='product_edit'),
    path('delete/<int:product_id>/', views.product_delete, name='product_delete'),
]