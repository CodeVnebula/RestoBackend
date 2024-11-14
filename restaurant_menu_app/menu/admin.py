from django.contrib import admin
from .models import Restaurant, MenuCategory, SubCategory, Dish, Ingredient

# Register your models here.

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']
    search_fields = ['name', 'address', 'phone']
    

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant']
    search_fields = ['name', 'restaurant__name']
    

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category']
    search_fields = ['name', 'parent_category__name']
    

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'subcategory']
    search_fields = ['name', 'price', 'subcategory__name']
    

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'dish']
    search_fields = ['name', 'dish__name']
