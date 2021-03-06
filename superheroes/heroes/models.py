from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=100)

    def __str__(self):
        return self.name
