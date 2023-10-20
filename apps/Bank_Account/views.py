from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Bank_Account, Accounting_Document
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from .forms import FormTransaction
from django.urls import reverse_lazy


class Transaction(TemplateView):
    template_name = 'show_transaction.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Transaction, self).get_context_data(*args, **kwargs)
        accs = Bank_Account.objects.filter(user=self.request.user)
        transact = Accounting_Document.objects.filter(account__in=accs)
        context['transactions'] = transact
        return context

    # def get(self, request):
    #     if request.user.is_authenticated:
    #         accs = Bank_Account.objects.filter(user=request.user)
    #         transact = Accounting_Document.objects.filter(account__in=accs)
    #     return render(request, 'show_transaction.html', {'transactions': transact})


# Create your views here.
def account_show(request):
    user = request.user  # Get the logged-in user
    accs = Bank_Account.objects.filter(user=user)
    total_amount = sum(account.cash for account in accs)
    return render(request, 'show account.html', {'acc': accs, 'total_amount': total_amount})


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
    total_amount = sum(account.cash for account in accs)
    return render(request, 'load account list.html', {'acc': accs, 'total_amount': total_amount})


def delete_account(request):
    if request.user.is_authenticated:
        print('delete', request.GET.get('idacc'))
        obj = get_object_or_404(Bank_Account, id=request.GET.get('idacc'))
        obj.delete()
        accs = Bank_Account.objects.filter(user=request.user)
        total_amount = sum(account.cash for account in accs)

    return render(request, 'load account list.html', {'acc': accs, 'total_amount': total_amount})


class MyFormView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = {'form': FormTransaction(request=request)}
        return render(request, "add_transaction_form.html", context=context)

    def post(self, request):
        form = FormTransaction(request.POST)  # Bind the form to the POST data

        if form.is_valid():  # Check if the form is valid
            form.save()
            return redirect('transactionsview')

