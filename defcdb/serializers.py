from django.conf import settings
from rest_framework import serializers
from .models import *
from bib.models import Book

try:
    base_url = settings.CURRENT_BASE_URL
except AttributeError:
    base_url = 'https://defc.acdh.oeaw.ac.at'


class GeoJsonSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):
        geonames_base = "http://www.geonames.org/"
        alt_names = [{'name': x.name} for x in obj.alternative_name.all()]
        for x in obj.alias_name.all():
            alt_names.append({'name': x.name})
        broad_matches = []
        try:
            geonames_id = obj.province.authorityfile_id
        except AttributeError:
            geonames_id = None

        if geonames_id:
            broad_matches.append(geonames_base+geonames_id)
        if obj.longitude:
            geojson = {
                "links": {
                    "broad_matches": broad_matches,
                },
                "descriptions": [
                    {"description": obj.description, "language": "EN"}
                ],
                "title": obj.name,
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(obj.longitude), float(obj.latitude)]
                    },
                "uri": base_url + obj.get_absolute_url(),
                "id": obj.pk,
                "names": alt_names,
                "properties": {
                    "name": obj.name
                }
            }
            return geojson
        else:
            return None


class DC_finds_lithics_raw_materialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_finds_lithics_raw_material


class DC_finds_lithics_retouched_toolsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_finds_lithics_retouched_tools


class DC_finds_lithics_unretouched_toolsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_finds_lithics_unretouched_tools


class DC_finds_lithics_core_shapeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_finds_lithics_core_shape


class DC_finds_lithics_industrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_finds_lithics_industry


class DC_area_agegroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_area_agegroups


class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Name


class DC_site_topographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_site_topography


class DC_site_coordinatesourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_site_coordinatesource


class DC_countrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_country


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


class DC_area_constructionshapeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DC_area_constructionshape


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


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book


class ResearchEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResearchEvent


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area


class FindsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finds


class InterpretationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interpretation
