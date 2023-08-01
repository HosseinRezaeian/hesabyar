from django.contrib import admin
from .models import Bank_Account, Accounting_Document


# Register your models here.

@admin.register(Bank_Account)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'accountNumber', 'cash')  # Fields to display in the list view
    search_fields = ('user__username', 'name', 'accountNumber')  # Add fields for searching
    list_filter = ('user',)


admin.site.register(Accounting_Document)
