from django.conf.urls import url
from . import views

app_name = 'product'

urlpatterns = [
    # <-- Products views URLs starts -->
    url(r'product/$',
        views.ProductListView.as_view(),
        name='product-list'),

    url(r'product/create/$',
        views.ProductCreateView.as_view(),
        name='product-create'),

    url(r'product/update/(?P<pk>[0-9]+)/$',
        views.ProductUpdateView.as_view(),
        name='product-update'),

    url(r'product/delete/(?P<pk>[0-9]+)/$',
        views.ProductDeleteView.as_view(),
        name='product-delete'),

    url(r'^product/(?P<pk>\d+)/$',
        views.ProductGetView.as_view(),
        name='get-product'),
    # <-- products views URLs ends -->
]
