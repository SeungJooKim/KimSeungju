from django.db import models
from django.shortcuts import reverse


class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "idea_image/%Y/%m/%d/",null=True,blank = True)  
    desc = models.TextField()
    interest = models.PositiveIntegerField(default =0)
    devtool = models.ForeignKey(
        "DevTools.Tool", on_delete=models.CASCADE, related_name="ideas"
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('Ideas:idea_detail', args=[self.pk])
