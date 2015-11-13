# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *

class DC_countrySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_country
		#fields = "__all__"

class DC_regionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_region
		#fields = "__all__"