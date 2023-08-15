from django.urls import path
from . import views
urlpatterns = [
    path('', views.account_show, name='home'),
]
