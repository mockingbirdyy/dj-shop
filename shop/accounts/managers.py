from django.contrib.auth.models import UserManager


class Manager(UserManager):

    def create_user(self, phone_number, email, full_name, password):
        if not phone_number:
            raise ValueError('phone_number is required.')
        if not email:
            raise ValueError('email is required.')
        if not full_name:
            raise ValueError('full_name is required.')
        if not password:
            raise ValueError('password is required.')

        user = self.model(phone_number=phone_number,
                          email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, full_name, password):
        user = self.create_user(phone_number, email, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user