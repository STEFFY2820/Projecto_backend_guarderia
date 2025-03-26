from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        user=self.model(
            email=self.normalize_email(email),
            **extra_fields
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user=self.create_user(
            email=email,
            password=password,
            )
        
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user