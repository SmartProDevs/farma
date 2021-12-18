from django.db import models
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, name, password,user_type, is_superuser=False, is_active=True,**extra_fields):

        user =self.model(name=name,user_type=user_type,is_superuser=is_superuser, is_active=is_active,
        **extra_fields)

        if password:
            user.set_password(password)
            user.save()
            return user



class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    USER_TYPE_CHOICES = (
        (1, 'superadmin'),
        (2, 'admin'),
        (3, 'user'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

    USERNAME_FIELD = "name"
    objects = UserManager()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering =["-date_joined"]
        get_latest_by = "date-joined"