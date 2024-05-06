from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

User = get_user_model()

STATUSES = {
    ('D', 'Deliverd'),
    ('ND', 'Not Deliverd')
}

PAYMENT_METHODS = {
    ('card', 'CARD'),
    ('cash', 'CASH')
}

class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    product = models.ManyToManyField(Product, through='OrderItem')
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=4, choices=STATUSES)
    payment = models.CharField(max_length=5, choices=PAYMENT_METHODS)

    def __str__(self) -> str:
        return f'{self.pk} - {self.user.email}'


class OrderItem(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказать товары'


    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.pk} - {self.order.user.email}'