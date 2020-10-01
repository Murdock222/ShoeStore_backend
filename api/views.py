from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from . import models


class ShoeViewSet(viewsets.ModelViewSet):
    """
    An endpoint that allows shoes to be viewed 
    Why shouldn't Joe play poker in the savanna?
    Because, there are too many cheetahs there.
    """
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeSerializer

class ShoeTypeSet(viewsets.ModelViewSet):
    """
    Endpoint that allows shoes type to be viewed
    """
    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeTypeSerializer

class ShoeColorSet(viewsets.ModelViewSet):
    """
    Endpoint that allows shoes color to be viewed
    """
    queryset = models.ShoeColor.objects.all()
    serializer_class = serializers.ShoeColorSerializer
  

class ManufacturerTypeSet(viewsets.ModelViewSet):
    """
    Endpoint that allows shoes type to be viewed
    """
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer