# Generated by Django 4.2.4 on 2023-10-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank_Account', '0014_alter_accounting_document_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting_document',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
