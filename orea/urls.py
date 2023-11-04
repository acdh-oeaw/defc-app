# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework import routers
from django.contrib import admin
from orea.settings import base
from defcdb import views
from defcdb import api_views
import autocomplete_light.shortcuts as al

al.autodiscover()

router = routers.DefaultRouter()
router.register(r"geojson", api_views.GeoJsonViewSet, base_name="places")
router.register(
    r"dc_finds_lithics_raw_material", api_views.DC_finds_lithics_raw_materialViewSet
)
router.register(
    r"dc_finds_lithics_retouched_tools",
    api_views.DC_finds_lithics_retouched_toolsViewSet,
)
router.register(
    r"dc_finds_lithics_retouched_tools",
    api_views.DC_finds_lithics_unretouched_toolsViewSet,
)
router.register(
    r"dc_finds_lithics_core_shape", api_views.DC_finds_lithics_core_shapeViewSet
)
router.register(
    r"dc_finds_lithics_industry", api_views.DC_finds_lithics_industryViewSet
)
router.register(r"dc_area_agegroups", api_views.DC_area_agegroupsViewSet)
router.register(r"name", api_views.NameViewSet)
router.register(r"dc_country", api_views.DC_countryViewSet)
router.register(r"dc_region", api_views.DC_regionViewSet)
router.register(r"dc_province", api_views.DC_provinceViewSet)
router.register(r"dc_site_topography", api_views.DC_site_topographyViewSet)
router.register(
    r"dc_researchevent_researchtype", api_views.DC_researchevent_researchtypeViewSet
)
router.register(
    r"dc_researchevent_institution", api_views.DC_researchevent_institutionViewSet
)
router.register(
    r"dc_researchevent_special_analysis",
    api_views.DC_researchevent_special_analysisViewSet,
)
router.register(
    r"dc_site_geographicalreferencesystem",
    api_views.DC_site_geographicalreferencesystemViewSet,
)
router.register(r"dc_area_areatype", api_views.DC_area_areatypeViewSet)
router.register(r"dc_area_settlementtype", api_views.DC_area_settlementtypeViewSet)
router.register(
    r"dc_area_settlementstructure", api_views.DC_area_settlementstructureViewSet
)
router.register(r"dc_area_constructiontype", api_views.DC_area_constructiontypeViewSet)
router.register(
    r"dc_area_constructionshape", api_views.DC_area_constructionshapeViewSet
)
router.register(
    r"dc_area_buildingtechnique", api_views.DC_area_buildingtechniqueViewSet
)
router.register(r"dc_area_specialfeatures", api_views.DC_area_specialfeaturesViewSet)
router.register(
    r"dc_area_evidenceofgraveshumanremains",
    api_views.DC_area_evidenceofgraveshumanremainsViewSet,
)
router.register(
    r"dc_area_evidenceofoccupation", api_views.DC_area_evidenceofoccupationViewSet
)
router.register(
    r"dc_area_caverockshelterstype", api_views.DC_area_caverockshelterstypeViewSet
)
router.register(r"dc_area_rawmaterial", api_views.DC_area_rawmaterialViewSet)
router.register(r"dc_area_exploitationtype", api_views.DC_area_exploitationtypeViewSet)
router.register(r"dc_area_topography", api_views.DC_area_topographyViewSet)
router.register(r"dc_area_mortuaryfeatures", api_views.DC_area_mortuaryfeaturesViewSet)
router.register(r"dc_area_gravetype", api_views.DC_area_gravetypeViewSet)
router.register(
    r"dc_area_typeofhumanremains", api_views.DC_area_typeofhumanremainsViewSet
)
router.register(r"dc_area_sexes", api_views.DC_area_sexesViewSet)
router.register(
    r"dc_area_manipulationofgraves", api_views.DC_area_manipulationofgravesViewSet
)
router.register(r"dc_finds_type", api_views.DC_finds_typeViewSet)
router.register(r"dc_finds_material", api_views.DC_finds_materialViewSet)
router.register(r"dc_finds_amount", api_views.DC_finds_amountViewSet)
router.register(
    r"dc_finds_small_finds_type", api_views.DC_finds_small_finds_typeViewSet
)
router.register(
    r"dc_finds_small_finds_category", api_views.DC_finds_small_finds_categoryViewSet
)
router.register(r"dc_finds_botany_species", api_views.DC_finds_botany_speciesViewSet)
router.register(
    r"dc_finds_animal_remains_species", api_views.DC_finds_animal_remains_speciesViewSet
)
router.register(
    r"dc_finds_animal_remains_completeness",
    api_views.DC_finds_animal_remains_completenessViewSet,
)
router.register(
    r"dc_finds_animal_remains_part", api_views.DC_finds_animal_remains_partViewSet
)
router.register(
    r"dc_finds_lithics_technology", api_views.DC_finds_lithics_technologyViewSet
)
router.register(r"dc_finds_pottery_form", api_views.DC_finds_pottery_formViewSet)
router.register(r"dc_finds_pottery_detail", api_views.DC_finds_pottery_detailViewSet)
router.register(
    r"dc_finds_pottery_decoration", api_views.DC_finds_pottery_decorationViewSet
)
router.register(
    r"dc_interpretation_productiontype",
    api_views.DC_interpretation_productiontypeViewSet,
)
router.register(
    r"dc_interpretation_subsistencetype",
    api_views.DC_interpretation_subsistencetypeViewSet,
)
router.register(r"dc_chronological_system", api_views.DC_chronological_systemViewSet)
router.register(r"dc_period_datingmethod", api_views.DC_period_datingmethodViewSet)
router.register(r"dc_period_datedby", api_views.DC_period_datedbyViewSet)
router.register(r"dc_site_coordinatesource", api_views.DC_site_coordinatesource)
router.register(r"Book", api_views.BookViewSet)
router.register(r"ResearchEvent", api_views.ResearchEventViewSet)
router.register(r"Site", api_views.SiteViewSet)
router.register(r"Area", api_views.AreaViewSet)
router.register(r"Finds", api_views.FindsViewSet)
router.register(r"Interpretation", api_views.InterpretationViewSet)

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^api/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls")),
    url(r"^defcdb/", include("defcdb.urls", namespace="defcdb")),
    url(r"^geolocation/", include("geolocation.urls", namespace="geolocation")),
    url(r"^login/$", views.user_login, name="user_login"),
    url(r"^accounts/login/$", views.user_login, name="user_login"),
    url(r"^logout/$", views.user_logout, name="user_logout"),
    url(r"^autocomplete/", include("autocomplete_light.urls")),
    url(r"^", include("webpage.urls", namespace="webpage")),
    url(r"^bib/", include("bib.urls", namespace="bib")),
    url(
        r"^media/(?P<path>.*)$",
        "django.views.static.serve",
        {
            "document_root": base.MEDIA_ROOT,
        },
        name="media_root_url",
    ),
    url(r"^image_gallery/", include("images_metadata.urls", namespace="image_gallery")),
    url(r"^publicrecords/", include("publicrecords.urls", namespace="publicrecords")),
    url(r"^3Dmodels/", include("threedmodels.urls", namespace="3Dmodels")),
    url(r"^browsing/", include("browsing.urls", namespace="browsing")),
    url(r"^datamodel/", include("django_spaghetti.urls", namespace="datamodel")),
]
