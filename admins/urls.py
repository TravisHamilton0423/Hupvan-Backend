from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^book/$', views.list_book, name='book-list'),
    url(r'^driver/$', views.list_driver, name='driver-list'),

    url(r'^store_house/$', views.list_store_house, name='store_house-list'),
    url(r'^store_house/create/$', views.create_store_house, name='store_house-create'),
    url(r'^store_house/(?P<store_house_id>\d+)/edit/$', views.edit_store_house, name='store_house-edit'),
    url(r'^store_house/(?P<store_house_id>\d+)/delete/$', views.delete_store_house, name='store_house-delete'),

    url(r'^storage/$', views.list_storage, name='promo_code-list'),
    url(r'^storage/create/$', views.create_storage, name='promo_code-create'),
    url(r'^storage/(?P<storage_id>\d+)/edit/$', views.edit_storage, name='promo_code-edit'),
    url(r'^storage/(?P<storage_id>\d+)/delete/$', views.delete_storage, name='promo_code-delete'),

    url(r'^promo_code/$', views.list_promo_code, name='promo_code-list'),
    url(r'^promo_code/create/$', views.create_promo_code, name='promo_code-create'),
    url(r'^promo_code/(?P<promo_id>\d+)/edit/$', views.edit_promo_code, name='promo_code-edit'),
    url(r'^promo_code/(?P<promo_id>\d+)/delete/$', views.delete_promo_code, name='promo_code-delete'),

    url(r'^driver/(?P<driver_id>\d+)/edit/$', views.edit_driver, name='driver-edit'),
    url(r'^driver/(?P<driver_id>\d+)/delete/$', views.delete_driver, name='driver-delete'),

    url(r'^customer/$', views.list_customer, name='customer-list'),
    url(r'^customer/(?P<customer_id>\d+)/delete/$', views.delete_customer, name='customer-delete'),
]
