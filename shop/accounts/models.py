from django.contrib.auth.models import AbstractUser
from django.db import models

from core.validators import PhoneValidator

from .managers import UserManager
from core.models import BaseModel

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
    GENDER_CHOICES = (('m','Male'),('f','female'),('o','Other'))

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=f'profile/',null=True,blank=True)


    def __str__(self) -> str:
        return f'profile for {self.user}'