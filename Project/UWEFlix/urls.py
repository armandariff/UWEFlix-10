from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('booking', views.booking, name='booking'),
    path('temp', views.temp, name='temp'),
    path('account', views.account, name='account'),
    path('account_management', views.account_management, name='account_management'),
    path('add_account', views.add_account),
    path('view_account', views.view_account),
    path('modify_account', views.modify_account),
]
