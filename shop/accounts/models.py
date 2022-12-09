from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import BaseModel

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


class ProfileUser(BaseModel):
    class GENDER(models.IntegerChoices):
        MALE = 1, 'Male'
        FEMALE = 2, 'Female'
        OTHER = 3, 'Other'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    gender = models.IntegerField(choices=GENDER.choices, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=f'profile/', null=True, blank=True)

    def __str__(self) -> str:
        return f'profile for {self.user}'


class Address(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses')
    country = models.CharField(max_length=100, default='iran')
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    adderess = models.TextField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.country}, {self.province}, {self.city}, {self.adderess}'


class OtpCode(BaseModel):
    phone = models.CharField(
        "phone number",
        max_length=11,
        unique=True,
        help_text=(
            "Required. 11 character. digits only."
        ),
        error_messages={
            "unique": ("A user with that phone already exists."),
        },
    )

    code = models.CharField(max_length=8)
    number_try = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.code
