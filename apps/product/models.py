from django.db import models
from apps.product.validators import validator_image

# Create your models here.
class article_Model (models.Model):
    title = models.CharField( max_length=50)
    
    def __str__(self):
        return f'{self.title}'
    


class product_Models (models.Model):
    name_pro = models.CharField(max_length=50)
    info_pro = models.CharField(max_length=100)
    price_pro = models.IntegerField()
    image_pro = models.ImageField(upload_to='image_pro/', validators=[validator_image], blank=True)

    class Meta:
        app_label = 'product'

    def __str__(self):
        return f'{self.name_pro} , {self.info_pro} '