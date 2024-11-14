from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('restaurants/', views.RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('categories/', views.MenuCategoryListCreate.as_view(), name='menu-category-list-create'),
    path('subcategories/', views.SubCategoryListCreate.as_view(), name='subcategory-list-create'),
    path('dishes/', views.DishListCreate.as_view(), name='dish-list-create'),
]
