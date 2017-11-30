import os
import urllib.parse
from django.db import models
from django.core.urlresolvers import reverse
from vocabs.models import SkosConcept
from idprovider.models import IdProvider
from places.models import Place, Person, Institution
from bib.models import Book
from arche.models import Collection


class Document(IdProvider):
    legacy_id = models.CharField(max_length=300, blank=True, verbose_name='ID')
    path = models.CharField(max_length=300, blank=True, verbose_name="Dateipfad")
    filename = models.CharField(max_length=300, blank=True, verbose_name="Dateiname")
    entry_order = models.CharField(
        max_length=300, blank=True, verbose_name="Ordnungskriterium/Eingabe"
    )
    medium = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name='medium', verbose_name="Medium"
    )
    analogue_format = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="analogue_format",
        verbose_name="Analoges Format"
    )
    author = models.ManyToManyField(
        Person, blank=True, related_name="author", verbose_name="Autor"
    )
    institution = models.ManyToManyField(
        Institution, blank=True, verbose_name="Institution", related_name="institution_document"
    )
    date_analogue = models.CharField(max_length=300, blank=True, verbose_name="Analoges Datum")
    date_digitization = models.DateField(
        auto_now=False, blank=True, null=True, verbose_name="Datum der Digitalisierung"
    )
    digital_format = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="digital_format",
        verbose_name="Speicherformat"
    )
    note = models.TextField(blank=True, verbose_name="Anmerkung")
    content = models.TextField(blank=True, verbose_name="Inhalt")
    topic_group = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="topic_group",
        verbose_name="Gruppe"
    )
    combination = models.CharField(max_length=300, blank=True, verbose_name="Kombination")
    location_id = models.CharField(max_length=300, blank=True, verbose_name="Fundnummer in FDB")
    place_of_origin = models.ForeignKey(Place, blank=True, null=True, verbose_name="KG/Areal")
    location_digitized_object = models.CharField(
        max_length=300, blank=True, verbose_name="Aufbewahrung Datei"
    )
    location_analogue = models.CharField(max_length=300, blank=True, verbose_name="Standort analog")
    curator = models.ForeignKey(
        Person, blank=True, null=True, verbose_name="Bearbeiter Digitalisierung"
    )
    filesize = models.FloatField(blank=True, null=True, verbose_name="Dateigröße KB")
    place_digizization = models.ForeignKey(
        Institution, blank=True, null=True, related_name="place_digizization",
        verbose_name="Ort der Digitalisierung"
    )
    reference = models.ManyToManyField(Book, blank=True, verbose_name="Literaturzitate")
    amendments = models.TextField(blank=True, verbose_name="Ergänzungen")
    in_collection = models.ForeignKey(
        Collection, blank=True, null=True, verbose_name="acdh:partOf",
        help_text="Resource is located in collection", related_name="children"
    )

    def get_file_name(self):
        if self.filename and self.digital_format.pref_label:
            return ".".join([self.filename, self.digital_format.pref_label.lower()])
        else:
            return None

    def get_file_location(self):
        if self.path and self.get_file_name():
            file_loc = os.path.join(
                self.path.replace('_', '\\'), self.get_file_name()
            )
            return file_loc
        else:
            return None

    def get_file_uri(self):
        if self.path and self.get_file_name():
            file_loc = "/".join(
                [self.path.replace('_', '/'), self.get_file_name()]
            )
            return "https://id.acdh.oeaw.ac.at/thunau/collection/{}".format(
                urllib.parse.quote(file_loc, safe="")
                )
        else:
            return None

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_documents')

    @classmethod
    def get_arche_dump(self):
        return reverse('browsing:rdf_documents')

    def get_next(self):
        next = Document.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Document.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        return "{}".format(self.filename)

    def get_absolute_url(self):
        return reverse('documents:document_detail', kwargs={'pk': self.id})
