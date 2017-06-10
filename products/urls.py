from django.conf.urls import url

from django.contrib.auth import views as auth_views

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

    # <-- Missing Products views URLs starts -->
    url(r'^missing-products/from/(?P<userpk>\d+)/$',
        views.MissingProductsFromView.as_view(),
        name='get-missing-products-from'),

    url(r'missing-products/create/$',
        views.MissingProductsCreateView.as_view(),
        name='missing-products-create'),

    url(r'missing-products/update/(?P<pk>[0-9]+)/$',
        views.MissingProductsUpdateView.as_view(),
        name='missing-products-update'),

    url(r'missing-products/delete/(?P<pk>[0-9]+)/$',
        views.MissingProductsDeleteView.as_view(),
        name='missing-products-delete'),

    url(r'^missing-products/(?P<pk>\d+)/$',
        views.MissingProductsGetView.as_view(),
        name='get-missing-products'),
    # <-- Missing Products URLs ends -->

    # <-- User views URLs starts -->
    url(r'^user/login/$', auth_views.LoginView.as_view()),

    url(r'user/create/$',
        views.UserCreateView.as_view(),
        name='user-create'),

    url(r'user/update/$',
        views.UserUpdateView.as_view(),
        name='user-update'),

    url(r'user/delete/$',
        views.UserDeleteView.as_view(),
        name='user-delete'),

    # <-- User views URLs ends -->
]
