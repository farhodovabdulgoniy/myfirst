# Generated by Django 3.2.9 on 2021-11-12 02:20

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField(max_length=255)),
                ('message', models.TextField(max_length=255)),
                ('status', models.CharField(choices=[('Yangi', 'New'), ('Uqildi', 'Read'), ('Yopilgan', 'Closed')], default='New', max_length=15)),
                ('ip', models.CharField(blank=True, max_length=222)),
                ('note', models.CharField(blank=True, max_length=222)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('question', models.CharField(max_length=255)),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField()),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('Muhim', 'Muhim'), ('False', 'Mavjud emas')], default='True', max_length=15)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='lic_images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='post_images/')),
                ('author', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('keywords', models.CharField(max_length=222)),
                ('description', models.CharField(max_length=222)),
                ('country', models.CharField(blank=True, max_length=222)),
                ('address', models.CharField(blank=True, max_length=222)),
                ('phone', models.CharField(blank=True, max_length=222)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(blank=True, max_length=222)),
                ('instagram', models.CharField(blank=True, max_length=222)),
                ('twitter', models.CharField(blank=True, max_length=222)),
                ('youtube', models.CharField(blank=True, max_length=222)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField()),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LicenseImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='lic_images/')),
                ('lic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.license')),
            ],
        ),
    ]
