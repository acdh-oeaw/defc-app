# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import VirtualObject

class VirtualObjectForm(ModelForm):
	class Meta:
		model = VirtualObject
		fields = "__all__"