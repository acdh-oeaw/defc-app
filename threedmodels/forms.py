# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Contact, Project, Threedmodel
from defcdb.models import Finds, ResearchEvent

class ThreedmodelForm(ModelForm):
	class Meta:
		model = Threedmodel
		fields = "__all__"

	def __init__(self, *args, **kwargs):
            super(ThreedmodelForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.add_input(Submit('submit', 'Create'))