from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='store-index'),
    path('products/', views.products, name='store-products'),
    path('product-order/<int:pk>/', views.product_order, name='product-order'),
    path('products/delete/<int:pk>/', views.product_delete,
        name='store-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail,
        name='store-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit,
        name='store-products-edit'),
    path('customers/', views.customers, name='store-customers'),
    path('customers/detial/<int:pk>/', views.customer_detail,
         name='store-customer-detail'),
    path('order/', views.order, name='store-order'),
]
