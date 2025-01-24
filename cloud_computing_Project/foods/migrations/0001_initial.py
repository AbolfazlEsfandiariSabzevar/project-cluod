from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',  # تغییر نام مدل به Food
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),  # نام غذا
                ('category', models.CharField(max_length=100, choices=[('Traditional', 'سنتی'), ('Fast Food', 'فست‌فود')])),  # نوع غذا
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),  # قیمت غذا
                ('is_available', models.BooleanField(default=True)),  # وضعیت موجودی
            ],
        ),
    ]
