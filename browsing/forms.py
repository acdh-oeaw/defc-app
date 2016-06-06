import autocomplete_light
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from defcdb.models import Site, Area
from .autocomplete_light_registry import SiteAutocomplete


class SiteFilterForm(forms.ModelForm):
    name = autocomplete_light.ModelMultipleChoiceField(
        Site.objects.all(),
        required=False,
        widget=autocomplete_light.MultipleChoiceWidget('SiteAutocomplete')
    )

    class Meta:
        model = Site
        fields = ['name']


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.add_input(Submit('Filter', 'Filter'))
