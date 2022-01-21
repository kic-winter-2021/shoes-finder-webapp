from django.db import models


class Shoes(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    name = models.CharField(max_length=100)
    brandcode = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()  # retail_price
    imagepath = models.CharField(max_length=100)
    searchword = models.CharField(max_length=100)

    def __str__(self):
        return self.name + self.id
