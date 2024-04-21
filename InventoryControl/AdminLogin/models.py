from django.db import models

# Create your models here.
class adminn (models.Model):
    userid = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.userid
