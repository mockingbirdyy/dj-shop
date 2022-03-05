from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import Manager


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    full_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = Manager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name', 'email',]
    

    def has_perm(self, perm):
        return True

    def has_module_perms(self, app_label):
        return True

    
    def __str__(self):
        return f'{self.full_name} - {self.phone_number} - {self.is_admin}'
    
    @property
    def is_staff (self):
        return self.is_admin
