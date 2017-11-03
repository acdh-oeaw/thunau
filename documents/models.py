from django.db import models
from django.core.urlresolvers import reverse
from vocabs.models import SkosConcept
from idprovider.models import IdProvider
from places.models import Place, Person, Institution
from bib.models import Book


class Document(IdProvider):
    legacy_id = models.CharField(max_length=300, blank=True, verbose_name='ID')
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
    path = models.CharField(max_length=300, blank=True, verbose_name="Dateipfad")
    amendments = models.TextField(blank=True, verbose_name="Ergänzungen")

    def __str__(self):
        return "{}".format(self.filename)

    def get_absolute_url(self):
        return reverse('documents:document_detail', kwargs={'pk': self.id})
