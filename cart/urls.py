
from django.urls import path
from . import views
 
app_name = 'cart'
 
urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove_one/<int:item_id>/', views.remove_one_from_cart, name='remove_one_from_cart'),
    path('cart/remove_all/<int:item_id>/', views.remove_all_from_cart, name='remove_all_from_cart'),
    path('add_one/<int:item_id>/', views.add_one_to_cart, name='add_one_to_cart'),
]