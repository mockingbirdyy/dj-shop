from django.db import models
from accounts.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user_related_name')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False, null=True)
    discount = models.CharField(max_length=20,null=True, blank=True, default=None)
    
    def get_total_price(self):
        total = sum(item.get_cost() for item in self.order_related_name.all())
        if self.discount:
            discount_price = float((float(self.discount) / 100) * total)
            return float(total - discount_price)
        return total

    def __str__(self):
        return f'{self.user}-{self.paid}'
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_related_name')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_related_name')
    price = models.IntegerField()
    quantity = models.SmallIntegerField(default=1)


    def __str__(self):
        return f'{self.product}-{self.price}-{self.order}'

    def get_cost(self):
        return float(self.price * self.quantity)

class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.code} - {self.valid_from} - {self.valid_to} - {self.active}'
    