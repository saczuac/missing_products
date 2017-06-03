# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.quantity

    def as_json(self):
        data = {
            "name": self.name,
            "description": self.description,
            "quantity": self.quantity
        }
        return data
