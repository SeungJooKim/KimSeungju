from django.db import models
from django.shortcuts import reverse
class Tool(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('DevTools:tool_detail', args=[self.pk])
