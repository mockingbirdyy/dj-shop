from django.contrib import admin
from .models import Order, OrderItem, Coupon


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'paid', 'created', 'updated')
    list_filter = ('paid',)
    inlines = (OrderItemInline,)



@admin.register(Coupon)
class OrderAdmin(admin.ModelAdmin):
    model = Coupon
    list_display = ('code', 'valid_from', 'valid_to' ,'active')