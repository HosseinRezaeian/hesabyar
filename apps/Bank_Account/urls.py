from django.urls import path
from . import views
urlpatterns = [
    path('show/', views.account_show, name='accountshow'),
]
