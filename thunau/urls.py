from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from places.apis_views import PlaceViewSet, GeoJsonViewSet

from vocabs import api_views

router = routers.DefaultRouter()
router.register(r'geojson', GeoJsonViewSet, base_name='places')
router.register(r'skoslabels', api_views.SkosLabelViewSet)
router.register(r'skosnamespaces', api_views.SkosNamespaceViewSet)
router.register(r'skosconceptschemes', api_views.SkosConceptSchemeViewSet)
router.register(r'skosconcepts', api_views.SkosConceptViewSet)
router.register(r'places', PlaceViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^arche/', include('arche.urls', namespace='arche')),
    url(r'^documents/', include('documents.urls', namespace='documents')),
    url(r'^browsing/', include('browsing.urls', namespace='browsing')),
    url(r'^sparql/', include('sparql.urls', namespace='sparql')),
    url(r'^vocabs/', include('vocabs.urls', namespace='vocabs')),
    url(r'^vocabs-ac/', include('vocabs.dal_urls', namespace='vocabs-ac')),
    url(r'^datamodel/', include('django_spaghetti.urls', namespace='datamodel')),
    url(r'^places/', include('places.urls', namespace='places')),
    url(r'^', include('webpage.urls', namespace='webpage')),
]
