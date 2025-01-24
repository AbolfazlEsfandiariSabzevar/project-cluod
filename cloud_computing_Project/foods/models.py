from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)  # نام غذا
    category = models.CharField(max_length=100, choices=[('Traditional', 'سنتی'), ('Fast Food', 'فست‌فود')])  # نوع غذا
    price = models.DecimalField(max_digits=8, decimal_places=2)  # قیمت غذا
    is_available = models.BooleanField(default=True)  # وضعیت موجودی

    def __str__(self):
        return f"{self.name} - {self.category}"
