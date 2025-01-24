from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodViewSet  # تغییر به FoodViewSet

router = DefaultRouter()
router.register(r'foods', FoodViewSet)  # تغییر به foods

urlpatterns = [
    path('', include(router.urls)),
]
