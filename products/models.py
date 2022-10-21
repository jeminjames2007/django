from django.db import models
from catagory.models import Catagory
from django.utils.safestring import mark_safe


class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE,default=False,null=False)
    image = models.ImageField(upload_to = 'product_images/',default=False,null=False)
    quantity = models.IntegerField(default=False,null=False)
    price = models.IntegerField(default=False,null=False)

    def product_image(self):
        return mark_safe('<img src="{}" width = "100" />'.format(self.image.url))



