import os
import rdflib
from django.conf import settings
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS, ConjunctiveGraph
from rdflib.namespace import DC, FOAF, RDFS, XSD
from rdflib.namespace import SKOS
from places.serializer_arche import place_to_arche, inst_to_arche, person_to_arche

ARCHE = Namespace('https://vocabs.acdh.oeaw.ac.at/schema#')
ACDH = Namespace('https://id.acdh.oeaw.ac.at/')
GEONAMES = Namespace('http://www.geonames.org/ontology#')
try:
    base_url = settings.ARCHE_SETTINGS['base_url']
except AttributeError:
    base_url = "https://please/provide/ARCHE-SETTINGS"

LOCATION_PATH = "Y:\OREA_DOKU_PLATTFORM-Thunau_Vers2_aktuell 08 03 2017"


def document_to_arche(itmes):

    """takes queryset of Documents objects and returns an ARCHE rdflib.Graph"""

    g = rdflib.Graph()
    for obj in itmes:
        subject = URIRef('/'.join([base_url, 'document', str(obj.id)]))
        g.add((subject, RDF.type, ARCHE.Resource))
        if obj.filename:
            g.add((subject, ARCHE.hasTitle, Literal(obj.filename)))
        if obj.author.all():
            authors_g = person_to_arche(obj.author.all())
            g = g + authors_g
            for x in obj.author.all():
                temp_a = URIRef('/'.join([base_url, 'person', str(x.id)]))
                g.add((subject, ARCHE.hasCreator, temp_a))
        if obj.curator:
            authors_g = person_to_arche([obj.curator])
            g = g + authors_g
            temp_c = URIRef('/'.join([base_url, 'person', str(obj.curator.id)]))
            g.add((subject, ARCHE.hasMetadataCreator, temp_c))
        if obj.date_digitization:
            g.add((
                subject, ARCHE.hasCreatedDate,
                Literal(obj.date_digitization, datatype=XSD.date))
            )
        if obj.note:
            g.add((subject, ARCHE.hasNote, Literal(obj.note)))
        if obj.content:
            g.add((subject, ARCHE.hasNote, Literal(obj.content)))
        if obj.get_file_location():
            abs_path = os.path.join(LOCATION_PATH, obj.get_file_location())
            g.add((subject, ARCHE.hasLocationPath, Literal(abs_path)))
    return g
