from django.conf.urls import url
from social_api import views

urlpatterns = [
    url(r'^api/v1/auth/$', views.auth),
]