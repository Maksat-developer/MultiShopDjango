from django.db import models
from accounts.models import MyUser
from blog.models import Product



class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(basket.sum() for basket in self)
    

    def total_quantity(self):
        return sum(basket.quantity for basket in self)
    




class Basket(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)

    objects = BasketQuerySet.as_manager()


    def __str__(self) -> str:
        return f"{self.user.username} {self.product.name}"
    

    def sum(self):
        return self.product.price * self.quantity
    

