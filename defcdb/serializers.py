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

class DC_researchevent_researchtypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_researchevent_researchtype


class DC_researchevent_institutionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_researchevent_institution


class DC_researchevent_special_analysisSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_researchevent_special_analysis


class DC_site_geographicalreferencesystemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_site_geographicalreferencesystem


class DC_area_areatypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_areatype


class DC_area_settlementtypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_settlementtype


class DC_area_settlementstructureSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_settlementstructure


class DC_area_constructiontypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_constructiontype


class DC_area_buildingtechniqueSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_buildingtechnique


class DC_area_specialfeaturesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_specialfeatures


class DC_area_evidenceofgraveshumanremainsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_evidenceofgraveshumanremains


class DC_area_evidenceofoccupationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_evidenceofoccupation


class DC_area_caverockshelterstypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_caverockshelterstype


class DC_area_rawmaterialSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_rawmaterial


class DC_area_exploitationtypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_exploitationtype


class DC_area_topographySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_topography


class DC_area_mortuaryfeaturesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_mortuaryfeatures


class DC_area_gravetypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_gravetype


class DC_area_typeofhumanremainsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_typeofhumanremains


class DC_area_sexesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_sexes


class DC_area_manipulationofgravesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_area_manipulationofgraves


class DC_finds_typeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_type


class DC_finds_materialSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_material


class DC_finds_amountSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_amount


class DC_finds_small_finds_typeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_small_finds_type


class DC_finds_small_finds_categorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_small_finds_category


class DC_finds_botany_speciesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_botany_species


class DC_finds_animal_remains_speciesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_animal_remains_species


class DC_finds_animal_remains_completenessSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_animal_remains_completeness


class DC_finds_animal_remains_partSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_animal_remains_part


class DC_finds_lithics_debitageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_lithics_debitage


class DC_finds_lithics_modified_toolsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_lithics_modified_tools


class DC_finds_lithics_coreSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_lithics_core


class DC_finds_lithics_technologySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_lithics_technology


class DC_finds_pottery_formSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_pottery_form


class DC_finds_pottery_detailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_pottery_detail


class DC_finds_pottery_decorationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_finds_pottery_decoration


class DC_interpretation_productiontypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_interpretation_productiontype


class DC_interpretation_subsistencetypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_interpretation_subsistencetype


class DC_chronological_systemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_chronological_system


class DC_period_datingmethodSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_period_datingmethod


class DC_period_datedbySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DC_period_datedby



