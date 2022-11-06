# Generated by Django 4.1.2 on 2022-11-06 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_profile.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=12, validators=[user_profile.validators.check_valid_phone_number])),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(max_length=100)),
                ('roles', models.CharField(choices=[('BUYER', 'Buyer'), ('SELLER', 'Seller')], max_length=6)),
                ('organization_name', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'db_table': 'user_profile',
            },
        ),
    ]