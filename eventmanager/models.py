from django.db import models


# Register your models here.
class Events(models.Model):
    created_date = models.DateField(auto_now_add = False)
    title = models.CharField(max_length=100, default = "Dummy Event")
    description = models.TextField()
