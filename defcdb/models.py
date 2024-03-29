# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from bib.models import Book
from reversion import revisions as reversion


class TrackChanges(models.Model):
    """
    Abstract base class with a creation and modification date and time
    """

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    public = models.BooleanField(
        default=False, help_text="Make this record public or not?"
    )

    class Meta:
        abstract = True
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class GenericMethods(models.Model):
    description = models.TextField(blank=True, help_text="Short description.")

    class Meta:
        abstract = True
        ordering = ("name",)

    def __str__(self):
        return self.name


#################################
#           DC-Classes          #
#################################


class DC_country(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, help_text="The name of the country"
    )
    original_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The original or local name of the country",
    )
    authorityfile_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Identifier provided by www.GeoNames.org",
    )
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)


class DC_region(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="The name of the region"
    )
    original_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The original or local name of the region",
    )
    authorityfile_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Identifier provided by www.GeoNames.org",
    )
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    country = models.ForeignKey(
        DC_country,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The name of the country",
    )


class DC_province(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="The name of the province"
    )
    original_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The original or local name of the province",
    )
    authorityfile_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Identifier provided by www.GeoNames.org",
    )
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    region = models.ForeignKey(
        DC_region,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The name of the country",
    )

    def __str__(self):
        return str(self.region) + "_" + self.name


class DC_reference_type(GenericMethods):
    name = models.CharField(max_length=100, blank=True, null=True)


class DC_researchevent_researchtype(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Methods used for researching the site.",
    )


class DC_researchevent_institution(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Organisation that carried out a research project at the site.",
    )


class DC_researchevent_special_analysis(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Analyses other than excavation that were carried out to research the site.",
    )


class DC_site_geographicalreferencesystem(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Name of system uniquely determining the position of the site.",
    )


class DC_site_topography(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Description of surface shape and features.",
    )


class DC_area_areatype(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="The type of the area."
    )


class DC_area_settlementtype(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Classification of settlement."
    )


class DC_area_settlementstructure(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Layout of settlement."
    )


class DC_area_constructiontype(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Type of buildings."
    )


class DC_area_constructionshape(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Shape of building."
    )


class DC_area_buildingtechnique(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Method used for fabricating the buildings.",
    )


class DC_area_specialfeatures(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Parts of the settlement other than buildings.",
    )


class DC_area_evidenceofgraveshumanremains(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Presence of graves and/or human remains.",
    )


class DC_area_evidenceofoccupation(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Type of evidence indicating occupation found.",
    )


class DC_area_caverockshelterstype(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Type of cave/rockshelter."
    )


class DC_area_rawmaterial(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Resource that was extracted."
    )


class DC_area_exploitationtype(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Type of extraction."
    )


class DC_area_topography(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Connection of the cemetery/graves with other archaeological /natural or modified landscape features.",
    )


class DC_area_mortuaryfeatures(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Parts of the cemetery other than graves.",
    )


class DC_area_gravetype(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Types of graves."
    )


class DC_area_typeofhumanremains(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="How the humans were treated after death and buried.",
    )


class DC_area_agegroups(GenericMethods):
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Age.")


class DC_area_sexes(GenericMethods):
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Sex.")


class DC_area_manipulationofgraves(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="If and how the space with the graves is marked.",
    )


class DC_finds_type(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class DC_finds_material(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_amount(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )

    def __str__(self):
        return self.name


class DC_finds_small_finds_category(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_small_finds_type(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    german_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    category = models.ForeignKey(
        DC_finds_small_finds_category, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        try:
            return str(self.name) + " - " + str(self.category)
        except:
            return str(self.name)
        # return str(self.name)+' - '+str(self.category)


class DC_finds_botany_species(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    latin_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return "%s (%s)" % (self.name, self.latin_name)


class DC_finds_animal_remains_species(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    latin_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return "%s (%s)" % (self.name, self.latin_name)


class DC_finds_animal_remains_completeness(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_animal_remains_part(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_lithics_technology(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_lithics_industry(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_lithics_core_shape(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_lithics_retouched_tools(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_lithics_unretouched_tools(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_lithics_raw_material(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )


class DC_finds_pottery_form(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    german_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    region = models.ManyToManyField(DC_region, blank=True)

    def __str__(self):
        # return u'%s - %s' % (self.name, self.region.name)
        return str(self.name) + "_" + str("_".join([str(x) for x in self.region.all()]))


class DC_finds_pottery_detail(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    german_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    region = models.ManyToManyField(DC_region, blank=True)

    def __str__(self):
        # return u'%s - %s' % (self.name, self.region.name)
        # return str(self.name)+'_'+str(self.region)
        return str(self.name) + "_" + str("_".join([str(x) for x in self.region.all()]))


class DC_finds_pottery_decoration(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    german_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX"
    )
    region = models.ManyToManyField(DC_region, blank=True)

    def __str__(self):
        return str(self.name) + "_" + str("_".join([str(x) for x in self.region.all()]))


######DCs for Interpretation######
class DC_interpretation_productiontype(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Types of production for which evidence was found.",
    )


class DC_interpretation_subsistencetype(GenericMethods):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Types of livelihood for which evidence was found.",
    )


class DC_chronological_system(GenericMethods):
    cs_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Name of the chronological system.",
    )
    period_name = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        help_text="Name of archaeological period for which evidence was found.",
    )
    start_date1_bc = models.IntegerField(blank=True, null=True)
    start_date2_bc = models.IntegerField(blank=True, null=True)
    end_date1_bc = models.IntegerField(blank=True, null=True)
    end_date2_bc = models.IntegerField(blank=True, null=True)
    region = models.ManyToManyField(DC_region, blank=True)

    class Meta:
        ordering = ("cs_name",)

    def __str__(self):
        # return str(self.region)+'_'+str(self.cs_name)+'_'+str(self.period_name)+'_'+str(self.start_date1_bc)
        return (
            str(self.cs_name)
            + "_"
            + str(self.period_name)
            + "_"
            + str(self.start_date1_bc)
            + "_"
            + str(self.end_date1_bc)
            + "_"
            + str("_".join([str(x) for x in self.region.all()]))
        )


class DC_period_datingmethod(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="please provide helptext"
    )
    # return ("/".join([str(x) for x in self.name.all()]))


class DC_period_datedby(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="please provide helptext"
    )


class DC_site_coordinatesource(GenericMethods):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="please provide helptext"
    )


#####################################
#       content tables              #
#####################################


class Name(TrackChanges):
    name = models.CharField(
        max_length=100, blank=True, null=True, help_text="The entities name"
    )
    language = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        help_text="The 'name´s' language. Controlled vocab will be provided.",
    )

    def __str__(self):
        return self.name


class Reference(TrackChanges):
    title = models.CharField(
        max_length=100, blank=True, null=True, help_text="The title of the ressource."
    )
    creator = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The person who is main responsible for creating the resource",
    )
    creation_time = models.IntegerField(
        blank=True,
        null=True,
        help_text="The date of the creation date of the ressource.",
    )
    # note: maybe use dc-vocabulary or maybe follow Zotero/Citavi?
    url = models.URLField(
        max_length=100, blank=True, null=True, help_text="The URL to the ressource"
    )

    class Meta:
        ordering = ("title",)


class ResearchEvent(TrackChanges):
    research_type = models.ManyToManyField(
        DC_researchevent_researchtype,
        blank=True,
        help_text="Methods used for researching the site.",
    )  # mandatory? default?
    institution = models.ManyToManyField(
        DC_researchevent_institution,
        blank=True,
        help_text="Organisation that carried out a research project at the site.",
    )  # mandatory? default?
    year_of_activity_start_year = models.IntegerField(
        blank=True,
        null=True,
        help_text="Year when research started.",
        verbose_name="Start year of research activity",
    )
    year_of_activity_end_year = models.IntegerField(
        blank=True,
        null=True,
        help_text="Year when research ended.",
        verbose_name="End year of research activity",
    )
    project_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Name of project."
    )  # optional?
    project_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Project unique identifier.",
        verbose_name="Project ID",
    )  # optional?
    project_leader = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Leader of the research project.",
    )  # optional?
    special_analysis = models.ManyToManyField(
        DC_researchevent_special_analysis,
        blank=True,
        help_text="Analyses other than excavation that were carried out to research the site.",
    )
    reference = models.ManyToManyField(
        Book,
        blank=True,
        help_text="Bibliographic and/or web-based reference(s) to publications and other relevant resources related to the project.",
    )
    comment = models.TextField(
        blank=True,
        null=True,
        help_text="Additional information on the research history not covered in any other field.",
    )

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return (
            str(
                "/".join([str(x) for x in self.research_type.all()])
                + "_"
                + str(self.project_name)
                + "_"
                + "/".join([str(x) for x in self.institution.all()])
            )
            + "_"
            + str(self.year_of_activity_start_year)
        )

    def get_absolute_url(self):
        return reverse("defcdb:researchevent_list")


reversion.register(ResearchEvent)


class Site(TrackChanges):
    EXACT_LOCATION_CHOICES = (
        ("yes", "yes"),
        ("no", "no"),
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.",
    )
    alias_name = models.ManyToManyField(
        Name, blank=True, help_text="Other name of the site.", related_name="aliasName"
    )
    alternative_name = models.ManyToManyField(
        Name,
        blank=True,
        help_text="Different spelling of the name of the site.",
        related_name="alternativeName",
    )
    province = models.ForeignKey(
        DC_province,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Geographical area where the site is located.",
        verbose_name="District",
    )
    geographical_coordinate_reference_system = models.ForeignKey(
        DC_site_geographicalreferencesystem,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Name of system uniquely determining the position of the site.",
    )
    coordinate_source = models.ForeignKey(
        DC_site_coordinatesource,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Source providing information about the global position of site.",
    )
    latitude = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True
    )
    elevation = models.IntegerField(blank=True, null=True, help_text="If available")
    authorityfile_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Identifier provided by www.GeoNames.org. E.g. the number in <a href='http://www.geonames.org/2772400/linz.html'>http://www.geonames.org/2772400/linz.html</a>.",
        verbose_name="Authorityfile ID",
    )
    topography = models.ForeignKey(
        DC_site_topography,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Description of surface shape and features.",
    )
    description = models.TextField(
        blank=True, null=True, help_text="Free text summary account on the site."
    )
    exact_location = models.CharField(
        max_length=50,
        choices=EXACT_LOCATION_CHOICES,
        default="no",
        help_text="<strong>Yes</strong>: location of site is known and coordinates from the approximate center of the site have been entered.<br/> <strong>No</strong>: Only the region/province/ephorie approximate location of the site is known. Coordinates from the approximate center of the region/province/ ephorie have been entered.",
    )
    number_of_activity_periods = models.IntegerField(
        blank=True,
        null=True,
        help_text="How many past activities have been recorded on the site?",
    )
    reference = models.ManyToManyField(
        Book,
        blank=True,
        help_text="Bibliographic and web-based references to publications and other relevant information on the site.",
    )
    comment = models.TextField(
        blank=True,
        null=True,
        help_text="Additional information on the site not covered in any other field.",
    )

    def __str__(self):
        return str(self.province) + "_" + str(self.name)

    def get_absolute_url(self):
        return reverse("publicrecords:site_detail", kwargs={"pk": self.id})

    class Meta:
        unique_together = ("name", "province")
        ordering = ["id", ]


reversion.register(Site)


class Area(TrackChanges):
    YESNO = (("yes", "yes"), ("no", "no"))
    GRAVEYESNO = (("cemetery", "cemetery"), ("grave", "grave"))
    HUMANREMAINS = (
        ("yes", "yes"),
        ("no", "no"),
    )
    site = models.ForeignKey(
        Site,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The site where this area is located.",
    )
    area_type = models.ForeignKey(
        DC_area_areatype,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The type of the area.",
    )
    area_nr = models.CharField(
        max_length=45,
        blank=True,
        null=True,
        help_text="An established identifier for this area",
        verbose_name="Area ID",
    )
    # Period fields
    period = models.ManyToManyField(
        DC_chronological_system,
        blank=True,
        help_text="Chronological period. This contains information about the name, the period, start/enddate1/2, and the region.",
    )
    dating_method = models.ManyToManyField(
        DC_period_datingmethod, blank=True, help_text="Method used for dating the site."
    )
    radiocarbon_dated = models.CharField(
        max_length=5,
        blank=True,  # moved these fields from Period table
        null=True,
        choices=YESNO,
        help_text="Radiocarbon dated?",
    )
    earliest_date_lab_number = models.CharField(
        max_length=100,
        blank=True,  # moved these fields from Period table
        null=True,
        help_text="The Laboratory number of 14C sample of the earliest date.",
        verbose_name="Earliest date: Lab Number",
    )
    earliest_date_14c_age = models.IntegerField(
        null=True,
        blank=True,
        help_text="The earliest date without calibration BP.",
        verbose_name="Earliest date: 14C age (BP)",
    )
    earliest_date_calibration = models.CharField(
        max_length=5,
        blank=True,  # moved these fields from Period table
        null=True,
        choices=YESNO,
        help_text="Was the date calibrated or not?",
        verbose_name="Earliest date: Calibration",
    )
    earliest_date_14c_age_calibrated = models.IntegerField(
        null=True,
        blank=True,
        help_text="The earliest date with calibration in BC.",
        verbose_name="Earliest date: 14C age calibrated (BC)",
    )
    earliest_date_date_of_calibration = models.DateField(
        null=True,
        blank=True,
        help_text="When was the date calibrated? If only year is specified, use the first day of the month/year.",
        verbose_name="Earliest date: Date of calibration",
    )
    earliest_date_standard_deviation = models.IntegerField(
        null=True,
        blank=True,
        help_text="The statistical reliability of the dating. Use +/-.",
        verbose_name="Earliest date: Standard deviation (+/-)",
    )
    earliest_date_delta13 = models.IntegerField(
        null=True,
        blank=True,
        help_text="Delta 13C information.",
        verbose_name="Earliest date: delta 13C",
    )
    earliest_datedated_by = models.ManyToManyField(
        DC_period_datedby,
        max_length=100,
        blank=True,
        help_text="Dating source material.",
        verbose_name="Earliest date: Dated by",
        related_name="earliestdatedatedby",
    )
    latest_date_lab_number = models.CharField(
        max_length=100,
        blank=True,  # moved these fields from Period table
        null=True,
        help_text="The Laboratory number of 14C sample of the latest date.",
        verbose_name="Latest date: Lab Number",
    )
    latest_date_14c_age = models.IntegerField(
        null=True,
        blank=True,
        help_text="The latest date without calibration BP (raw).",
        verbose_name="Latest date: 14C age (BP)",
    )
    latest_date_calibration = models.CharField(
        max_length=5,
        blank=True,  # moved these fields from Period table
        null=True,
        choices=YESNO,
        help_text="Was the date calibrated or not?",
        verbose_name="Latest date: Calibration",
    )
    latest_date_14c_age_calibrated = models.IntegerField(
        null=True,
        blank=True,
        help_text="The latest date with calibration in BC.",
        verbose_name="Latest date: 14C age calibrated (BC)",
    )
    latest_date_date_of_calibration = models.DateField(
        null=True,
        blank=True,
        help_text="When was the date calibrated? If only year is specified, use the first day of the month/year.",
        verbose_name="Latest date: Date of calibration",
    )
    latest_date_standard_deviation = models.IntegerField(
        null=True,
        blank=True,
        help_text="The statistical reliability of the dating. Use +/-.",
        verbose_name="Latest date: Standard deviation (+/-)",
    )
    latest_date_delta13 = models.IntegerField(
        null=True,
        blank=True,
        help_text="Delta 13C information.",
        verbose_name="Latest date: delta 13C",
    )
    latest_datedated_by = models.ManyToManyField(
        DC_period_datedby,
        max_length=100,
        blank=True,
        help_text="Dating source material.",
        verbose_name="Latest date: Dated by",
        related_name="latestdatedatedby",
    )
    period_reference = models.ManyToManyField(
        Book,
        blank=True,
        help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the period.",
        related_name="periodreference",
    )
    period_comment = models.TextField(
        blank=True,
        null=True,
        help_text="Additional information on the period not covered in any other field.",
    )
    # settlement fields
    settlement_type = models.ForeignKey(
        DC_area_settlementtype,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Classification of settlement.",
    )
    settlement_structure = models.ManyToManyField(
        DC_area_settlementstructure, blank=True, help_text="Layout of settlement."
    )
    settlement_construction_type = models.ManyToManyField(
        DC_area_constructiontype,
        blank=True,
        help_text="Method used for fabricating the buildings.",
        verbose_name="Settlement building type",
    )
    settlement_construction_shape = models.ManyToManyField(
        DC_area_constructionshape,
        blank=True,
        help_text="Shape of the building.",
        verbose_name="Settlement building shape",
    )
    settlement_building_technique = models.ManyToManyField(
        DC_area_buildingtechnique, blank=True, help_text="Type of buildings."
    )
    settlement_special_features = models.ManyToManyField(
        DC_area_specialfeatures,  # it was FK field
        blank=True,
        help_text="Parts of the settlement other than buildings.",
        verbose_name="Settlement archaeological features",
    )
    settlement_human_remains = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        choices=HUMANREMAINS,
        help_text="Any human remains found in this Settlement?",
    )
    # cave&rockshelters fields
    cave_rockshelters_type = models.ForeignKey(
        DC_area_caverockshelterstype,
        on_delete=models.SET_NULL,
        verbose_name="Cave/rockshelters type",
        blank=True,
        null=True,
        help_text="Type of cave/rockshelter.",
    )
    cave_rockshelters_human_remains = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        choices=HUMANREMAINS,
        help_text="Any human remains found in this cave or rockshelter?",
    )
    cave_rockshelters_evidence_of_occupation = models.ManyToManyField(
        DC_area_evidenceofoccupation,
        verbose_name="Cave/rockshelters: evidence of occupation",
        blank=True,
        help_text="Type of evidence indicating occupation found.",
    )
    # quarry fields
    quarry_exploitation_type = models.ForeignKey(
        DC_area_exploitationtype,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Type of extraction.",
    )
    quarry_raw_material = models.ManyToManyField(
        DC_area_rawmaterial, blank=True, help_text="Resource that was extracted."
    )
    # cemetery/graves fields
    cemetery_or_grave = models.CharField(
        max_length=100, blank=True, null=True, choices=GRAVEYESNO
    )
    cemetery_or_graves_topography = models.ManyToManyField(
        DC_area_topography,
        blank=True,
        help_text="Connection of the cemetery/graves with other archaeological /natural or modified landscape features.",
    )
    cemetery_or_graves_mortuary_features = models.ManyToManyField(
        DC_area_mortuaryfeatures,
        blank=True,
        help_text="Parts of the cemetery other than graves.",
    )
    grave_number_of_graves = models.CharField(
        verbose_name="Grave: number of graves",
        max_length=100,
        blank=True,
        null=True,
        help_text="Number of graves.",
    )  # CharField or models.IntegerField ?
    grave_type = models.ManyToManyField(
        DC_area_gravetype, blank=True, help_text="Types of graves."
    )
    grave_type_of_human_remains = models.ManyToManyField(
        DC_area_typeofhumanremains,
        verbose_name="Grave: type of human remains",
        blank=True,
        help_text="How the humans were treated after death and buried.",
    )
    grave_estimated_number_of_individuals = models.CharField(
        verbose_name="Grave: estimated number of individuals",
        max_length=100,
        blank=True,
        null=True,
        help_text="minimum and or maximum",
    )
    grave_age_groups = models.ManyToManyField(
        DC_area_agegroups,
        verbose_name="Grave: age groups",
        blank=True,
        help_text="Age.",
    )
    grave_sexes = models.ManyToManyField(
        DC_area_sexes, verbose_name="Grave: sexes", blank=True, help_text="Sex."
    )
    grave_number_of_female_sex = models.IntegerField(
        verbose_name="Grave: number of female sex",
        null=True,
        blank=True,
        help_text="Number of female individuals in a grave/settlement.",
    )
    grave_number_of_male_sex = models.IntegerField(
        verbose_name="Grave: number of male sex",
        null=True,
        blank=True,
        help_text="Number of male individuals in a grave/settlement.",
    )
    grave_number_of_not_specified_sex = models.IntegerField(
        verbose_name="Grave: number of not specified sex",
        null=True,
        blank=True,
        help_text="Number of those individuals whose sex could not be determined.",
    )
    grave_manipulations_of_graves = models.ManyToManyField(
        DC_area_manipulationofgraves,
        verbose_name="Grave: disturbance of graves",
        blank=True,
        help_text="Post-depositional intervention of grave.",
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text="Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves",
    )
    reference = models.ManyToManyField(
        Book,
        blank=True,
        help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.",
        related_name="referencereference",
    )
    comment = models.TextField(
        blank=True,
        null=True,
        help_text="Additional information not covered in any other field.",
    )

    class Meta:
        ordering = ("site",)

    def __str__(self):
        return str(self.site) + "_" + str(self.area_type) + "_" + str(self.id)

    def get_absolute_url(self):
        return reverse("publicrecords:area_detail", kwargs={"pk": self.id})


reversion.register(Area)


class Finds(TrackChanges):
    CONFIDENCE_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    OBSIDIAN_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Location of the find.",
    )
    research_event = models.ForeignKey(
        ResearchEvent,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Project / Research the finds are related to.",
    )
    finds_type = models.ForeignKey(
        DC_finds_type,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Category of finds.",
    )
    # small finds properties
    small_finds_category = models.ForeignKey(
        DC_finds_small_finds_category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Superordinate class of small find.",
    )
    small_finds_type = models.ManyToManyField(
        DC_finds_small_finds_type,
        blank=True,
        help_text="What kind of small find is described.",
    )
    # Botany
    botany_species = models.ManyToManyField(
        DC_finds_botany_species,
        blank=True,
        help_text="How the botanical sample / find is categorised.",
    )
    # Animal remains
    animal_remains_species = models.ManyToManyField(
        DC_finds_animal_remains_species,
        blank=True,
        help_text="How the zoological sample / find is categorised.",
    )
    animal_remains_completeness = models.ForeignKey(
        DC_finds_animal_remains_completeness,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="How much was present (complete or part).",
    )
    animal_remains_part = models.ManyToManyField(
        DC_finds_animal_remains_part, blank=True, help_text="Which part was present."
    )
    # Lithics
    lithics_technology = models.ManyToManyField(
        DC_finds_lithics_technology,
        blank=True,
        help_text="Technology of lithic production.",
    )
    lithics_industry = models.ManyToManyField(
        DC_finds_lithics_industry,
        blank=True,
        help_text="Blade/Flake/Microlithic industry.",
    )
    lithics_core_shape = models.ManyToManyField(
        DC_finds_lithics_core_shape,
        blank=True,
        help_text="Type of the core of the tool.",
        verbose_name="Lithics cores and preparation",
    )
    lithics_retouched_tools = models.ManyToManyField(
        DC_finds_lithics_retouched_tools,
        blank=True,
        help_text="Type of the retouched tool.",
        verbose_name="Lithics retouched tools (types)",
    )
    lithics_unretouched_tools = models.ManyToManyField(
        DC_finds_lithics_unretouched_tools,
        blank=True,
        help_text="",
        verbose_name="Lithics unretouched tools (types)",
    )
    lithics_raw_material = models.ManyToManyField(
        DC_finds_lithics_raw_material,
        blank=True,
        help_text="Material from which the tool was made.",
    )
    obsidian = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Are there traces of obsidian in the tool?",
        choices=OBSIDIAN_CHOICES,
    )
    obsidian_amount = models.IntegerField(
        blank=True,
        null=True,
        help_text="The percentage of obsidian in the tool.",
        verbose_name="Obsidian amount (%)",
    )
    # Pottery
    pottery_form = models.ForeignKey(
        DC_finds_pottery_form,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The form of the pottery.",
    )
    pottery_detail = models.ManyToManyField(
        DC_finds_pottery_detail, blank=True, help_text="Preserved part of the pottery."
    )
    pottery_decoration = models.ManyToManyField(
        DC_finds_pottery_decoration,
        blank=True,
        help_text="What the pottery was embellished with.",
    )
    pottery_type = models.CharField(max_length=500, blank=True, null=True, help_text="")
    # common fields
    amount = models.ForeignKey(
        DC_finds_amount,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Number of pieces within the category.",
    )
    material = models.ManyToManyField(
        DC_finds_material, blank=True, help_text="What was the small find made of."
    )
    confidence = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="How reliable the information is that was entered.",
        choices=CONFIDENCE_CHOICES,
    )
    reference = models.ManyToManyField(
        Book,
        blank=True,
        help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the selected small finds.",
    )
    comment = models.TextField(
        blank=True,
        null=True,
        help_text="Additional information not covered in any other field.",
    )

    class Meta:
        ordering = ("area",)

    def get_absolute_url(self):
        return reverse("publicrecords:finds_detail", kwargs={"pk": self.id})

    def __str__(self):
        return str(self.area) + "_" + str(self.finds_type) + "_" + str(self.id)

    @property
    def finds_description(self):
        if self.pottery_form is not None:
            return "{} {}".format(self.finds_type, self.pottery_form.name)
        elif self.small_finds_category is not None:
            return "{} {}".format(self.finds_type, self.small_finds_category)
        else:
            return "{}".format(self.finds_type)


reversion.register(Finds)


class Interpretation(TrackChanges):
    area = models.ManyToManyField(
        Area, blank=True, help_text="The interpreted area(s)."
    )
    finds = models.ManyToManyField(
        Finds, blank=True, help_text="The interpreted find(s)."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Free text summary account on subsistence & production of the site.",
    )
    production_type = models.ManyToManyField(
        DC_interpretation_productiontype,
        blank=True,
        help_text="Types of production for which evidence was found.",
    )
    subsistence_type = models.ManyToManyField(
        DC_interpretation_subsistencetype,
        blank=True,
        help_text="Types of livelihood for which evidence was found.",
    )
    reference = models.ManyToManyField(
        Book,
        blank=True,
        help_text="Bibliographic and web-based reference(s)to publications and other relevant resources on industry & subsistence of the site/phase of the site.",
    )
    comment = models.TextField(
        blank=True,
        null=True,
        help_text="Additional information on subsistence and production not covered in any other field.",
    )

    class Meta:
        ordering = ("id",)

    def get_absolute_url(self):
        return reverse("defcdb:interpretation_list")

    def __str__(self):
        return "Interpretation" + "_" + str(self.finds) + "_" + str(self.id)


reversion.register(Interpretation)


# class RegionRegion(TrackChanges):
#   region_A = models.ForeignKey(DC_region, related_name="region_A")
#   region_B = models.ForeignKey(Dc_region, related_name="region_B")
