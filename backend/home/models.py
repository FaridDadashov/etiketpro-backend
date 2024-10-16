from django.db import models

# Create your models here.
class Certificate(models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField()
    
    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    product=models.ForeignKey(Certificate,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to='product_images')