from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from slideshow.models import Slideshow
from slideshow.serializers import SlideshowSerializer

@api_view(['GET'])

def getSliderData(request):
    slider = Slideshow.objects.all()
    serializer = SlideshowSerializer(slider,many=True)
    return Response(serializer.data)
