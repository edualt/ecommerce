from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    "Manager for user model"
    
    def create_user(self, email, first_name, last_name, password=None):
        "Create new user"
        if not email:
            raise ValueError('User must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser=True
        user.is_staff=True

        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    "Database model for users"
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email
