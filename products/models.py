# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

MEDITION_CHOICES = (
    ('gr', 'gramos'),
    ('kg', 'kilogramos'),
    ('ltrs', 'litros')
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    medition = models.CharField(
        max_length=5,
        choices=MEDITION_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name + " " + (self.medition or '')

    def as_json(self):
        data = {
            "name": self.name,
            "description": self.description,
            "medition": self.medition or ''
        }
        return data


class MissingProduct(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.product.name + " --> " + str(self.quantity)

    def as_json(self):
        data = {
            "quantity": self.quantity,
            "product": self.product.as_json()
        }
        return data
