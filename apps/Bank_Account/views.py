from django.shortcuts import render
from .models import Bank_Account

# Create your views here.
def account_show(request):
    accs=Bank_Account.objects.all()
    return render(request, 'show account.html',{'acc':accs})
