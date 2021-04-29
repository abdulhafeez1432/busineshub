from django.core.exceptions import ValidationError
import os
    


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value


def validate_file_extension02(value):
    
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


def validate_file_extension(value):
  
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.pdf','.doc','.docx']
  if not ext in valid_extensions:
    raise ValidationError(u'File not supported!')


