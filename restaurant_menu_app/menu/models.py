from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    cover_photo = models.ImageField(upload_to='restaurant_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='main_categories')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='subcategory_images/', blank=True, null=True)
    parent_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dish_photos/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name
