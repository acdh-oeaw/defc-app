import autocomplete_light
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field
from defcdb.models import *
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
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                #area fields
                'site__province__region__name',
                'site__province',
                'area_type',
                'site__name',
                'period',
                'period__cs_name',
                'period__start_date1_BC', 
                'period__end_date1_BC', 
                'dating_method', 
                'radiocarbon_dated', 
                #finds fields
                'finds_type',
                'area__site__province',
                'area__site__name',
                'area__area_type',
                'research_event__research_type__name',
                # 'period',
                # 'period__cs_name', 
                'area__period__start_date1_BC', 
                'area__period__end_date1_BC', 
                'amount',
                'material', 
                'confidence', 
                css_id="basic_search_fields"),
            Fieldset(
                'Advanced search options',
                #area fields
                'settlement_type',
                'settlement_structure',
                'settlement_construction_type',
                'settlement_building_technique',
                'settlement_special_features',
                'settlement_human_remains',
                'cave_rockshelters_type',
                'cave_rockshelters_human_remains',
                'cave_rockshelters_evidence_of_occupation',
                'quarry_exploitation_type',
                'quarry_raw_material',
                'cemetery_or_grave',
                'cemetery_or_graves_topography',
                'cemetery_or_graves_mortuary_features',
                'grave_number_of_grave',
                'grave_type',
                'grave_type_of_human_remains',
                'grave_estimated_number_of_individuals',
                'grave_age_groups',
                'grave_sexes',
                'grave_number_of_female_sex',
                'grave_number_of_male_sex',
                'grave_number_of_not_specified_sex',
                'grave_manipulations_of_graves',
                #finds fields
                'small_finds_category',
                'small_finds_type',
                'botany_species',
                'animal_remains_species',
                'animal_remains_completeness',
                'animal_remains_part',
                'lithics_technology',
                'lithics_industry',
                'lithics_core_shape',
                'lithics_retouched_tools',
                'lithics_raw_material',
                'obsidian',
                'obsidian_amount',
                'pottery_form',
                'pottery_detail',
                'pottery_decoration',
                css_id="advanced_search_fields"
                ),
        )



