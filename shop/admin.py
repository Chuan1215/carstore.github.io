from django.contrib import admin
from .models import Order,Car
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','car','quantity','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('user__username','car_name',)