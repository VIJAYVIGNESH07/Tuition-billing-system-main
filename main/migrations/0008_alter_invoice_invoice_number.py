# Generated by Django 5.1 on 2024-12-01 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_invoice_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(default='C407626B', max_length=100, unique=True),
        ),
    ]
