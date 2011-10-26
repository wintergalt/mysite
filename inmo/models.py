from django.db import models

# Create your models here.
class Property(models.Model):
    internal_code = models.IntegerField()
    title = models.CharField(max_length=50)
    property_type = models.ForeignKey(PropertyType)
    price = models.DecimalField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    property_specs = models.ForeignKey(PropertySpecs)
    
class PropertyType(models.Model):
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    
class Post(models.Model):
    pub_date = models.DateTimeField('date published')
    property = models.ForeignKey(Property)
    
class PropertySpecs(models.Model):
    bedrooms = models.IntegerField()
    garage = models.IntegerField()
    living_room = models.IntegerField()
    kitchen = models.IntegerField()
    washroom = models.IntegerField()
    backyard = models.IntegerField()
    reserved = models.BooleanField()
    laundry_room = models.IntegerField()
    new_property = models.BooleanField()
    running_water = models.BooleanField()
    phone = models.BooleanField()
    apt_bank = models.BooleanField()
    natural_gas = models.BooleanField()
    sewer = models.BooleanField()
    pavement = models.BooleanField()
    electricity = models.BooleanField()