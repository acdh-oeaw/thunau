from django.db import models
from django.core.urlresolvers import reverse
from idprovider.models import IdProvider


class AlternativeName(IdProvider):
    name = models.CharField(max_length=250, blank=True, help_text="Alternative Name")

    def __str__(self):
        return self.name


class Place(IdProvider):
    PLACE_TYPES = (
        ("city", "city"),
        ("country", "country")
    )

    """Holds information about places."""
    name = models.CharField(
        max_length=250, blank=True, help_text="Normalized name"
    )
    alternative_name = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        help_text="Alternative names"
    )
    geonames_id = models.CharField(
        max_length=50, blank=True,
        help_text="GND-ID"
    )
    lat = models.DecimalField(
        max_digits=20, decimal_places=12,
        blank=True, null=True
    )
    lng = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True
    )
    part_of = models.ForeignKey(
        "Place", null=True, blank=True, help_text="A place (country) this place is part of."
    )
    place_type = models.CharField(choices=PLACE_TYPES, null=True, blank=True, max_length=50)

    @classmethod
    def get_listview_url(self):
        return reverse('places:place_list')

    def get_next(self):
        next = Place.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Place.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse('place:place_detail', kwargs={'pk': self.id})

    def __str__(self):
        return "{}".format(self.name)


class Institution(IdProvider):
    legacy_id = models.CharField(max_length=300, blank=True)
    written_name = models.CharField(max_length=300, blank=True)
    authority_url = models.CharField(max_length=300, blank=True)
    alt_names = models.CharField(max_length=300, blank=True)
    abbreviation = models.CharField(max_length=300, blank=True)
    location = models.ForeignKey(Place, blank=True, null=True)
    parent_institution = models.ForeignKey('Institution', blank=True, null=True)
    comment = models.TextField(blank=True)

    def get_next(self):
        next = Institution.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Institution.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        return "{}".format(self.name)


class Person(IdProvider):
    legacy_id = models.CharField(max_length=300, blank=True)
    written_name = models.CharField(max_length=300, blank=True)
    forename = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300, blank=True)
    acad_title = models.CharField(max_length=300, blank=True)
    alt_names = models.CharField(max_length=300, blank=True)
    belongs_to_institution = models.ForeignKey(Institution, blank=True, null=True)
    authority_url = models.CharField(max_length=300, blank=True)
    comment = models.TextField(blank=True)

    def get_next(self):
        next = Person.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Person.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        return "{}".format(self.name)
