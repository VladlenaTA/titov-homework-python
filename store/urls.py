from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('all_products', views.all_products, name='all_products'),
    path('home', views.home),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('change/<int:id>/', views.change_product, name='change_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]
