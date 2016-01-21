# -*- coding: utf-8 -*-
from django import forms
import autocomplete_light
#autocomplete_light.autodiscover()
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from django.utils.translation import ugettext_lazy as _
from .autocomplete_light_registry import BookAutocomplete, InstitutionAutocomplete, ProjectleaderAutocomplete, NameAutocomplete
from .models import Area, ResearchEvent, Site, Finds, Interpretation, DC_researchevent_institution, Name
from bib.models import Book


class NameForm(autocomplete_light.ModelForm):
	class Meta:
		model=Name
		fields = "__all__"

	def __init__(self, *args, **kwargs):
			super(NameForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper()
			self.helper.add_input(Submit('submit','Create'))


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
		fields="__all__"

	def __init__(self, *args, **kwargs):
			super(AreaForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper()
			self.helper.add_input(Submit('submit','Create'))


class ResearcheventForm(autocomplete_light.ModelForm):
	project_leader = forms.CharField(required=False,
		widget=autocomplete_light.TextWidget('ResearchEventProjectleaderAutocomplete'),
		help_text="Leader of the research project.")
	# project_leader = autocomplete_light.ChoiceField(ResearchEvent.objects.all(),
	# 	required = False,
	# 	widget = autocomplete_light.TextWidget('ProjectleaderAutocomplete'))
#if user inputs a not yet existing Project Leader, the whole object won´t be stored in the db
	
	class Meta:
		model = ResearchEvent
		fields = '__all__'

	def __init__(self, *args, **kwargs):
			super(ResearcheventForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper()
			self.helper.add_input(Submit('submit','Create'))


class FindsForm(autocomplete_light.ModelForm, forms.ModelForm):
	reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete'),
		help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the selected small finds.")
	research_event = forms.ModelMultipleChoiceField(queryset=ResearchEvent.objects.all(),
		help_text="Project/ Research the finds are related to.")

	class Meta:
		model = Finds
		fields = '__all__'

	def __init__(self, *args, **kwargs):
			super(FindsForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper()
			self.helper.add_input(Submit('submit','Create'))


class SiteForm(autocomplete_light.ModelForm):
	reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete'),
		help_text="Bibliographic and web-based references to publications and other relevant information on the site.")

	class Meta:
		model = Site
		fields = '__all__'

	def __init__(self, *args, **kwargs):
			super(SiteForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper()
			self.helper.add_input(Submit('submit','Create'))


class InterpretationForm(autocomplete_light.ModelForm):
	reference = autocomplete_light.ModelMultipleChoiceField(Book.objects.all(),
		required = False,
		widget =autocomplete_light.MultipleChoiceWidget('BookAutocomplete'))

	class Meta:
		model = Interpretation
		fields = '__all__'

	def __init__(self, *args, **kwargs):
			super(InterpretationForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper()
			self.helper.add_input(Submit('submit','Create'))



class form_user_login(forms.Form):
	username = forms.CharField(label='Username',widget=forms.TextInput)
	password = forms.CharField(label='Password',widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(form_user_login, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit','Login'))

