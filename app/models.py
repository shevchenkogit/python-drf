from django.db import models

class Api(models.Model):
    
    name = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return self.task
