from django.shortcuts import render
from .models import Bank_Account


# Create your views here.
def account_show(request):
    user = request.user  # Get the logged-in user
    accs = Bank_Account.objects.filter(user=user)
    return render(request, 'show account.html', {'acc': accs})
