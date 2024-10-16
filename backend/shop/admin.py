from django.contrib import admin
from . models import Product,ProductImage,OurProduct,Projects,Friends,Contact
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(OurProduct)
admin.site.register(Projects)
admin.site.register(Friends)
admin.site.register(Contact)