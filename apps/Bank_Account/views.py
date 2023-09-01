from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Bank_Account


# Create your views here.
def account_show(request):
    user = request.user  # Get the logged-in user
    accs = Bank_Account.objects.filter(user=user)
    return render(request, 'show account.html', {'acc': accs})


def add_in_account_bank(request):
    if request.user.is_authenticated:
        name = request.GET.get('name')
        number = request.GET.get('number')
        cash = request.GET.get('cash')
        # Bank_Account(accountNumber=number,cash=int(cash),number=number,user=request.user)
        print(name, len(number), number.isdigit(), cash)
        if name != None and len(number) == 16 and cash != None and number.isdigit():
            add = Bank_Account(accountNumber=number, cash=int(cash), name=name, user=request.user)
            add.save()
    accs = Bank_Account.objects.filter(user=request.user)

    # data = {
    #     'user': 'user',
    #     'html': html
    # }
    return render(request, 'load account list.html', {'acc': accs})
