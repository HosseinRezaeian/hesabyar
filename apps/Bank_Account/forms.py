from django import forms
from .models import Accounting_Document, Bank_Account
from jalali_date.fields import SplitJalaliDateTimeField
from jalali_date.widgets import AdminSplitJalaliDateTime

class FormTransaction(forms.ModelForm):

    class Meta:
        model = Accounting_Document
        fields = ["account", "datetime", "type", "amount"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['datetime'] = SplitJalaliDateTimeField(label='date time',
                                                           widget=AdminSplitJalaliDateTime)

        # Now you can access self.request in the form's __init__ method
        if self.request:
            user = self.request.user
            # Filter the 'account' field queryset based on the ForeignKey to the user
            # self.fields['account'].queryset = Accounting_Document.objects.filter(user=user)
            accs = Bank_Account.objects.filter(user=self.request.user)
            self.fields['account'].queryset = accs
