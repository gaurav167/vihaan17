from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.home, name='index'),
	url(r'^upload/$' ,views.upload ,name = 'upload'),
	url(r'^view_image/(?P<_id>\w+)/$' ,views.view_image ,name = 'view_upload'),
	url(r'^upload_img/$', views.generic, name='generic'),
	url(r'^view_img/$', views.elements, name='elements'),
	url(r'^gallery/$', views.gallery, name='gallery'),
	url(r'^signup/$', views.signup, name='signup'),
]