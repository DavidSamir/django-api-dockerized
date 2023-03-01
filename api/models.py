from django.db import models


class Scrapper(models.Model):
    res = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

