from typing import Text
from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):  # 모델 객체를 정의
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # 글자수가 제한된 텍스트 정의
    text = models.TextField()  # 글자수 제한 없는 텍스트 정의

    created_date = models.DateTimeField(  # 날짜와 시간을 의미
        default=timezone.now
    )

    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
