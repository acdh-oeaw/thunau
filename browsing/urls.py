from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'places/$', views.PlaceListView.as_view(), name='browse_places'),
    url(r'documents/$', views.DocumentListView.as_view(), name='browse_documents'),
]
