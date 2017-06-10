# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Product, MissingProduct

from utils.serializers.serializers import JSONResponseMixin

from forms import ProductCreateForm, ProductUpdateForm
from forms import MissingProductCreateForm, MissingProductUpdateForm
from forms import UserUpdateForm, UserCreateForm

from utils.views.templates import CreateTemplateView
from utils.views.templates import UpdateTemplateView
from utils.views.templates import DeleteTemplateView

from django.contrib.auth.models import User


class ProductCreateView(CreateTemplateView):

    def __init__(self):
        self.with_request = False
        model = Product
        template_name = ""
        form_class = ProductCreateForm
        ctx = {}
        super(self.__class__, self).__init__(
            model, template_name, form_class, ctx)


class ProductUpdateView(UpdateTemplateView):

    def __init__(self):
        self.with_request = False
        model = Product
        template_name = ""
        form_class = ProductUpdateForm
        message_not_exists = "The product does not exist"
        element_name = "product"
        super(self.__class__, self).__init__(
            model,
            template_name,
            form_class,
            message_not_exists,
            element_name
        )


class ProductDeleteView(DeleteTemplateView):

    def __init__(self):
        model = Product
        message_not_exists = "The product does not exist"
        super(self.__class__, self).__init__(
            model,
            message_not_exists,
        )


class ProductListView(JSONResponseMixin):
    model = Product
    message_error = 'No products in db'


class ProductGetView(JSONResponseMixin):
    model = Product
    message_error = 'Can not find product in db'

    def get_query(self, request=None, *args, **kwargs):
        return self.model.objects.filter(pk=kwargs['pk'])


class MissingProductsFromView(JSONResponseMixin):
    model = MissingProduct
    message_error = 'Can not find user in db'

    def get_query(self, request=None, *args, **kwargs):
        return self.model.objects.filter(user__pk=kwargs['userpk'])


class MissingProductsCreateView(CreateTemplateView):

    def __init__(self):
        self.with_request = False
        model = MissingProduct
        template_name = ""
        form_class = MissingProductCreateForm
        ctx = {}
        super(self.__class__, self).__init__(
            model, template_name, form_class, ctx)


class MissingProductsUpdateView(UpdateTemplateView):

    def __init__(self):
        self.with_request = False
        model = MissingProduct
        template_name = ""
        form_class = MissingProductUpdateForm
        message_not_exists = "The Missingproducts does not exist"
        element_name = "missing_product"
        super(self.__class__, self).__init__(
            model,
            template_name,
            form_class,
            message_not_exists,
            element_name
        )


class MissingProductsDeleteView(DeleteTemplateView):

    def __init__(self):
        model = MissingProduct
        message_not_exists = "The Missingproducts does not exist"
        super(self.__class__, self).__init__(
            model,
            message_not_exists,
        )


class MissingProductsListView(JSONResponseMixin):
    model = MissingProduct
    message_error = 'No Missingproductss in db'


class MissingProductsGetView(JSONResponseMixin):
    model = MissingProduct
    message_error = 'Can not find product in db'

    def get_query(self, request=None, *args, **kwargs):
        return self.model.objects.filter(pk=kwargs['pk'])


class UserCreateView(CreateTemplateView):

    def __init__(self):
        self.with_request = False
        model = User
        template_name = ""
        form_class = UserCreateForm
        ctx = {}
        super(self.__class__, self).__init__(
            model, template_name, form_class, ctx)


class UserUpdateView(JSONResponseMixin):
    model = User
    message_error = 'You are not logued in'

    def get_post(self, request, post):
        if request.user.is_authenticated():
            u = User.objects.get(username=request.user)
            form = UserUpdateForm(post, u.id)

            if form.is_valid():
                user = form.update()
                return user
            return form.error


class UserDeleteView(JSONResponseMixin):
    model = User
    message_error = 'You are not logued in'

    def get_post(self, request, post):
        if request.user.is_authenticated():
            u = User.objects.get(username=request.user)
            u.delete()
            return True
