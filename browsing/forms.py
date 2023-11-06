from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from defcdb.models import *


class SiteFilterForm(forms.ModelForm):
    

    class Meta:
        model = Site
        fields = ["name"]


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.add_input(Submit("Filter", "Filter"))


class SpecificAreaForm(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SpecificAreaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.add_input(Submit("Filter", "Filter"))
        self.layout = Layout(
            Fieldset(
                "Basic search options",
                # area fields
                "site__province__region__name",
                "site__province",
                "area_type",
                "site__name",
                "period",
                "period__cs_name",
                "period__start_date1_BC",
                "period__end_date1_BC",
                "dating_method",
                "radiocarbon_dated",
                # finds fields
                css_id="basic_search_fields",
            ),
            Fieldset(
                "Advanced search options",
                # area fields
                "settlement_type",
                "settlement_structure",
                "settlement_construction_type",
                "settlement_construction_shape",
                "settlement_building_technique",
                "settlement_special_features",
                "settlement_human_remains",
                "cave_rockshelters_type",
                "cave_rockshelters_human_remains",
                "cave_rockshelters_evidence_of_occupation",
                "quarry_exploitation_type",
                "quarry_raw_material",
                "cemetery_or_grave",
                "cemetery_or_graves_topography",
                "cemetery_or_graves_mortuary_features",
                "grave_number_of_grave",
                "grave_type",
                "grave_type_of_human_remains",
                "grave_estimated_number_of_individuals",
                "grave_age_groups",
                "grave_sexes",
                "grave_number_of_female_sex",
                "grave_number_of_male_sex",
                "grave_number_of_not_specified_sex",
                "grave_manipulations_of_graves",
                css_id="advanced_search_fields",
            ),
        )


class SpecificFindsForm(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SpecificFindsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.add_input(Submit("Filter", "Filter"))
        self.layout = Layout(
            Fieldset(
                "Basic search options",
                # finds fields
                "finds_type",
                "area__site__province",
                "area__site__name",
                "area__area_type",
                "research_event__research_type__name",
                "period",
                "period__cs_name",
                "area__period__start_date1_BC",
                "area__period__end_date1_BC",
                "amount",
                "material",
                "confidence",
                css_id="basic_search_fields",
            ),
            Fieldset(
                "Advanced search options",
                # finds fields
                "small_finds_category",
                "small_finds_type",
                "botany_species",
                "animal_remains_species",
                "animal_remains_completeness",
                "animal_remains_part",
                "lithics_technology",
                "lithics_industry",
                "lithics_core_shape",
                "lithics_retouched_tools",
                "lithics_unretouched_tools",
                "lithics_raw_material",
                "obsidian",
                "obsidian_amount",
                "pottery_form",
                "pottery_detail",
                "pottery_decoration",
                "pottery_type",
                css_id="advanced_search_fields",
            ),
        )


class SpecificMapForm(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SpecificMapForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.add_input(Submit("Filter", "Search", css_class="btn-crispy-search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options",
                # site fields
                "name",
                "province__region__name",
                "province",
                "topography__name",
                "period",
                "period__cs_name",
                "area__period__start_date1_BC",
                "area__period__end_date1_BC",
                css_id="basic_search_fields",
            ),
            Fieldset(
                "Area search options",
                # area fields
                "area__area_type",
                "area__dating_method",
                "area__radiocarbon_dated",
                "area__settlement_type",
                "area__settlement_structure",
                "area__settlement_construction_type",
                "area__settlement_construction_shape",
                "area__settlement_building_technique",
                "area__settlement_special_features",
                "area__settlement_human_remains",
                "area__cave_rockshelters_type",
                "area__cave_rockshelters_human_remains",
                "area__cave_rockshelters_evidence_of_occupation",
                "area__quarry_exploitation_type",
                "area__quarry_raw_material",
                "area__cemetery_or_grave",
                "area__cemetery_or_graves_topography",
                "area__cemetery_or_graves_mortuary_features",
                "area__grave_number_of_graves",
                "area__grave_type",
                "area__grave_type_of_human_remains",
                "area__grave_estimated_number_of_individuals",
                "area__grave_age_groups",
                "area__grave_sexes",
                "area__grave_number_of_female_sex",
                "area__grave_number_of_male_sex",
                "area__grave_number_of_not_specified_sex",
                "area__grave_manipulations_of_graves",
                css_id="area_search_fields",
            ),
            Fieldset(
                "Finds search options",
                # finds fields
                "area__finds__finds_type",
                "area__finds__amount",
                "area__finds__material",
                "area__finds__confidence",
                "area__finds__small_finds_category",
                "area__finds__small_finds_type",
                "area__finds__botany_species",
                "area__finds__animal_remains_species",
                "area__finds__animal_remains_completeness",
                "area__finds__animal_remains_part",
                "area__finds__lithics_technology",
                "area__finds__lithics_industry",
                "area__finds__lithics_core_shape",
                "area__finds__lithics_retouched_tools",
                "area__finds__lithics_unretouched_tools",
                "area__finds__lithics_raw_material",
                "area__finds__obsidian",
                "area__finds__obsidian_amount",
                "area__finds__pottery_form",
                "area__finds__pottery_detail",
                "area__finds__pottery_decoration",
                "area__finds__pottery_type",
                css_id="finds_search_fields",
            ),
        )
