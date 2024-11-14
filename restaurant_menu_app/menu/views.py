from rest_framework import generics
from .models import Restaurant, MenuCategory, SubCategory, Dish
from .serializers import RestaurantSerializer, MenuCategorySerializer, SubCategorySerializer, DishSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MenuCategoryListCreate(generics.ListCreateAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SubCategoryListCreate(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DishListCreate(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
