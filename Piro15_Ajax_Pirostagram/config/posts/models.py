from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to = "post_image/%Y/%m/%d/",null=True,blank = True)  
    like = models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('posts:post_list')

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
