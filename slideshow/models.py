from common.utils import *
from django.db import models
from django.utils.safestring import mark_safe

class Slideshow(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.FileField(upload_to = rename_upload('slideshow/'), default=None)
    link = models.TextField(default=None, null=False)

    def slide_show_image(self):
        return mark_safe('<img src="{}" width = "100" />'.format(self.image.url))
