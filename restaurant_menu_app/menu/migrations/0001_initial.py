# Generated by Django 5.1.3 on 2024-11-14 15:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dish_photos/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='menu.dish')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='restaurant_photos/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_categories', to='menu.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='subcategory_images/')),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='menu.menucategory')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='menu.subcategory'),
        ),
    ]