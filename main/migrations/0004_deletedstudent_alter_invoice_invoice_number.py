# Generated by Django 4.2.16 on 2024-11-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_invoice_invoice_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent_name', models.CharField(max_length=255)),
                ('phone_number1', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('total_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advance_payment_months', models.IntegerField(default=0)),
                ('subjects', models.TextField()),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(default='92EB7831', max_length=100, unique=True),
        ),
    ]