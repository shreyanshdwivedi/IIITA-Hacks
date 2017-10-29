"""digitalmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from products.views import create_view, update_view, detail_view, detail_slug_view, list_view, form_view
# from products.views import (
#         ProductCreateView,
#         ProductDetailView,
#         ProductListView,
#         ProductUpdateView,
#         CreateView
#         )

urlpatterns = [
    # url(r'^$', ProductListView.as_view(), name='product_list_view'),
    url(r'^form/$', form_view, name='form_view'),
    url(r'^create/$', create_view, name='create_view'),
    # url(r'^ad_create/$', CreateView.as_view(), name='ad_create'),
    url(r'^detail/(?P<object_id>\d+)/edit/$', update_view, name='update_view'),
    url(r'^detail/(?P<object_id>\d+)/$', detail_view, name='detail_view'),
    url(r'^detail/(?P<slug>[\w-]+)/$', detail_slug_view, name='detail_slug_view'),
    url(r'^list/$', list_view, name='list_view'),
    # url(r'^add/$', ProductCreateView.as_view(), name='product_create_view'),
    # url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail_view'),
    # url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='product_detail_slug_view'),
    # url(r'^(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='product_update_view'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(), name='product_update_view'),


]
