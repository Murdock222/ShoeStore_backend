from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name

class ShoeType(models.Model):
    style = models.CharField(max_length=50)
    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    SHOE_COLOR_CHOICES = [
            ('Red', 'Red'),
            ('Orange', 'Orange'),
            ('Yellow', 'Yellow'),
            ('Green', 'Green'),
            ('Blue', 'Blue'),
            ('Indigo', 'Indigo'),
            ('Violet', 'Violet'),
            ('White', 'White')        
        ]
    color_name = models.CharField(choices=SHOE_COLOR_CHOICES,max_length=15)
    def __str__(self):
        return self.color_name


class ShoeManager(models.Manager):
    def Populatedata(self):
        ShoeType.objects.create(style='sneaker')
        ShoeType.objects.create(style='boot')
        ShoeType.objects.create(style='sandal')
        ShoeType.objects.create(style='dress')
        ShoeType.objects.create(style='other')    
        ShoeColor.objects.create(color_name='Red')
        ShoeColor.objects.create(color_name='Orange')
        ShoeColor.objects.create(color_name='Yellow')
        ShoeColor.objects.create(color_name='Green')
        ShoeColor.objects.create(color_name='Blue')
        ShoeColor.objects.create(color_name='Indigo')
        ShoeColor.objects.create(color_name='Violet')
        ShoeColor.objects.create(color_name='White')

class Shoe(models.Model):
    size = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True,blank=True,related_name='manufacturer' )
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE, null=True,blank=True ,related_name='color' )
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE, null=True,blank=True,related_name='shoe_type' )
    material = models.CharField(max_length=100)
    fasten_type =  models.CharField(max_length=100)
    objects = ShoeManager()

    def __str__(self):
        return self.brand_name
