from django.db import models
import jwt
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)




class User(PermissionsMixin, AbstractBaseUser):

    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'
        OTHERS = 'O'

    class MaritalStatus(models.TextChoices):
        MARRIED = 'MR'
        SINGLE = 'SI'
        SEPARATED = 'SE'
        DIVORCE = 'DV'
        OTHERS = 'OT'

    class Role(models.TextChoices):
       ADMIN = "AD"
       INFLUENCER = "IR"
       PARTNER = "PR"
       USER = "UR"


    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
        )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=10, null=True)
    role = models.CharField(choices=Role.choices, max_length=10, null=True)
    dob = models.DateField(null=True)
    marital_status = models.CharField(choices=MaritalStatus.choices, max_length=10, null=True)
    gender = models.CharField(choices=Gender.choices, max_length=10, null=True)
    resident_address = models.TextField(null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return self.username

