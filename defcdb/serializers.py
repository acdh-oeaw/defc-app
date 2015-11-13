# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *

class DC_countrySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_country


class DC_regionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_region


class DC_regionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_region


class DC_provinceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_province