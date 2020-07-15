from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

from django.utils import timezone

from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_field):
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'




