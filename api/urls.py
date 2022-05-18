from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^auth/login$', views.LoginAPIView.as_view(), name='api-login'),
    # url(r'^auth/login', obtain_jwt_token, name='api-token-login'),
    url(r'^auth/signup$', views.RegisterAPIView.as_view(), name='api-register'),
    url(r'^auth/set_password$', views.SetPasswordAPIView.as_view(), name='api-set-password'),
    url(r'^book/previous', views.BookPreviousAPIView.as_view(), name='api-previous-book'),
    url(r'^book/cancel', views.BookCancelAPIView.as_view(), name='api-cancel-book'),
    url(r'^book/storage', views.BookStorageAPIView.as_view(), name='api-storage-book'),
    url(r'^book/storehouse', views.BookStoreHouseAPIView.as_view(), name='api-storehouse-book'),
    url(r'^book/accept', views.BookAcceptAPIView.as_view(), name='api-accept-book'),
    url(r'^book/promo_code', views.BookPromoCodeAPIView.as_view(), name='api-promo-code-book'),
    url(r'^book/complete', views.BookCompleteAPIView.as_view(), name='api-accept-book'),
    url(r'^book/current', views.BookCurrentAPIView.as_view(), name='api-current-book'),
    url(r'^book', views.BookCreateAPIView.as_view(), name='api-customer-book'),
    url(r'^profile$', views.ProfileUpdateAPIView.as_view(), name='api-profile-update'),
]
