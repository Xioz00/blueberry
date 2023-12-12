from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('accounts/', views.accounts, name='accounts'),
    path('<slug:c_slug>/', views.home, name='product_category'),
    path('<slug:c_slug>/<slug:Products_slug>/', views.prodDetails, name='product_details'),
    path('search',views.searching, name= 'search'),
    path('cart', views.cart, name= 'cart'),

]

