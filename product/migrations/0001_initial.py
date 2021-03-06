# Generated by Django 3.2.9 on 2021-11-12 02:20

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222, unique=True)),
                ('keywords', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='category_images/')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222, unique=True)),
                ('keywords', models.CharField(max_length=222, unique=True)),
                ('description', models.CharField(blank=True, max_length=222)),
                ('image', models.ImageField(blank=True, upload_to='product_main/')),
                ('price', models.FloatField()),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], max_length=15)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=55)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('rate', models.IntegerField(default=1)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], default='True', max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
