import re
from django.core.exceptions import ValidationError


def check_valid_phone_number(value):
    if not re.findall('^01[13-9]\d{8}$', value):
        raise ValidationError("Enter valid phone number")