from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_show, name='account'),
    path('addaccount/', views.add_in_account_bank, name='add_in_account_bank'),
    path('deleteaccount/', views.delete_account, name='delete_account'),
    path('transactoin/', views.Transaction.as_view(), name='transactionsview'),
    path('transactoin/addtransaction/', views.MyFormView.as_view(), name='formtransaction'),
]
