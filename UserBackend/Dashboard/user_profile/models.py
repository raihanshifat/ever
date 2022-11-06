import uuid

from django.db import models
from django.contrib.auth.models import User
from user_profile.validators import check_valid_phone_number

# # Create your models here.
class UserProfile(models.Model):
    role_choices = [
        ("BUYER","Buyer"),
        ("SELLER","Seller")
    ]
    class Meta:
        db_table = "user_profile"
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    full_name = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True,null=False, blank=False)
    phone = models.CharField(max_length=12, validators=[check_valid_phone_number], blank=False, null=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=100,blank=False,null=False)
    roles = models.CharField(max_length=6,choices=role_choices,blank=False,null=False)
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

