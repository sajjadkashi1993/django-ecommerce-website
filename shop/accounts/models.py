from django.contrib.auth.models import AbstractUser
from django.db import models

from core.validators import PhoneValidator

from .managers import UserManager


class User(AbstractUser):
    ROLE_CHOICES = (('c', 'Customer'),
                    ('e1', 'Employee1'),
                    ('e2', 'Employee2'),
                    )

    username = None

    phone_validator = PhoneValidator()

    phone = models.CharField(
        "phone number",
        max_length=11,
        unique=True,
        help_text=(
            "Required. 11 character. digits only."
        ),
        validators=[phone_validator],
        error_messages={
            "unique": ("A user with that phone already exists."),
        },
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='c')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone
