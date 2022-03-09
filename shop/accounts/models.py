from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import Manager

# Creating custom user model 
class User(AbstractUser):
    """ It's really important to set username to None, otherwise
    you face Django error: UNIQUE constraint failed: auth_user.username """
    username = None 
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    full_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = Manager()
    # USERNAME_FIELD must be: unique=True
    USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS are only used for creating superuser
    REQUIRED_FIELDS = ['full_name', 'email',]
    

    def has_perm(self, perm):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff (self):
        return self.is_admin
    
    def __str__(self):
        return f'{self.full_name} - {self.phone_number} - {self.is_admin}'

class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.CharField(max_length=4)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code} - {self.created}'
    