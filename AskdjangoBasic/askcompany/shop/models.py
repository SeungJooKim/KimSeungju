from django.db import models
from django.conf import settings
from askcompany.utils import uuid_upload_to
# 파일은 FileField, ImageField 많이 사용
# 문자열은 CharField, TextField, SlugField 등
# 날짜/ 시간 :DateTimeField, DateField, TimeField 등
# 이메일 : EmailField

# Relationship Types
# ForeignKey
# ManyToManyField
# OneToOneField

# 옵션
# blank , null , db_index, default,choices, validator


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)  # 공백도 ok
    price = models.PositiveIntegerField()  # 양수
    photo = models.ImageField(blank = True, upload_to = uuid_upload_to)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.pk}> {self.name}'


# class Post(models.Model):
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


"""
from django.conf immport settings
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASECADE)
    title = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(allow_unicode= True, db_index= True) # ModelAdmin.prepopulated_fields 편리
    desc = models.TextField(blank = True)
    image = models.ImageField(blank = True)
    is_publish = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now =True)
"""
