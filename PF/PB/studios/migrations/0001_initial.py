# Generated by Django 4.1 on 2022-12-07 19:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=120)),
                ('lon', models.FloatField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('postal_code', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='Postal codes must be entered in the following format: A1A 1A1 or A1A1A1', regex='^[A-Z]\\d[A-Z]\\s?\\d[A-Z]\\d$')])),
                ('phone_num', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+111111111 or 111-111-1111 (+ optional)'. Up to 10 digits allowed.", regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$')])),
                ('images', models.ImageField(blank=True, null=True, upload_to='studios')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('coach', models.CharField(max_length=120)),
                ('keywords', models.CharField(max_length=120)),
                ('capacity', models.PositiveIntegerField()),
                ('frequency', models.IntegerField(choices=[(2, 'Weekly'), (0, 'Once'), (1, 'Daily'), (3, 'Monthly')], null=True)),
                ('start_date', models.DateField(null=True)),
                ('start_time', models.CharField(max_length=120, null=True)),
                ('end_time', models.CharField(max_length=120, null=True)),
                ('cancelled_date', models.DateTimeField(blank=True, null=True)),
                ('curr_enrolled', models.PositiveIntegerField(default=0, null=True)),
                ('enrolled', models.ManyToManyField(blank=True, related_name='enrolled_users', to=settings.AUTH_USER_MODEL)),
                ('studio', models.ManyToManyField(related_name='studios_classes', to='studios.studio')),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
                ('quantity', models.PositiveIntegerField()),
                ('studio', models.ManyToManyField(related_name='studios_amenity', to='studios.studio')),
            ],
        ),
    ]