# -*- coding: utf-8 -*-
from django import forms
import autocomplete_light
autocomplete_light.autodiscover()
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from django.utils.translation import ugettext_lazy as _
from .autocomplete_light_registry import BookAutocomplete, InstitutionAutocomplete, ProjectleaderAutocomplete
from .models import Area, ResearchEvent, Site, Period, Finds, Interpretation, DC_researchevent_institution
from bib.models import Book

class AreaForm(autocomplete_light.ModelForm):
	period_reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete')
		)
	reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete')
		)
	
	class Meta:
		model = Area
		#exclude =['reference', 'period_reference']
		fields=["site", "area_type", "area_nr","stratigraphical_unit_id",
		"geographical_reference", "period", "c14_calibrated",
		"c14_absolute_from","c14_absolute_to","period_reference",
		"period_comment","settlement_type","settlement_structure",
		"settlement_construction_type", "settlement_building_technique",
		"settlement_special_features", "settlement_human_remains",
		"cave_rockshelters_type", "cave_rockshelters_evidence_of_graves_human_remains",
		"cave_rockshelters_evidence_of_occupation","quarry_exploitation_type",
		"quarry_raw_material", "cemetery_or_grave", "cemetery_or_graves_topography",
		"cemetery_or_graves_mortuary_features", "grave_number_of_graves",
		"grave_type", "grave_type_of_human_remains",
		"grave_estimated_number_of_individuals", "grave_age_groups",
		"grave_sexes", "grave_number_of_female_sex",
		"grave_number_of_male_sex", "grave_number_of_not_specified_sex",
		"grave_manipulations_of_graves", "reference", "description",
		"comment"]


class ResearcheventForm(autocomplete_light.ModelForm):
	# project_leader = autocomplete_light.ChoiceField(ResearchEvent.objects.all(),
	# 	required = False,
	# 	widget =autocomplete_light.TextWidget('ProjectleaderAutocomplete'))
#if user inputs a not yet existing Project Leader, the whole object won´t be stored in the db
	
	class Meta:
		model = ResearchEvent
		fields = '__all__'

class FindsForm(autocomplete_light.ModelForm):
	reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete'))

	class Meta:
		model = Finds
		fields = '__all__'

class SiteForm(autocomplete_light.ModelForm):
	reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete'))

	class Meta:
		model = Site
		fields = '__all__'

class InterpretationForm(autocomplete_light.ModelForm):
	reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete'))

	class Meta:
		model = Interpretation
		fields = '__all__'


class form_user_login(forms.Form):
	username = forms.CharField(label='Username',widget=forms.TextInput)
	password = forms.CharField(label='Password',widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(form_user_login, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit','Login'))

