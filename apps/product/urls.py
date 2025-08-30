from django.urls import path
from apps.product.views import product_Views , search_ajax , edit_view

urlpatterns = [
    path('', product_Views, name='products'),
    path('search/', search_ajax , name = 'search_ajax'),
    path('product/<int:id>/' ,edit_view , name='edit_view'  ),
]
