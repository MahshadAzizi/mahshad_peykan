from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """

        user = self.model(username=username, password=password, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.
        """

        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
