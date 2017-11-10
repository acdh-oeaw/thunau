from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'places/$', views.PlaceListView.as_view(), name='browse_places'),
    url(r'institutions/$', views.InstitutionListView.as_view(), name='browse_institutions'),
    url(r'documents/$', views.DocumentListView.as_view(), name='browse_documents'),
]
