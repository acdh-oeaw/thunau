from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import *


class GenericFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))


class AlternativeNameFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AlternativeNameFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'name',
                ),
            )
        )


class PersonFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PersonFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'name',
                    'forename',
                    'written_name',
                    css_id="basic_search_fields"
                ),
                AccordionGroup(
                    'Advanced search',
                    'acad_title',
                    'alt_names',
                    'authority_url',
                    'belongs_to_institution',
                    css_id="more"
                    ),
                )
            )


class InstitutionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InstitutionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'written_name',
                    'alt_names',
                    css_id="basic_search_fields"
                ),
                AccordionGroup(
                    'Advanced search'
                    'authority_url',
                    'location',
                    css_id="more"
                    ),
                )
            )


class PlaceFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PlaceFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'name',
                    'alternative_name',
                    css_id="basic_search_fields"
                ),
                AccordionGroup(
                    'Advanced search'
                    'geonames_id',
                    'part_of',
                    css_id="more"
                    ),
                )
            )


class DocumentFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(DocumentFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'filename',
                    'digital_format',
                    'path',
                    'entry_order',
                    css_id="basic_search_fields"
                ),
                AccordionGroup(
                    'Advanced search',
                    'institution',
                    'medium',
                    'analogue_format',
                    css_id="more"
                    ),
                )
            )
