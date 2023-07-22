# Generated by Django 4.2.3 on 2023-07-22 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('chamber_file_number', models.PositiveIntegerField(blank=True, null=True)),
                ('Representativ', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('additional_mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('short_note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('law_and_section', models.TextField()),
                ('case_no', models.PositiveIntegerField()),
                ('fixed_for', models.TextField(blank=True, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Decided', 'Decided'), ('Abandoned', 'Abandoned')], default='Running', max_length=20)),
                ('updated', models.BooleanField(default=False)),
                ('appointed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointed_cases', to='cases.client')),
                ('case_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.casetype')),
                ('court', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.court')),
                ('first_party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_party_cases', to='cases.client')),
                ('police_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.policestation')),
                ('second_party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_party_cases', to='cases.client')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
