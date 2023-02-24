from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField, ManyToManyField
from django.utils import timezone
from cloudinary.models import CloudinaryField


class ImageModel(models.Model):
    img = CloudinaryField('image', null=True)
    id = models.CharField(max_length=16, primary_key=True)


class Paperclip(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=200)
    publish_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=16, primary_key=True)


class Author(models.Model):
    paperclip = models.ForeignKey(Paperclip, on_delete=models.CASCADE)  # 关联发布会id
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)  # 手机号
    email = models.EmailField(primary_key=True)  # 邮箱
    sign = models.BooleanField()  # 签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    class Meta:
        unique_together = ('phone', 'paperclip')
        ordering = ['email']

    def __str__(self):
        return self.realname


class Comment(models.Model):
    paperclip = models.ForeignKey(Paperclip, on_delete=models.CASCADE)  # 关联发布会id
    contents = models.CharField(max_length=200)
    publish_time = models.DateTimeField()
    id = models.CharField(max_length=16, primary_key=True)
    phone = models.CharField(max_length=16)  # 手机号

    class Meta:
        unique_together = ('phone', 'paperclip')
        ordering = ['-id']

    def __str__(self):
        return self.id


class PetPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    # image field
    images = ManyToManyField(ImageModel)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
