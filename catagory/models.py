from django.db import models

class Catagory(models.Model):
    category_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.category_name
