import os , sys 
from django.core.exceptions import ValidationError


def validator_image (image):
    image_path = os.path.split(image.name)[1][1:].lower()
    validate_pass = ['jpg' ,'png' ,'jpeg']
    if image_path not in validate_pass :
        raise ValidationError('پسوند درست نیست جانا')
        