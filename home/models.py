from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Setting(models.Model):

    title = models.CharField(max_length=222)
    keywords = models.CharField(max_length=222)
    description = models.CharField(max_length=222)
    country = models.CharField(max_length=222,blank=True)
    address = models.CharField(max_length=222,blank=True)
    phone = models.CharField(max_length=222, blank=True)
    email = models.EmailField()
    facebook = models.CharField(max_length=222,blank=True)
    instagram = models.CharField(max_length=222,blank=True)
    twitter = models.CharField(max_length=222,blank=True)
    youtube = models.CharField(max_length=222,blank=True)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 


class Post(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='post_images/')
    author = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class License(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='lic_images/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title   


class LicenseImages(models.Model):

    lic = models.ForeignKey(License, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True,upload_to='lic_images/')

    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):

    STATUS = (
        ('Yangi','New'),
        ('Uqildi','Read'),
        ('Yopilgan','Closed'),
    )

    name = models.CharField(max_length=222)
    email = models.EmailField()
    subject = models.TextField(max_length=255)
    message = models.TextField(max_length=255)
    status = models.CharField(max_length=15,default='New',choices=STATUS)
    ip = models.CharField(max_length=222,blank=True)
    note = models.CharField(max_length=222,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 


class FAQ(models.Model):

    STATUS = (
        ('True','Mavjud'),
        ('Muhim','Muhim'),
        ('False','Mavjud emas'),
    )

    ordernumber = models.IntegerField()
    question = models.CharField(max_length=255)
    answer = RichTextUploadingField()
    status = models.CharField(max_length=15,choices=STATUS,default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question