from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where phone is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone, password=None, **extra_fields):
        """
        Create and save a User with the given phone and password.
        """
        if not phone:
            raise ValueError('The phone must be set')
        # email = self.normalize_email(email)

        user = self.model(phone=phone, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given phone and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(phone, password, **extra_fields)


class CustomerManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role__in=(1, 0))
