from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)  # 공백도 ok
    price = models.PositiveIntegerField()  # 양수
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
