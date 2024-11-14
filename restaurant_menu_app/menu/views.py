from rest_framework import generics
from .models import Restaurant, MenuCategory, SubCategory, Dish
from .serializers import RestaurantSerializer, MenuCategorySerializer, SubCategorySerializer, DishSerializer


class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuCategoryListCreate(generics.ListCreateAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class SubCategoryListCreate(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class DishListCreate(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
