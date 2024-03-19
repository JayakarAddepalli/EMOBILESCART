from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Apple(models.Model):
    Image=models.ImageField(upload_to='appleImages')
    Name=models.CharField(max_length=100)
    Info=models.CharField(max_length=200)
    Cost=models.IntegerField()
    Anchors = models.URLField(default = 'http://127.0.0.1:8000/APP/')
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.Name
    
    
class CartItem(models.Model):
    appleproduct = models.ForeignKey(Apple, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.appleproduct.Name} * {self.quantity}'
    
    



    
class Oneplus(models.Model):
    Image=models.ImageField(upload_to='oneplusImages')
    Name=models.CharField(max_length=100)
    Info=models.CharField(max_length=200)
    Cost=models.IntegerField()
    Anchors = models.URLField(default = 'http://127.0.0.1:8000/APP/')
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.Name
    

class OneplusCartItem(models.Model):
    oneplusproduct = models.ForeignKey(Oneplus, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.oneplusproduct.Name} * {self.quantity}'
    
    



class Redmi(models.Model):
    Image=models.ImageField(upload_to='redmiImages')
    Name=models.CharField(max_length=100)
    Info=models.CharField(max_length=200)
    Cost=models.IntegerField()
    Anchors = models.URLField(default = 'http://127.0.0.1:8000/APP/')
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.Name
    
class RedmiCartItem(models.Model):
    redmiproduct = models.ForeignKey(Redmi, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.redmiproduct.Name} * {self.quantity}'
    





class Samsung(models.Model):
    Image=models.ImageField(upload_to='samsungImages')
    Name=models.CharField(max_length=100)
    Info=models.CharField(max_length=200)
    Cost=models.IntegerField()
    Anchors = models.URLField(default = 'http://127.0.0.1:8000/APP/')
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.Name
    
class SamsungCartItem(models.Model):
    samsungproduct = models.ForeignKey(Samsung, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.samsungproduct.Name} * {self.quantity}'






class Realme(models.Model):
    Image=models.ImageField(upload_to='realmeImages')
    Name=models.CharField(max_length=100)
    Info=models.CharField(max_length=200)
    Cost=models.IntegerField()
    Anchors = models.URLField(default = 'http://127.0.0.1:8000/APP/')
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.Name
    
class RealmeCartItem(models.Model):
    realmeproduct = models.ForeignKey(Realme, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.realmeproduct.Name} * {self.quantity}'
    





class Trends(models.Model):
    Trend1 = models.ForeignKey(Apple, on_delete = models.CASCADE)
    Trend2 = models.ForeignKey(Oneplus, on_delete = models.CASCADE)
    Trend3 = models.ForeignKey(Redmi, on_delete = models.CASCADE)
    Trend4 = models.ForeignKey(Samsung, on_delete = models.CASCADE)

class PaymentModel(models.Model):
    FullName = models.CharField(max_length = 60)
    Email = models.EmailField()
    PhNo = models.IntegerField()
    Address = models.TextField()
    PinCode = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
