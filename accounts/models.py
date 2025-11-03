from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name=_('username'),
        max_length=40,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
