import django_filters
from defcdb.models import *
from .forms import SiteFilterForm


django_filters.filters.LOOKUP_TYPES = [
    ("", "---------"),
    ("exact", "Is equal to"),
    ("iexact", "Is equal to (case insensitive)"),
    ("not_exact", "Is not equal to"),
    ("lt", "Lesser than/before"),
    ("gt", "Greater than/after"),
    ("gte", "Greater than or equal to"),
    ("lte", "Lesser than or equal to"),
    ("startswith", "Starts with"),
    ("endswith", "Ends with"),
    ("contains", "Contains"),
    ("icontains", "Contains (case insensitive)"),
    ("not_contains", "Does not contain"),
]

YESNO_CHOICES = (
    ("", "---------"),
    ("yes", "yes"),
    ("no", "no"),
)

GRAVE_OR_CEMETERY_CHOICES = (
    ("", "---------"),
    ("cemetery", "cemetery"),
    ("grave", "grave"),
)

CONFIDENCE_CHOICES = (
    ("", "---------"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


class MapListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains", label="Site name", help_text=False
    )
    province__region__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_region.objects.all(), label="Region", help_text=False
    )
    province = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_province.objects.all(), label="District", help_text=False
    )
    topography__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_site_topography.objects.all(), label="Topography", help_text=False
    )
    period = django_filters.CharFilter(
        label="Period",
        field_name="area__period__period_name",
        distinct=True,
        lookup_expr="icontains",
        help_text=False,
    )
    period__cs_name = django_filters.CharFilter(
        label="Period Chronological system",
        help_text=False,
        field_name="area__period__cs_name",
        distinct=True,
        lookup_expr="icontains",
    )
    area__period__start_date1_BC = django_filters.NumberFilter(
        lookup_expr="lte",
        label="Period start date 1 BC",
        help_text="Lesser than or equal to",
        field_name="area__period__start_date1_BC",
        distinct=True,
    )
    area__period__end_date1_BC = django_filters.NumberFilter(
        lookup_expr="gte",
        label="Period end date 1 BC",
        help_text="Greater than or equal to",
        field_name="area__period__end_date1_BC",
        distinct=True,
    )
    # area filters
    area__area_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_areatype.objects.all(), help_text=False, label="Area type"
    )
    area__dating_method = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_period_datingmethod.objects.all(),
        help_text=False,
        label="Dating method",
    )

    area__radiocarbon_dated = django_filters.ChoiceFilter(
        choices=YESNO_CHOICES, help_text=False, label="Radiocarbon dated"
    )

    # settlement fields

    area__settlement_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_settlementtype.objects.all(),
        help_text=False,
        label="Settlement type",
    )

    area__settlement_structure = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_settlementstructure.objects.all(),
        help_text=False,
        label="Settlement structure",
    )

    area__settlement_construction_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_constructiontype.objects.all(),
        help_text=False,
        label="Settlement building type",
    )

    area__settlement_construction_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_constructionshape.objects.all(),
        help_text=False,
        label="Settlement building shape",
    )

    area__settlement_building_technique = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_buildingtechnique.objects.all(),
        help_text=False,
        label="Settlement building technique",
    )

    area__settlement_special_features = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_specialfeatures.objects.all(),
        help_text=False,
        label="Settlement archaeological features",
    )
    # get helptext
    # help_text=Area._meta.get_field('settlement_special_features').help_text

    area__settlement_human_remains = django_filters.ChoiceFilter(
        choices=YESNO_CHOICES, help_text=False, label="Settlement human remains"
    )

    # cave/rockshelters fields

    area__cave_rockshelters_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_caverockshelterstype.objects.all(),
        help_text=False,
        label="Cave rockshelters type",
    )

    area__cave_rockshelters_human_remains = django_filters.ChoiceFilter(
        choices=YESNO_CHOICES, help_text=False, label="Cave rockshelters human remains"
    )

    area__cave_rockshelters_evidence_of_occupation = (
        django_filters.ModelMultipleChoiceFilter(
            queryset=DC_area_evidenceofoccupation.objects.all(),
            help_text=False,
            label="Cave rockshelters evidence of occupation",
        )
    )

    # quarry fields

    area__quarry_exploitation_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_exploitationtype.objects.all(),
        help_text=False,
        label="Querry exploitation type",
    )

    area__quarry_raw_material = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_rawmaterial.objects.all(),
        help_text=False,
        label="Quarry raw material",
    )

    # cemetery/graves fields

    area__cemetery_or_grave = django_filters.ChoiceFilter(
        choices=GRAVE_OR_CEMETERY_CHOICES, help_text=False, label="Cemetery or grave"
    )

    area__cemetery_or_graves_topography = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_topography.objects.all(),
        help_text=False,
        label="Cemetery or grave topography",
    )

    area__cemetery_or_graves_mortuary_features = (
        django_filters.ModelMultipleChoiceFilter(
            queryset=DC_area_mortuaryfeatures.objects.all(),
            help_text=False,
            label="Cemetery or grave mortuary features",
        )
    )
    area__grave_number_of_graves = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Number of graves"
    )

    area__grave_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_gravetype.objects.all(), help_text=False, label="Grave type"
    )
    area__grave_type_of_human_remains = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_typeofhumanremains.objects.all(),
        help_text=False,
        label="Grave: type of human remains",
    )
    area__grave_estimated_number_of_individuals = django_filters.NumberFilter(
        lookup_expr="exact",
        help_text=False,
        label="Grave estimated number of individuals",
    )

    area__grave_age_groups = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_agegroups.objects.all(),
        help_text=False,
        label="Grave: age groups",
    )
    area__grave_sexes = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_sexes.objects.all(), help_text=False, label="Grave: sexes"
    )
    area__grave_number_of_female_sex = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False, label="Grave: number of female sex"
    )

    area__grave_number_of_male_sex = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False, label="Grave: number of male sex"
    )

    area__grave_number_of_not_specified_sex = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False, label="Grave: number of not specified sex"
    )

    area__grave_manipulations_of_graves = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_manipulationofgraves.objects.all(),
        help_text=False,
        label="Grave: disturbance of graves",
    )
    # finds filters
    area__finds__finds_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_type.objects.all(), help_text=False, label="Finds type"
    )
    area__finds__amount = django_filters.ModelChoiceFilter(
        queryset=DC_finds_amount.objects.all(), help_text=False, label="Finds amount"
    )
    area__finds__material = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_material.objects.all(),
        help_text=False,
        label="Finds material",
    )
    area__finds__confidence = django_filters.ChoiceFilter(
        choices=CONFIDENCE_CHOICES, help_text=False, label="Finds confidence"
    )

    # small finds fields

    area__finds__small_finds_category = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_small_finds_category.objects.all(),
        help_text=False,
        label="Small finds category",
    )

    area__finds__small_finds_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_small_finds_type.objects.all(),
        help_text=False,
        label="Small finds type",
    )
    # Botany fields

    area__finds__botany_species = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_botany_species.objects.all(),
        help_text=False,
        label="Botany species",
    )
    # Animal remains fields

    area__finds__animal_remains_species = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_animal_remains_species.objects.all(),
        help_text=False,
        label="Animal remains species",
    )
    area__finds__animal_remains_completeness = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_animal_remains_completeness.objects.all(),
        help_text=False,
        label="Animal remains completeness",
    )
    area__finds__animal_remains_part = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_animal_remains_part.objects.all(),
        help_text=False,
        label="Animal remains part",
    )
    # Lithics fields

    area__finds__lithics_technology = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_technology.objects.all(),
        help_text=False,
        label="Lithics technology",
    )
    area__finds__lithics_industry = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_industry.objects.all(),
        help_text=False,
        label="Lithics industry",
    )
    area__finds__lithics_core_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_core_shape.objects.all(),
        help_text=False,
        label="Lithics cores and preparation",
    )
    area__finds__lithics_retouched_tools = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_retouched_tools.objects.all(),
        help_text=False,
        label="Lithics retouched tools",
    )
    area__finds__lithics_unretouched_tools = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_unretouched_tools.objects.all(),
        help_text=False,
        label="Lithics unretouched tools",
    )
    area__finds__lithics_raw_material = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_raw_material.objects.all(),
        help_text=False,
        label="Lithics raw material",
    )
    area__finds__obsidian = django_filters.ChoiceFilter(
        choices=YESNO_CHOICES, help_text=False, label="Obsidian"
    )

    area__finds__obsidian_amount = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False, label="Obsidian amount"
    )

    # Pottery fields

    area__finds__pottery_form = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_pottery_form.objects.all(),
        help_text=False,
        label="Pottery form",
    )
    area__finds__pottery_detail = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_pottery_detail.objects.all(),
        help_text=False,
        label="Pottery detail",
    )
    area__finds__pottery_decoration = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_pottery_decoration.objects.all(),
        help_text=False,
        label="Pottery decoration",
    )
    area__finds__pottery_type = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Pottery type"
    )

    class Meta:
        model = Site
        form = SiteFilterForm
        fields = "__all__"


class SiteListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains", label="Site name", help_text=False
    )
    province__region__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_region.objects.all(), label="Region", help_text=False
    )
    province = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_province.objects.all(), label="District", help_text=False
    )
    topography__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_site_topography.objects.all(), label="Topography", help_text=False
    )
    period = django_filters.CharFilter(
        label="Period",
        field_name="area__period__period_name",
        distinct=True,
        lookup_expr="icontains",
        help_text=False,
    )
    period__cs_name = django_filters.CharFilter(
        label="Period Chronological system",
        help_text=False,
        field_name="area__period__cs_name",
        distinct=True,
        lookup_expr="icontains",
    )
    area__period__start_date1_BC = django_filters.NumberFilter(
        lookup_expr="lte",
        label="Period start date 1 BC",
        help_text="Lesser than or equal to",
        field_name="area__period__start_date1_BC",
        distinct=True,
    )
    area__period__end_date1_BC = django_filters.NumberFilter(
        lookup_expr="gte",
        label="Period end date 1 BC",
        help_text="Greater than or equal to",
        field_name="area__period__end_date1_BC",
        distinct=True,
    )

    class Meta:
        model = Site
        form = SiteFilterForm
        fields = ["id", "province"]


class AreaListFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='icontains') no name field in area class
    site__province__region__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_region.objects.all(), label="Region", help_text=False
    )
    site__province = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_province.objects.all(), label="District", help_text=False
    )
    area_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_areatype.objects.all(), help_text=False
    )
    site__name = django_filters.CharFilter(lookup_expr="icontains", help_text=False)
    period = django_filters.CharFilter(
        label="Period",
        field_name="period__period_name",
        distinct=True,
        lookup_expr="icontains",
        help_text=False,
    )
    period__cs_name = django_filters.CharFilter(
        label="Period Chronological system",
        field_name="period__cs_name",
        distinct=True,
        lookup_expr="icontains",
        help_text=False,
    )
    period__start_date1_BC = django_filters.NumberFilter(
        lookup_expr="lte",
        label="Period start date 1 BC",
        help_text="Lesser than or equal to",
    )
    period__end_date1_BC = django_filters.NumberFilter(
        lookup_expr="gte",
        label="Period end date 1 BC",
        help_text="Greater than or equal to",
    )
    dating_method = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_period_datingmethod.objects.all(), help_text=False
    )

    radiocarbon_dated = django_filters.ChoiceFilter(
        choices=YESNO_CHOICES, help_text=False
    )

    # settlement fields

    settlement_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_settlementtype.objects.all(), help_text=False
    )

    settlement_structure = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_settlementstructure.objects.all(), help_text=False
    )

    settlement_construction_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_constructiontype.objects.all(),
        help_text=False,
        label="Settlement building type",
    )

    settlement_construction_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_constructionshape.objects.all(),
        help_text=False,
        label="Settlement building shape",
    )

    settlement_building_technique = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_buildingtechnique.objects.all(), help_text=False
    )

    settlement_special_features = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_specialfeatures.objects.all(),
        help_text=False,
        label="Settlement archaeological features",
    )
    # help_text=Area._meta.get_field('settlement_special_features').help_text
    settlement_human_remains = django_filters.ChoiceFilter(
        choices=YESNO_CHOICES, help_text=False
    )

    # cave/rockshelters fields

    cave_rockshelters_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_caverockshelterstype.objects.all(), help_text=False
    )

    cave_rockshelters_human_remains = django_filters.ChoiceFilter(
        choices=YESNO_CHOICES, help_text=False
    )

    cave_rockshelters_evidence_of_occupation = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_evidenceofoccupation.objects.all(), help_text=False
    )

    # quarry fields

    quarry_exploitation_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_exploitationtype.objects.all(), help_text=False
    )

    quarry_raw_material = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_rawmaterial.objects.all(), help_text=False
    )

    # cemetery/graves fields

    cemetery_or_grave = django_filters.ChoiceFilter(
        choices=GRAVE_OR_CEMETERY_CHOICES, help_text=False
    )

    cemetery_or_graves_topography = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_topography.objects.all(), help_text=False
    )

    cemetery_or_graves_mortuary_features = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_mortuaryfeatures.objects.all(), help_text=False
    )
    grave_number_of_graves = django_filters.CharFilter(
        lookup_expr="exact", help_text=False
    )

    grave_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_gravetype.objects.all(), help_text=False
    )
    grave_type_of_human_remains = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_typeofhumanremains.objects.all(), help_text=False
    )
    grave_estimated_number_of_individuals = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False
    )

    grave_age_groups = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_agegroups.objects.all(), help_text=False
    )
    grave_sexes = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_sexes.objects.all(), help_text=False
    )
    grave_number_of_female_sex = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False
    )

    grave_number_of_male_sex = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False
    )

    grave_number_of_not_specified_sex = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False
    )

    grave_manipulations_of_graves = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_manipulationofgraves.objects.all(),
        help_text=False,
        label="Grave disturbance of graves",
    )

    class Meta:
        model = Area
        fields = ["id", "area_type"]


class FindsListFilter(django_filters.FilterSet):
    finds_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_type.objects.all(), help_text=False
    )
    area__site__province = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_province.objects.all(), label="District", help_text=False
    )
    area__site__name = django_filters.CharFilter(
        lookup_expr="icontains", label="Site name", help_text=False
    )
    area__area_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_areatype.objects.all(), label="Area type", help_text=False
    )
    research_event__research_type__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_researchevent_researchtype.objects.all(),
        label="Research type",
        help_text=False,
    )
    period = django_filters.CharFilter(
        label="Period",
        field_name="area__period__period_name",
        distinct=True,
        lookup_expr="icontains",
        help_text=False,
    )
    period__cs_name = django_filters.CharFilter(
        label="Period Chronological system",
        help_text=False,
        field_name="area__period__cs_name",
        distinct=True,
        lookup_expr="icontains",
    )
    area__period__start_date1_BC = django_filters.NumberFilter(
        lookup_expr="lte",
        label="Period start date 1 BC",
        help_text="Lesser than or equal to",
    )
    area__period__end_date1_BC = django_filters.NumberFilter(
        lookup_expr="gte",
        label="Period end date 1 BC",
        help_text="Greater than or equal to",
    )
    amount = django_filters.ModelChoiceFilter(
        queryset=DC_finds_amount.objects.all(), help_text=False
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_material.objects.all(), help_text=False
    )
    confidence = django_filters.ChoiceFilter(
        choices=CONFIDENCE_CHOICES, help_text=False
    )

    # small finds fields

    small_finds_category = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_small_finds_category.objects.all(), help_text=False
    )

    small_finds_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_small_finds_type.objects.all(), help_text=False
    )
    # Botany fields

    botany_species = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_botany_species.objects.all(), help_text=False
    )
    # Animal remains fields

    animal_remains_species = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_animal_remains_species.objects.all(), help_text=False
    )
    animal_remains_completeness = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_animal_remains_completeness.objects.all(), help_text=False
    )
    animal_remains_part = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_animal_remains_part.objects.all(), help_text=False
    )
    # Lithics fields

    lithics_technology = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_technology.objects.all(), help_text=False
    )
    lithics_industry = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_industry.objects.all(), help_text=False
    )
    lithics_core_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_core_shape.objects.all(),
        help_text=False,
        label="Lithics cores and preparation",
    )
    lithics_retouched_tools = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_retouched_tools.objects.all(), help_text=False
    )
    lithics_unretouched_tools = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_unretouched_tools.objects.all(), help_text=False
    )
    lithics_raw_material = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_lithics_raw_material.objects.all(), help_text=False
    )
    obsidian = django_filters.ChoiceFilter(choices=YESNO_CHOICES, help_text=False)

    obsidian_amount = django_filters.NumberFilter(lookup_expr="exact", help_text=False)

    # Pottery fields

    pottery_form = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_pottery_form.objects.all(), help_text=False
    )
    pottery_detail = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_pottery_detail.objects.all(), help_text=False
    )
    pottery_decoration = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_pottery_decoration.objects.all(), help_text=False
    )
    pottery_type = django_filters.CharFilter(lookup_expr="icontains", help_text=False)

    class Meta:
        model = Finds
        fields = ["id", "finds_type"]


class ResearchEventListFilter(django_filters.FilterSet):
    research_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_researchevent_researchtype.objects.all(), help_text=False
    )
    institution = django_filters.CharFilter(
        field_name="institution__name",
        distinct=True,
        lookup_expr="icontains",
        help_text=False,
    )
    year_of_activity_start_year = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False, label="Start year of research activity"
    )
    year_of_activity_end_year = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False, label="End year of research activity"
    )
    project_name = django_filters.CharFilter(lookup_expr="icontains", help_text=False)
    finds__area__site__name = django_filters.CharFilter(
        lookup_expr="icontains", label="Site name", help_text=False
    )

    class Meta:
        model = ResearchEvent
        fields = ["id", "research_type"]


class InterpretationListFilter(django_filters.FilterSet):
    production_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_interpretation_productiontype.objects.all(), help_text=False
    )
    subsistence_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_interpretation_subsistencetype.objects.all(), help_text=False
    )
    area__site__name = django_filters.CharFilter(
        lookup_expr="icontains", label="Site name", help_text=False
    )
    area__site__province__region__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_region.objects.all(), label="Region", help_text=False
    )
    area__site__province = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_province.objects.all(), label="District", help_text=False
    )

    class Meta:
        model = Interpretation
        fields = ["id", "production_type"]
