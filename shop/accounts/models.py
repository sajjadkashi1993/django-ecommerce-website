from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from core.validators import PhoneValidator

from .managers import UserManager


class User(AbstractUser):
    class ROLE(models.IntegerChoices):
        USER = 0, _('User')
        CUSTOMER = 1, _('Customer')
        ADMIM = 2, _('Admin')
        EMPLOYEE = 3, _('Employee')

    username = None
    phone_validator = PhoneValidator()

    phone = models.CharField(
        _("phone number"),
        max_length=11,
        unique=True,
        help_text=(
            _("Required. 11 character. digits only.")
        ),
        validators=[phone_validator],
        error_messages={
            "unique": _("A user with that phone already exists."),
        },
    )

    role = models.CharField(_('role'), max_length=20,
                            choices=ROLE.choices, default=ROLE.USER)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.phone


class ProfileUser(BaseModel):
    class GENDER(models.IntegerChoices):
        MALE = 1, _('Male')
        FEMALE = 2, _('Female')
        OTHER = 3, _('Other')

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', verbose_name=_('user'))
    gender = models.IntegerField(
        _('gender'), choices=GENDER.choices, null=True, blank=True)
    birthday = models.DateField(_('birthday'), null=True, blank=True)
    bio = models.TextField(_('bio'), null=True, blank=True)
    image = models.ImageField(
        _('image'), upload_to=f'profile/', null=True, blank=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self) -> str:
        return f'profile for {self.user}'


class Address(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses', verbose_name=_("user"))
    country = models.CharField(_("country"), max_length=100, default='iran')
    province = models.CharField(_("province"), max_length=100)
    city = models.CharField(_("city"), max_length=100)
    adderess = models.TextField(_("adderess"), max_length=100)
    postal_code = models.CharField(_("postal code"), max_length=20)

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _('adresses')

    def __str__(self):
        return f'{self.country}, {self.province}, {self.city}, {self.adderess}'


class OtpCode(BaseModel):
    phone = models.CharField(
        _("phone number"),
        max_length=11,
        unique=True,
        help_text=(
            _("Required. 11 character. digits only.")
        ),
        validators=[PhoneValidator()],
        error_messages={
            "unique": _("A user with that phone already exists."),
        },
    )

    code = models.CharField(_('code'), max_length=8)
    number_try = models.PositiveSmallIntegerField(_('number try'), default=0)

    class Meta:
        verbose_name = _("OTP Code")
        verbose_name_plural = _('OTP Codes')

    def __str__(self):
        return self.code
