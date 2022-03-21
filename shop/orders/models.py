from django.db import models
from accounts.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user_related_name')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False, null=True)

    def get_total_price(self):
        return sum(item.get_cost() for item in self.oreder_related_name.all())
    
    def __str__(self):
        return f'{self.user}-{self.paid}'
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_related_name')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='oreder_related_name')
    price = models.IntegerField()
    quantity = models.SmallIntegerField(default=1)


    def __str__(self):
        return f'{self.product}-{self.price}-{self.order}'

    def get_cost(self):
        return self.price * self.quantity

