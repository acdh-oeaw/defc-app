# -*- coding: utf-8 -*-
from django import forms
import autocomplete_light
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from django.utils.translation import ugettext_lazy as _
from .autocomplete_light_registry import BookAutocomplete
from .models import Area


class AreaForm(autocomplete_light.ModelForm):
	reference = forms.CharField(required = False,
		label = 'Reference',
		widget =autocomplete_light.TextWidget('BookAutocomplete')
		)
	period_reference = forms.CharField(required = False,
		label = 'Periode Reference',
		widget =autocomplete_light.TextWidget('BookAutocomplete')
		)
	class Meta:
		model = Area
		exclude =['reference', 'period_reference']
#		widgets = {'reference' : forms.TextInput}


class form_user_login(forms.Form):
	username = forms.CharField(label='Username',widget=forms.TextInput)
	password = forms.CharField(label='Password',widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(form_user_login, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit','Login'))

