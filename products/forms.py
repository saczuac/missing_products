# -*- coding: utf-8 -*-
from models import Product, MissingProduct

from django.contrib.auth.models import User


class ProductCreateForm():

    def __init__(self, values):
        self.name = values.get('name', None)
        self.description = values.get('description', None)
        self.medition = values.get('medition', None)
        self.error = ""

    def is_valid(self):
        if self.name and self.description and self.medition:
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
            medition=self.medition)

        prod.save()
        return prod


class ProductUpdateForm(ProductCreateForm, object):

    def __init__(self, values, id):
        super(ProductUpdateForm, self).__init__(values)
        self.id = id

    def is_valid(self):
        if self.name and self.description and self.medition:
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
        prod.medition = self.medition
        prod.save()
        return prod


class MissingProductCreateForm():

    def __init__(self, values):
        self.quantity = values.get('quantity', None)
        self.user = values.get('user', None)
        self.product = values.get('product', None)
        self.error = ""

    def is_valid(self):
        if self.product and self.user and self.quantity:
            objects = MissingProduct.objects.all().filter(
                user__pk=self.user).filter(product__pk=self.product)

            if objects.count():
                self.error = "El MissingProducto ya existe, elija otro"
                return False
            return True
        self.error = "Todos los campos son obligatorios"
        return False

    def save(self):
        user = User.objects.get(pk=self.user)
        product = Product.objects.get(pk=self.product)
        missing_product = MissingProduct(
            user=user,
            product=product,
            quantity=self.quantity)

        missing_product.save()
        return missing_product


class MissingProductUpdateForm(MissingProductCreateForm, object):

    def __init__(self, values, id):
        super(MissingProductUpdateForm, self).__init__(values)
        self.id = id

    def is_valid(self):
        if self.product and self.user and self.quantity:
            objects = MissingProduct.objects.all().filter(
                user__pk=self.user).filter(
                product__pk=self.product).exclude(id=self.id)

            if objects.count():
                self.error = "El MissingProducto ya existe, elija otro"
                return False
            return True
        self.error = "Todos los campos son obligatorios"
        return False

    def update(self):
        missing_product = MissingProduct.objects.get(pk=self.id)
        user = User.objects.get(pk=self.user)
        product = Product.objects.get(pk=self.product)
        missing_product.product = product
        missing_product.user = user
        missing_product.quantity = self.quantity
        missing_product.save()
        return missing_product
