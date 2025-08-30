from django.db import models 
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager , AbstractUser
from django.core.validators import RegexValidator
import random
from datetime import timedelta
from django.utils import timezone
from encrypted_model_fields.fields import EncryptedCharField, EncryptedTextField

class EditBaseUserManager (BaseUserManager):
    def create_user (self , phone_number  , password = None , **extra_fields ):
        if not phone_number:
            raise ValueError('شماره نامعتبر است')
        
        user_name = f'user_{phone_number}'

        

        
        user =self.model(
            phone_number = phone_number,
            user_name = user_name ,
            **extra_fields
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)

        return user
    
    def create_superuser (self , phone_number , password = None , **extra_fields):
        if not password :
            raise ValueError('make password')
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('این staff نیست')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('این super نیست')

        return self.create_user(phone_number , password ,  **extra_fields)
    

        
phon_number_iran = RegexValidator(
    regex=r'^(\+98|0)?9\d{9}$', 
    message='شماره موبایل معتبر وارد کنید'
)

class CustomUser(AbstractBaseUser , PermissionsMixin):
    phone_number = EncryptedCharField(max_length=11, validators=[phon_number_iran], unique=True)    
    user_name = EncryptedCharField(max_length=50 , blank= True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []  


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = EditBaseUserManager()
    def __str__(self):
        return self.phone_number

   

        
    class Meta :
        permissions = [('edit profile','can_edit_product' )]

class profile (models.Model):
    email = EncryptedCharField(unique=True ,)
    address =EncryptedTextField(max_length=80 , )
    code_post = EncryptedCharField(max_length=80 ,)

