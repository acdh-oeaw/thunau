import django_tables2 as tables
from django_tables2.utils import A
from places.models import *
from documents.models import Document


class InstitutionTable(tables.Table):
    written_name = tables.LinkColumn(
        'places:institution_detail',
        args=[A('pk')], verbose_name='Name'
    )
    location = tables.Column()

    class Meta:
        model = Institution
        sequence = ('id', 'written_name',)
        attrs = {"class": "table table-responsive table-hover"}


class PlaceTable(tables.Table):
    name = tables.LinkColumn(
        'places:place_detail',
        args=[A('pk')], verbose_name='Name'
    )
    part_of = tables.Column()

    class Meta:
        model = Place
        sequence = ('id', 'name',)
        attrs = {"class": "table table-responsive table-hover"}


class DocumentTable(tables.Table):
    filename = tables.LinkColumn(
        'documents:document_detail',
        args=[A('pk')], verbose_name='Name'
    )
    part_of = tables.Column()

    class Meta:
        model = Document
        sequence = ('id', 'filename',)
        attrs = {"class": "table table-responsive table-hover"}
