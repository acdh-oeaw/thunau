from django.db import models
from places.models import Person, Institution


class RepoObject(models.Model):
    has_title = models.CharField(
        max_length=250, blank=True, verbose_name="acdh:hasTitle",
        help_text="Title or name of Collection."
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="acdh:hasDescription",
        help_text="A verbose description of certain aspects of an entity. \
        This is the most generic property, use more specific sub-properties where applicable."
    )

    class Meta:
        abstract = True


class Collection(RepoObject):
    part_of = models.ForeignKey(
        'Collection', blank=True, null=True, verbose_name="acdh:isPartOf",
        help_text="Indicates A is a part of aggregate B, \
        e. g. elements of a series, items of a collection.", related_name="has_part"
    )
    has_contributor = models.ManyToManyField(
        Person, blank=True, verbose_name="acdh:hasContributor",
        help_text="Agent (person, group, organisation) (B) who was actively involved in \
        creating/curating/editing a Resource, a Collection or in a Project (A).",
        related_name="contributes_to_collection"
    )

    def __str__(self):
        return "{}".format(self.has_title)


class Project(RepoObject):
    has_principal = models.ManyToManyField(
        Person, blank=True, verbose_name="acdh:hasContributor",
        help_text="Person officially designated as head of project team or subproject \
        team instrumental in the work necessary to development of the resource.",
        related_name="is_principal"
    )
    has_contributor = models.ManyToManyField(
        Person, blank=True, verbose_name="acdh:hasContributor",
        help_text="Agent (person, group, organisation) (B) who was actively involved in \
        creating/curating/editing a Resource, a Collection or in a Project (A).",
        related_name="contributes_to_project"
    )
    has_start_date = models.DateField(
        blank=True, null=True, verbose_name="acdh:hasStartDate",
        help_text="Indicates the start date of a Project."
    )
    has_end_date = models.DateField(
        blank=True, null=True, verbose_name="acdh:hasEndtDate",
        help_text="Indicates the end date of a Project."
    )
    has_funder = models.ManyToManyField(
        Institution, blank=True, verbose_name="acdh:hasFunder",
        help_text="Organisation (B) which provided funding for the project (A).",
        related_name="is_funding"
    )
    related_collection = models.ManyToManyField(
        Collection, blank=True, verbose_name="acdh:hasRelatedCollection",
        help_text="Indication of a project (B) associated with this resource or collection (A).",
        related_name="has_related_project"
    )

    def __str__(self):
        return "{}".format(self.has_title)
