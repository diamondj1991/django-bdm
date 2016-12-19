from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    category_thumbnail = models.FileField()

    def __str__(self):
        return self.name


class Type(models.Model):

    YES = 'Y'
    NO = 'N'
    SHIPPABLE_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type_thumbnail = models.FileField()
    era = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    short_description = models.CharField(max_length=50, default="None")
    description = models.TextField()
    shippable = models.CharField(
        max_length=1,
        choices=SHIPPABLE_CHOICES,
        default=NO
    )

    def __str__(self):
        return self.color + " - " + self.era + "\n\n" + self.description
