from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', views.DocumentDetailView.as_view(), name='document_detail'),
    url(r'^create/$', views.DocumentCreate.as_view(), name='document_create'),
    url(r'^update/(?P<pk>[0-9]+)$', views.DocumentUpdate.as_view(), name='document_update'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.DocumentDelete.as_view(), name='document_delete'),
]
