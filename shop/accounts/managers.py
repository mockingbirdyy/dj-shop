from django.contrib.auth.models import UserManager

# Creating users in custom user model.
class Manager(UserManager):

    def create_user(self, phone_number, email, full_name, password=None):
        if not phone_number:
            raise ValueError('phone_number is required.')
        if not email:
            raise ValueError('email is required.')
        if not full_name:
            raise ValueError('full_name is required.')
        if not password:
            raise ValueError('password is required.')
        # Refers back to User model, to construct user
        user = self.model(phone_number=phone_number,
                          email=self.normalize_email(email), full_name=full_name)
                          # normalize_email, normalizes email addresses by lowercasing the domain portion of the email address.
        # set_password creates a hashed password
        user.set_password(password)
        
        user.save(using=self._db) # Saving in default database
        
        return user
    # Same as create_user just set is_admin=True
    def create_superuser(self, phone_number, email, full_name, password=None):
        
        user = self.create_user(phone_number, email, full_name, password)
        
        user.is_admin = True
        user.save(using=self._db)
        
        return user
