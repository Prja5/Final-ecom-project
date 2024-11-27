from django.contrib import admin
from.models import Product, cart, orders
# Register your models here.

class ProAdmin(admin.ModelAdmin):
    list_display=['id','name', 'price','pdetails','cat','is_active']
    list_filter=['cat','is_active']  
class cartAdmin(admin.ModelAdmin):  
    list_display=['id','uid','pid']
admin.site.register(cart,cartAdmin)
admin.site.register(Product,ProAdmin)

class OrderAdmin(admin.ModelAdmin):  
    list_display=['id','order_id','uid','pid']
admin.site.register(cart,cartAdmin)
admin.site.register(Product,ProAdmin)
admin.site.register(orders,OrderAdmin)



