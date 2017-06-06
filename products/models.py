# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

MEDITION_CHOICES = (
    ('gr', 'gramos'),
    ('kg', 'kilogramos'),
    ('ltrs', 'litros')
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    medition = models.CharField(
        max_length=5,
        choices=MEDITION_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name + " " + str(self.quantity) + (
            self.medition if self.medition else '')

    def as_json(self):
        data = {
            "name": self.name,
            "description": self.description,
            "quantity": self.quantity
        }
        return data
