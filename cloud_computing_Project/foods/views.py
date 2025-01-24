from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Food  # تغییر به مدل غذا
from .serializers import FoodSerializer  # تغییر به سریالایزر غذا

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()  # تغییر به queryset مربوط به غذا
    serializer_class = FoodSerializer  # استفاده از سریالایزر جدید غذا
