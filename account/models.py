from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 22.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))



class User(AbstractUser):
    is_seller = models.BooleanField('Seller status', default=False)
    is_buyer = models.BooleanField('Buyer status', default=False)





