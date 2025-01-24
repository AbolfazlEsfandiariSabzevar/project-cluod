from rest_framework import serializers
from .models import Food  # مدل مرتبط با غذا

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food  # مدل جدید غذا
        fields = '__all__'  # تمام فیلدهای مدل غذا
