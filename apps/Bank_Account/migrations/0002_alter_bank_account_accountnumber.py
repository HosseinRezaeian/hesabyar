# Generated by Django 4.2.3 on 2023-07-24 16:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank_Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_account',
            name='accountNumber',
            field=models.CharField(max_length=19, validators=[django.core.validators.RegexValidator(message='Enter a valid account number in the format XXXX-XXXX-XXXX-XXXX.', regex='^\\d{4}-\\d{4}-\\d{4}-\\d{4}$')]),
        ),
    ]