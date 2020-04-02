from django.db import models

# Create your models here.

class TaskContent(models.Model):
    title = models.CharField(max_length=128, default='', verbose_name='任務標題')
    description = models.TextField(blank=True, verbose_name='任務描述')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
