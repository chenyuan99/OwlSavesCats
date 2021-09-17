from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Paperclip(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=200)
    publish_time = models.DateTimeField() 
    create_time = models.DateTimeField(auto_now=True)
    pid = models.CharField(max_length=16)

    # def __str__(self):
    #     return self.title

class Author(models.Model):
    paperclip = models.ForeignKey(Paperclip, on_delete=models.CASCADE)  # 关联发布会id
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)     # 手机号
    email = models.EmailField()                 # 邮箱
    sign = models.BooleanField()                # 签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    class Meta:
        unique_together = ('phone', 'paperclip')
        ordering = ['-id']

    def __str__(self):
        return self.realname

class Comment(models.Model):
    paperclip = models.ForeignKey(Paperclip, on_delete=models.CASCADE)  # 关联发布会id
    contents = models.CharField(max_length=200)
    publish_time = models.DateTimeField() 
    cid = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)     # 手机号

    class Meta:
        unique_together = ('phone', 'paperclip')
        ordering = ['-id']

    def __str__(self):
        return self.cid

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title