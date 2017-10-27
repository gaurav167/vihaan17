from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'form/$', views.data_encrypt(), name='data_save_form')
]
