from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url = ''
        return url
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)
    transaction_id =  models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=0)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    City = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'ShippingAddresses'

    def __str__(self):
        return self.address
    



