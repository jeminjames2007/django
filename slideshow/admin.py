from django.contrib import admin
from .models import Slideshow

class SlideshowAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle','slide_show_image')

admin.site.register(Slideshow,SlideshowAdmin)