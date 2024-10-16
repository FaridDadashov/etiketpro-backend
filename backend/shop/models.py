from django.db import models
from django.contrib.admin import display
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class OurProduct(models.Model):
        title=models.CharField(max_length=20)
        update=models.DateField(auto_now=True)
        created=models.DateTimeField(auto_now_add=True)
        image=models.ImageField()
        
        
def __str__(self):
    return self.title


class Projects(models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField()
    
    
def __str__(self):
    return self.title




class Friends(models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField()






class Product(models.Model):
    title=models.CharField(max_length=50)
    old_price=models.FloatField(null=True,blank=True)
    featured=models.BooleanField(default=False)
    price=models.FloatField()
    description=models.TextField()
    update=models.DateField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)     
    ourproduct=models.ManyToManyField(OurProduct,related_name='ourproduct')
    project=models.ManyToManyField(Projects,related_name='project')
    friends=models.ManyToManyField(Friends,related_name='friend')
    
    
    
    def __str__(self):
        return self.title
    


class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to='product_images')
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name

    
  
    
  
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
         return self.user.get_full_name()
    
    
    
    
    
    
    

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.TextField()
    text=models.TextField()    
    
    
def __str__(self):
    return self.name


