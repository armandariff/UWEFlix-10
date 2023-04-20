from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('booking', views.booking, name='booking'),
    path('account', views.account, name='account'),
    path('account_management', views.account_management, name='account_management'),
    path('add_account', views.add_account),
    path('view_account', views.view_account),
    path('modify_account', views.modify_account),
    path('cinema_management', views.cm_dash, name='cinema_management'),
    path('film_management', views.film_dash, name='film_management'),
    path('payment', views.payment, name='payment'),
    path('cancel_booking', views.cancel_booking, name='cancel_booking'),
    path('showings_management', views.showings_dash, name='showings_management'),
    path('screens_management', views.screens_dash, name='screens_management'),
    path('tickets_management', views.tickets_dash, name='tickets_management'),
    path('users_management', views.users_dash, name='users_management'),
    path('clubs_management', views.clubs_dash, name='clubs_management'),
    path('add', views.add, name='add'),
    path('modify', views.modify, name='modify'),
    path('delete', views.delete, name='delete'),
    path('request', views.request, name='request'),
    path('accept', views.accept, name='accept'),
    path('reject', views.reject, name='reject'),
]
