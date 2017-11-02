from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.response import Response
from .api_renderers import GeoJsonRenderer
from .models import *
from .serializers import *
from bib.models import Book


class GeoJsonViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Site.objects.all()
        serializer = GeoJsonSerializer(queryset, many=True)
        return Response(serializer.data)

    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (GeoJsonRenderer,)


class DC_finds_lithics_raw_materialViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_lithics_raw_material.objects.all()
    serializer_class = DC_finds_lithics_raw_materialSerializer


class DC_finds_lithics_retouched_toolsViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_lithics_retouched_tools.objects.all()
    serializer_class = DC_finds_lithics_retouched_toolsSerializer


class DC_finds_lithics_unretouched_toolsViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_lithics_unretouched_tools.objects.all()
    serializer_class = DC_finds_lithics_unretouched_toolsSerializer


class DC_finds_lithics_core_shapeViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_lithics_core_shape.objects.all()
    serializer_class = DC_finds_lithics_core_shapeSerializer


class DC_finds_lithics_industryViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_lithics_industry.objects.all()
    serializer_class = DC_finds_lithics_industrySerializer


class DC_area_agegroupsViewSet(viewsets.ModelViewSet):
    queryset = DC_area_agegroups.objects.all()
    serializer_class = DC_area_agegroupsSerializer


class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


class DC_site_topographyViewSet(viewsets.ModelViewSet):
    queryset = DC_site_topography.objects.all()
    serializer_class = DC_site_topographySerializer


class DC_countryViewSet(viewsets.ModelViewSet):
    queryset = DC_country.objects.all()
    serializer_class = DC_countrySerializer


class DC_regionViewSet(viewsets.ModelViewSet):
    queryset = DC_region.objects.all()
    serializer_class = DC_regionSerializer


class DC_provinceViewSet(viewsets.ModelViewSet):
    queryset = DC_province.objects.all()
    serializer_class = DC_provinceSerializer


class DC_researchevent_researchtypeViewSet(viewsets.ModelViewSet):
    queryset = DC_researchevent_researchtype.objects.all()
    serializer_class = DC_researchevent_researchtypeSerializer


class DC_researchevent_institutionViewSet(viewsets.ModelViewSet):
    queryset = DC_researchevent_institution.objects.all()
    serializer_class = DC_researchevent_institutionSerializer


class DC_researchevent_special_analysisViewSet(viewsets.ModelViewSet):
    queryset = DC_researchevent_special_analysis.objects.all()
    serializer_class = DC_researchevent_special_analysisSerializer


class DC_site_geographicalreferencesystemViewSet(viewsets.ModelViewSet):
    queryset = DC_site_geographicalreferencesystem.objects.all()
    serializer_class = DC_site_geographicalreferencesystemSerializer


class DC_area_areatypeViewSet(viewsets.ModelViewSet):
    queryset = DC_area_areatype.objects.all()
    serializer_class = DC_area_areatypeSerializer


class DC_area_settlementtypeViewSet(viewsets.ModelViewSet):
    queryset = DC_area_settlementtype.objects.all()
    serializer_class = DC_area_settlementtypeSerializer


class DC_area_settlementstructureViewSet(viewsets.ModelViewSet):
    queryset = DC_area_settlementstructure.objects.all()
    serializer_class = DC_area_settlementstructureSerializer


class DC_area_constructiontypeViewSet(viewsets.ModelViewSet):
    queryset = DC_area_constructiontype.objects.all()
    serializer_class = DC_area_constructiontypeSerializer


class DC_area_constructionshapeViewSet(viewsets.ModelViewSet):
    queryset = DC_area_constructionshape.objects.all()
    serializer_class = DC_area_constructionshapeSerializer


class DC_area_buildingtechniqueViewSet(viewsets.ModelViewSet):
    queryset = DC_area_buildingtechnique.objects.all()
    serializer_class = DC_area_buildingtechniqueSerializer


class DC_area_specialfeaturesViewSet(viewsets.ModelViewSet):
    queryset = DC_area_specialfeatures.objects.all()
    serializer_class = DC_area_specialfeaturesSerializer


class DC_area_evidenceofgraveshumanremainsViewSet(viewsets.ModelViewSet):
    queryset = DC_area_evidenceofgraveshumanremains.objects.all()
    serializer_class = DC_area_evidenceofgraveshumanremainsSerializer


class DC_area_evidenceofoccupationViewSet(viewsets.ModelViewSet):
    queryset = DC_area_evidenceofoccupation.objects.all()
    serializer_class = DC_area_evidenceofoccupationSerializer


class DC_area_caverockshelterstypeViewSet(viewsets.ModelViewSet):
    queryset = DC_area_caverockshelterstype.objects.all()
    serializer_class = DC_area_caverockshelterstypeSerializer


class DC_area_rawmaterialViewSet(viewsets.ModelViewSet):
    queryset = DC_area_rawmaterial.objects.all()
    serializer_class = DC_area_rawmaterialSerializer


class DC_area_exploitationtypeViewSet(viewsets.ModelViewSet):
    queryset = DC_area_exploitationtype.objects.all()
    serializer_class = DC_area_exploitationtypeSerializer


class DC_area_topographyViewSet(viewsets.ModelViewSet):
    queryset = DC_area_topography.objects.all()
    serializer_class = DC_area_topographySerializer


class DC_area_mortuaryfeaturesViewSet(viewsets.ModelViewSet):
    queryset = DC_area_mortuaryfeatures.objects.all()
    serializer_class = DC_area_mortuaryfeaturesSerializer


class DC_area_gravetypeViewSet(viewsets.ModelViewSet):
    queryset = DC_area_gravetype.objects.all()
    serializer_class = DC_area_gravetypeSerializer


class DC_area_typeofhumanremainsViewSet(viewsets.ModelViewSet):
    queryset = DC_area_typeofhumanremains.objects.all()
    serializer_class = DC_area_typeofhumanremainsSerializer


class DC_area_sexesViewSet(viewsets.ModelViewSet):
    queryset = DC_area_sexes.objects.all()
    serializer_class = DC_area_sexesSerializer


class DC_area_manipulationofgravesViewSet(viewsets.ModelViewSet):
    queryset = DC_area_manipulationofgraves.objects.all()
    serializer_class = DC_area_manipulationofgravesSerializer


class DC_finds_typeViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_type.objects.all()
    serializer_class = DC_finds_typeSerializer


class DC_finds_materialViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_material.objects.all()
    serializer_class = DC_finds_materialSerializer


class DC_finds_amountViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_amount.objects.all()
    serializer_class = DC_finds_amountSerializer


class DC_finds_small_finds_typeViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_small_finds_type.objects.all()
    serializer_class = DC_finds_small_finds_typeSerializer


class DC_finds_small_finds_categoryViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_small_finds_category.objects.all()
    serializer_class = DC_finds_small_finds_categorySerializer


class DC_finds_botany_speciesViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_botany_species.objects.all()
    serializer_class = DC_finds_botany_speciesSerializer


class DC_finds_animal_remains_speciesViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_animal_remains_species.objects.all()
    serializer_class = DC_finds_animal_remains_speciesSerializer


class DC_finds_animal_remains_completenessViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_animal_remains_completeness.objects.all()
    serializer_class = DC_finds_animal_remains_completenessSerializer


class DC_finds_animal_remains_partViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_animal_remains_part.objects.all()
    serializer_class = DC_finds_animal_remains_partSerializer


class DC_finds_lithics_technologyViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_lithics_technology.objects.all()
    serializer_class = DC_finds_lithics_technologySerializer


class DC_finds_pottery_formViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_pottery_form.objects.all()
    serializer_class = DC_finds_pottery_formSerializer


class DC_finds_pottery_detailViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_pottery_detail.objects.all()
    serializer_class = DC_finds_pottery_detailSerializer


class DC_finds_pottery_decorationViewSet(viewsets.ModelViewSet):
    queryset = DC_finds_pottery_decoration.objects.all()
    serializer_class = DC_finds_pottery_decorationSerializer


class DC_interpretation_productiontypeViewSet(viewsets.ModelViewSet):
    queryset = DC_interpretation_productiontype.objects.all()
    serializer_class = DC_interpretation_productiontypeSerializer


class DC_interpretation_subsistencetypeViewSet(viewsets.ModelViewSet):
    queryset = DC_interpretation_subsistencetype.objects.all()
    serializer_class = DC_interpretation_subsistencetypeSerializer


class DC_chronological_systemViewSet(viewsets.ModelViewSet):
    queryset = DC_chronological_system.objects.all()
    serializer_class = DC_chronological_systemSerializer


class DC_period_datingmethodViewSet(viewsets.ModelViewSet):
    queryset = DC_period_datingmethod.objects.all()
    serializer_class = DC_period_datingmethodSerializer


class DC_period_datedbyViewSet(viewsets.ModelViewSet):
    queryset = DC_period_datedby.objects.all()
    serializer_class = DC_period_datedbySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ResearchEventViewSet(viewsets.ModelViewSet):
    queryset = ResearchEvent.objects.all()
    serializer_class = ResearchEventSerializer


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class FindsViewSet(viewsets.ModelViewSet):
    queryset = Finds.objects.all()
    serializer_class = FindsSerializer


class InterpretationViewSet(viewsets.ModelViewSet):
    queryset = Interpretation.objects.all()
    serializer_class = InterpretationSerializer


class DC_site_coordinatesource(viewsets.ModelViewSet):
    queryset = DC_site_coordinatesource.objects.all()
    serializer_class = DC_site_coordinatesourceSerializer
