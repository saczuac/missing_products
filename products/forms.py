# -*- coding: utf-8 -*-
from models import Product


class ProductCreateForm():

    def __init__(self, values):
        self.name = values.get('name', None)
        self.description = values.get('description', None)
        self.quantity = values.get('quantity', None)
        self.error = ""

    def is_valid(self):
        if self.name and self.description and self.quantity:
            if Product.objects.all().filter(name=self.name).count():
                self.error = "El Producto ya existe, elija otro nombre"
                return False
            return True
        self.error = "Todos los campos son obligatorios"
        return False

    def save(self):
        prod = Product(
            name=self.name,
            description=self.description,
            quantity=self.quantity)

        prod.save()
        return prod


class ProductUpdateForm(ProductCreateForm, object):

    def __init__(self, values, id):
        super(ProductUpdateForm, self).__init__(values)
        self.id = id

    def is_valid(self):
        if self.name and self.description and self.quantity:
            objects = Product.objects.all().filter(
                name=self.name).exclude(id=self.id)
            if objects.count():
                self.error = "El Producto ya existe, elija otro nombre"
                return False
            return True
        self.error = "Todos los campos son obligatorios"
        return False

    def update(self):
        prod = Product.objects.get(pk=self.id)
        prod.description = self.description
        prod.name = self.name
        prod.quantity = self.quantity
        prod.save()
        return prod
