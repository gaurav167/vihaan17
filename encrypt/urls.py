from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'save/$', views.data_encrypt, name='sub_data'),
    url(r'^retrieve/$', views.retrieve, name='ret_data'),
]
