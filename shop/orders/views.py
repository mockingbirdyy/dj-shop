from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from products.models import Product
from .forms import CartAddForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem


class Cart:
    CART_SESSION_ID = 'cart'
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.CART_SESSION_ID)
        if not cart:
            cart = self.session[self.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, quantity, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()
        

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['total_price'] = float(item['price']) * item['quantity']
            yield item

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())
    
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def clear(self):
        del self.session[self.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True


class CartView(View):
    
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {'cart': cart})


class CartAddView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(quantity=1, product=product)
        return redirect('products:home')


    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(quantity=form.cleaned_data['quantity'], product=product)
            return redirect('products:home')

class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('orders:cart')  



class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        template_name = 'orders/order_detail.html'
        order = get_object_or_404(Order, id=order_id)
        return render(request, template_name, {'order': order})



class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        order_id = order.id
        for item in cart:
            OrderItem.objects.create(product=item['product'], order=order, price=float(item['price']), quantity=item['quantity'] )      
        return redirect('orders:order_detail', order_id)
