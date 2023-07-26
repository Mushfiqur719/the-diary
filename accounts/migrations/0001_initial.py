# Generated by Django 4.2.3 on 2023-07-25 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0003_client_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense')], max_length=20)),
                ('party_name', models.CharField(blank=True, max_length=50, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Quotations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('vat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.client')),
            ],
        ),
        migrations.CreateModel(
            name='BillInvoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('vat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.client')),
            ],
        ),
    ]
