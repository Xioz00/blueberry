from django.urls import path
from . import views

urlpatterns=[
    path('accounts/', views.accounts, name='accounts'),
    path('register/', views.register, name='Register'),
    path('login/', views.login, name='Login'),

]