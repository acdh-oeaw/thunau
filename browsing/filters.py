import django_filters
from dal import autocomplete
from places.models import Place, AlternativeName, Institution, Person
from documents.models import Document
from vocabs.models import SkosConcept

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class AlternativeNameListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=AlternativeName._meta.get_field('name').help_text,
        label=AlternativeName._meta.get_field('name').verbose_name
        )

    class Meta:
        model = AlternativeName
        fields = "__all__"


class PersonListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('name').help_text,
        label=Person._meta.get_field('name').verbose_name
        )
    forename = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('forename').help_text,
        label=Person._meta.get_field('forename').verbose_name
        )
    written_name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('written_name').help_text,
        label=Person._meta.get_field('written_name').verbose_name
        )
    acad_title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('acad_title').help_text,
        label=Person._meta.get_field('acad_title').verbose_name
        )
    alt_names = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('alt_names').help_text,
        label=Person._meta.get_field('alt_names').verbose_name
        )
    belongs_to_institution = django_filters.ModelMultipleChoiceFilter(
        queryset=Institution.objects.all(),
        help_text=Person._meta.get_field('belongs_to_institution').help_text,
        label=Person._meta.get_field('belongs_to_institution').verbose_name
        )

    class Meta:
        model = Person
        fields = "__all__"


class InstitutionListFilter(django_filters.FilterSet):
    written_name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('written_name').help_text,
        label=Institution._meta.get_field('written_name').verbose_name
        )
    alt_names = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('alt_names').help_text,
        label=Institution._meta.get_field('alt_names').verbose_name
        )
    authority_url = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('authority_url').help_text,
        label=Institution._meta.get_field('authority_url').verbose_name
        )
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Institution._meta.get_field('location').help_text,
        label=Institution._meta.get_field('location').verbose_name
        )

    class Meta:
        model = Institution
        fields = [
            'id', 'written_name', 'authority_url', 'location'
        ]


class DocumentListFilter(django_filters.FilterSet):
    filename = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Document._meta.get_field('filename').help_text,
        label=Document._meta.get_field('filename').verbose_name
        )
    path = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Document._meta.get_field('path').help_text,
        label=Document._meta.get_field('path').verbose_name
        )
    entry_order = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Document._meta.get_field('entry_order').help_text,
        label=Document._meta.get_field('entry_order').verbose_name
        )
    medium = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title="Medium"),
        help_text=Document._meta.get_field('medium').help_text,
        label=Document._meta.get_field('medium').verbose_name
        )
    analogue_format = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title="Analoges Format"),
        help_text=Document._meta.get_field('analogue_format').help_text,
        label=Document._meta.get_field('analogue_format').verbose_name
        )
    institution = django_filters.ModelMultipleChoiceFilter(
        queryset=Institution.objects.all(),
        help_text=Document._meta.get_field('institution').help_text,
        label=Document._meta.get_field('institution').verbose_name
        )
    digital_format = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title="Speicherformat"),
        help_text=Document._meta.get_field('digital_format').help_text,
        label=Document._meta.get_field('digital_format').verbose_name
        )

    class Meta:
        model = Document
        fields = [
            'id', 'filename'
        ]


class PlaceListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('name').help_text,
        label=Place._meta.get_field('name').verbose_name
        )
    geonames_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('geonames_id').help_text,
        label=Place._meta.get_field('geonames_id').verbose_name
        )
    alternative_name = django_filters.ModelMultipleChoiceFilter(
        queryset=AlternativeName.objects.all(),
        help_text=Place._meta.get_field('alternative_name').help_text,
        label=Place._meta.get_field('alternative_name').verbose_name
        )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Place._meta.get_field('part_of').help_text,
        label=Place._meta.get_field('part_of').verbose_name
        )

    class Meta:
        model = Place
        fields = [
            'id'
        ]
