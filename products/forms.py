# -*- coding: utf-8 -*-
from models import Product, MissingProduct

from django.contrib.auth.models import User

import re


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
        self.error = "Missing fields"
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


class UserCreateForm(object):

    def __init__(self, values):
        self.username = values.get('username', None)
        self.password = values.get('password', None)
        self.email = values.get('email', None)
        self.error = ""

    def has_numbers(self, password):
        return any(char.isdigit() for char in password)

    def validate_password(self, password):
        return (self.has_numbers(password) and len(password) >= 8)

    def validate_email(self, email):
        # Return if the mail is valid
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True

    def is_valid(self):
        if self.username and self.email and self.password:
            if User.objects.all().filter(username=self.username).exists():
                self.error = "The username already exists on db"
                return False
            elif not self.validate_email(self.email):
                self.error = "The email format is not valid"
                return False
            elif not self.validate_password(self.password):
                self.error = "Pass must have 8 characters at least and numbers"
                return False
            elif User.objects.all().filter(email=self.email).exists():
                self.error = "The email already exists on db"
                return False
            else:
                return True
        else:
            self.error = "Missing fields"
            return False

    def save(self):
        user = User.objects.create_user(
            username=self.username, email=self.email, password=self.password)

        return user


class UserUpdateForm(UserCreateForm):

    def __init__(self, values, id):
        super(UserUpdateForm, self).__init__(values)
        self.id = id

    def is_valid(self):
        if self.password:
            if not self.validate_password(self.password):
                self.error = "Pass must have 8 characters at least and numbers"
                return False
        if self.username and self.email:
            user_objects = User.objects.all().filter(username=self.username)
            email_objects = User.objects.all().filter(email=self.email)

            if user_objects.exclude(id=self.id).exists():
                self.error = "The username already exists on db"
                return False
            elif not self.validate_email(self.email):
                self.error = "The email format is not valid"
                return False
            elif email_objects.exclude(id=self.id).exists():
                self.error = "The email already exists on db"
                return False

            else:
                return True
        else:
            self.error = "Missing fields"
            return False

    def update(self):
        u = User.objects.get(id=self.id)
        u.email = self.email
        u.username = self.username

        if self.password:
            u.set_password(self.password)
            u.save()

        return u
