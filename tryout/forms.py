# -*- coding: utf-8 -*-
from django import forms
import autocomplete_light
from defcdb.autocomplete_light_registry import BookAutocomplete, InstitutionAutocomplete, ProjectleaderAutocomplete, NameAutocomplete
from .models import AreaTry
from bib.models import Book


class AreaTryForm(autocomplete_light.ModelForm):
	period_reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete')
		)
	reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete')
		)
	
	class Meta:
		model = AreaTry
		#exclude =['reference', 'period_reference']
		fields="__all__"

