from django.conf.urls import url
from . import views

app_name = 'product'

urlpatterns = [
    # <-- Products views URLs starts -->
    url(r'product/$',
        views.productListView.as_view(),
        name='product-list'),

    url(r'product/create/$',
        views.productCreateView.as_view(),
        name='product-create'),

    url(r'product/update/(?P<pk>[0-9]+)/$',
        views.productUpdateView.as_view(),
        name='product-update'),

    url(r'product/delete/(?P<pk>[0-9]+)/$',
        views.productDeleteView.as_view(),
        name='product-delete'),

    url(r'^product/(?P<pk>\d+)/$',
        views.productGetView.as_view(),
        name='get-product'),
    # <-- products views URLs ends -->
]
