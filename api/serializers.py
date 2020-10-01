from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ['id','name', 'website']


class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeType
        fields = ['id','style']


class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeColor
        fields = ['id','color_name']
        

class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Shoe
        fields = ['id','size', 'brand_name','manufacturer','color','shoe_type','material','fasten_type']
