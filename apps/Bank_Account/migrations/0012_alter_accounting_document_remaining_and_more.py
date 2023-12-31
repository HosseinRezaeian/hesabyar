# Generated by Django 4.2.4 on 2023-09-15 21:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Bank_Account', '0011_accounting_document_remaining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting_document',
            name='remaining',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bank_account',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
