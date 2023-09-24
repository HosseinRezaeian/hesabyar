from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import uuid
from django.core.validators import RegexValidator


# Create your models here.
class Bank_Account(models.Model):
    account_number_validator = RegexValidator(
        regex=r'^\d{4}-\d{4}-\d{4}-\d{4}$',
        message='Enter a valid account number in the format XXXX-XXXX-XXXX-XXXX.'
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    accountNumber = models.CharField(max_length=16, unique=True)  # Replace with your desired minimum value

    cash = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s Bank Account - {self.accountNumber}"


class Accounting_Document(models.Model):
    account = models.ForeignKey(Bank_Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type_chose = [
        ("debit", "debit"),
        ("credit", "credit"),
    ]
    type = models.CharField(choices=type_chose, max_length=20, null=True)
    datetime = models.DateTimeField(null=True)
    remaining = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate remaining based on cash and amount
        if self.type == 'debit':
            self.remaining = self.account.cash - self.amount
        elif self.type == 'credit':
            self.remaining = self.account.cash + self.amount
        self.account.cash = self.remaining
        self.account.save()
        super(Accounting_Document, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.account}"
