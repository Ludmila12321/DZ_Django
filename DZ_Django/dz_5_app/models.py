from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='Это прекрасный продукт!', blank=True)
    price = models.DecimalField(default=100.00, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Общая сумма заказа
    order_date = models.DateField(auto_now_add=True)
    
    def str(self):
        return f'Order for {self.client}'

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.quantity * self.price_per_item
        self.order.total_amount += self.total_price
        self.order.save()
        super(OrderProduct, self).save(*args, **kwargs)