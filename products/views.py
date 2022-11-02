from django.shortcuts import render
from slideshow.models import Slideshow

def test(request):
    data = Slideshow.objects.all()
    slide_show = {'data':data}
    return render(request,'index.html',slide_show)