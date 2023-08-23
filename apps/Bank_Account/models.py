from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Create your models here.
class Bank_Account(models.Model):
    account_number_validator = RegexValidator(
        regex=r'^\d{4}-\d{4}-\d{4}-\d{4}$',
        message='Enter a valid account number in the format XXXX-XXXX-XXXX-XXXX.'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    accountNumber = models.CharField(max_length=19,  # Set the maximum length for the formatted account number
                                     validators=[account_number_validator])  # Replace with your desired minimum value

    cash = models.IntegerField()

    def clean(self):
        # Remove any hyphens from the input and check the format
        cleaned_account_number = self.accountNumber.replace('-', '')
        if not cleaned_account_number.isdigit() or len(cleaned_account_number) != 16:
            raise ValidationError('Enter a valid 16-digit account number.')

        # Add the hyphens to the account number in the desired format
        formatted_account_number = '-'.join(
            cleaned_account_number[i:i + 4] for i in range(0, 16, 4)
        )

        self.accountNumber = formatted_account_number

    def __str__(self):
        return f"{self.user.username}'s Bank Account - {self.accountNumber}"


class Accounting_Document(models.Model):
    account = models.ForeignKey(Bank_Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type_chose = [
        ("debit", "debit"),
        ("credit", "credit"),
    ]
    type = models.CharField(choices=type_chose, max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.account}"
