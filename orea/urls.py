# -*- coding: utf-8 -*-
from django.conf.urls import include, url
import autocomplete_light.shortcuts as al
al.autodiscover()
from rest_framework import routers
from django.contrib import admin
from orea.settings import base

from defcdb import views

router = routers.DefaultRouter()
router.register(r'dc_country', views.DC_countryViewSet)
router.register(r'dc_region', views.DC_regionViewSet)
router.register(r'dc_province', views.DC_provinceViewSet)
router.register(r'dc_researchevent_researchtype', views.DC_researchevent_researchtypeViewSet)
router.register(r'dc_researchevent_institution', views.DC_researchevent_institutionViewSet)
router.register(r'dc_researchevent_special_analysis', views.DC_researchevent_special_analysisViewSet)
router.register(r'dc_site_geographicalreferencesystem', views.DC_site_geographicalreferencesystemViewSet)
router.register(r'dc_area_areatype', views.DC_area_areatypeViewSet)
router.register(r'dc_area_settlementtype', views.DC_area_settlementtypeViewSet)
router.register(r'dc_area_settlementstructure', views.DC_area_settlementstructureViewSet)
router.register(r'dc_area_constructiontype', views.DC_area_constructiontypeViewSet)
router.register(r'dc_area_buildingtechnique', views.DC_area_buildingtechniqueViewSet)
router.register(r'dc_area_specialfeatures', views.DC_area_specialfeaturesViewSet)
router.register(r'dc_area_evidenceofgraveshumanremains', views.DC_area_evidenceofgraveshumanremainsViewSet)
router.register(r'dc_area_evidenceofoccupation', views.DC_area_evidenceofoccupationViewSet)
router.register(r'dc_area_caverockshelterstype', views.DC_area_caverockshelterstypeViewSet)
router.register(r'dc_area_rawmaterial', views.DC_area_rawmaterialViewSet)
router.register(r'dc_area_exploitationtype', views.DC_area_exploitationtypeViewSet)
router.register(r'dc_area_topography', views.DC_area_topographyViewSet)
router.register(r'dc_area_mortuaryfeatures', views.DC_area_mortuaryfeaturesViewSet)
router.register(r'dc_area_gravetype', views.DC_area_gravetypeViewSet)
router.register(r'dc_area_typeofhumanremains', views.DC_area_typeofhumanremainsViewSet)
router.register(r'dc_area_sexes', views.DC_area_sexesViewSet)
router.register(r'dc_area_manipulationofgraves', views.DC_area_manipulationofgravesViewSet)
router.register(r'dc_finds_type', views.DC_finds_typeViewSet)
router.register(r'dc_finds_material', views.DC_finds_materialViewSet)
router.register(r'dc_finds_amount', views.DC_finds_amountViewSet)
router.register(r'dc_finds_small_finds_type', views.DC_finds_small_finds_typeViewSet)
router.register(r'dc_finds_small_finds_category', views.DC_finds_small_finds_categoryViewSet)
router.register(r'dc_finds_botany_species', views.DC_finds_botany_speciesViewSet)
router.register(r'dc_finds_animal_remains_species', views.DC_finds_animal_remains_speciesViewSet)
router.register(r'dc_finds_animal_remains_completeness', views.DC_finds_animal_remains_completenessViewSet)
router.register(r'dc_finds_animal_remains_part', views.DC_finds_animal_remains_partViewSet)
router.register(r'dc_finds_lithics_debitage', views.DC_finds_lithics_debitageViewSet)
router.register(r'dc_finds_lithics_modified_tools', views.DC_finds_lithics_modified_toolsViewSet)
router.register(r'dc_finds_lithics_core', views.DC_finds_lithics_coreViewSet)
router.register(r'dc_finds_lithics_technology', views.DC_finds_lithics_technologyViewSet)
router.register(r'dc_finds_pottery_form', views.DC_finds_pottery_formViewSet)
router.register(r'dc_finds_pottery_detail', views.DC_finds_pottery_detailViewSet)
router.register(r'dc_finds_pottery_decoration', views.DC_finds_pottery_decorationViewSet)
router.register(r'dc_interpretation_productiontype', views.DC_interpretation_productiontypeViewSet)
router.register(r'dc_interpretation_subsistencetype', views.DC_interpretation_subsistencetypeViewSet)
router.register(r'dc_chronological_system', views.DC_chronological_systemViewSet)
router.register(r'dc_period_datingmethod', views.DC_period_datingmethodViewSet)
router.register(r'dc_period_datedby', views.DC_period_datedbyViewSet)
router.register(r'Reference', views.ReferenceViewSet)
#router.register(r'ResearchEvent', views.ResearchEventViewSet)
router.register(r'Period', views.PeriodViewSet)
#router.register(r'Site', views.SiteViewSet)
#router.register(r'Area', views.AreaViewSet)
#router.register(r'Finds', views.FindsViewSet)
#router.register(r'Interpretation', views.InterpretationViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^defcdb/', include('defcdb.urls', namespace='defcdb')),
    url(r'^virtualgallery/', include('virtualgallery.urls', namespace="virtualgallery")),
	url(r'^geolocation/', include('geolocation.urls', namespace="geolocation")),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^accounts/login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': base.MEDIA_ROOT,}, name='media_root_url'),
]

