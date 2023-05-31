from django.db import models
from accounts.models import MyUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='category/%Y/%m/%d')


    def __str__(self) -> str:
        return f"Category name: {self.name}"


class Product(models.Model):
    SIZE_CHOICES = [
        ("XS", 'XS'),
        ("S", 'S'),
        ("M", 'M'),
        ("L", 'L'),
        ("XL", 'XL'),
    ]
    COLOR_CHOICES = [
        ('B', 'Black'),
        ('W', 'White'),
        ('R', 'Red'),
        ('Bl', 'Blue'),
        ('G', 'Green'),
    ]
    RATING_CHOICES = [
        (1, '1 Звезда'),
        (2, '2 Звезды'),
        (3, '3 Звезды'),
        (4, '4 Звезды'),
        (5, '5 Звезд'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    desc = models.TextField()
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/%Y/%m/%d')
    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    rating = models.IntegerField(choices=RATING_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"Product name: {self.name}"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"Review:{self.name} Product {self.product}"
        


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self) -> str:
        return f"Contact: {self.name}"
    