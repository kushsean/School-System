from django.db import models


class Designation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
