# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Product

from utils.serializers.serializers import JSONResponseMixin

from forms import ProductCreateForm, ProductUpdateForm

from utils.views.templates import CreateTemplateView
from utils.views.templates import UpdateTemplateView
from utils.views.templates import DeleteTemplateView


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
