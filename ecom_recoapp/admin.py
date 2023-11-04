from django.contrib import admin
from ecom_recoapp.models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','gender','masterCategory','subCategory','articleType','baseColour','season','year','usage','productDisplayName','product_image')   

class CartAdmin(admin.ModelAdmin):
    list_display = ('product_id','quantity')  


admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)

