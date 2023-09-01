from django.urls import path
from . import views
urlpatterns = [
    path('', views.account_show, name='account'),
    path('addaccount', views.add_in_account_bank, name='add_in_account_bank'),
]
