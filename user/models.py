from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from user.manager import UserManager


class Profile(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    email_address = models.EmailField(null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email_address', 'password']

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.username
