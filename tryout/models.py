# -*- coding: utf-8 -*-
from django.db import models
from defcdb.models import * 


class AreaTry(TrackChanges):
	YESNO = (
		("yes", "yes"),
		("no", "no")
		)
	GRAVEYESNO = (
		("cemetery", "cemetery"),
		("grave", "grave")
		)
	HUMANREMAINS = (
		("yes", "yes"),
		("no", "no"),
		)
	site = models.ForeignKey(Site, blank=True, null=True,
		help_text="The site where this area is located.",
		related_name="areatry_site")
	area_type = models.ForeignKey(DC_area_areatype, blank=True, null=True,
		help_text = "The type of the area.")
	area_nr = models.CharField(max_length=45, blank=True, null=True, 
		help_text = "An established identifier for this area", 
		verbose_name="Area ID")
#Period fields
	period = models.ForeignKey(DC_chronological_system, blank = True, null =True, 
		help_text="Chronological period. This contains information about the name, the period, start/enddate1/2, and the region.",
		related_name="areatry_period")
	radiocarbon_dated = models.CharField(max_length=5, blank=True,                          #moved these fields from Period table
 		null=True, choices = YESNO, help_text="Radiocarbon dated?")
	dating_method = models.ManyToManyField(DC_period_datingmethod, blank=True,
		help_text="Method used for dating the site.")
	earliest_date_lab_number = models.CharField(max_length=100, blank=True,                          #moved these fields from Period table
 		null=True, help_text="pleaseProvideSomeHelptext",
 		verbose_name="Earliest date: Lab Number")
	earliest_date_14C_age = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Earliest date: 14C age (BC/BP)")
	earliest_date_14C_age_calibrated = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Earliest date: 14C age calibrated (BC/BP)")
	earliest_date_standard_deviation = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Earliest date: Standard deviation (+/-)")
	earliest_date_delta13 = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Earliest date: delta 13C")
	earliest_date_calibration = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Earliest date: Calibration")
	earliest_date_date_of_calibration = models.DateField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Earliest date: Date of calibration")
	earliest_datedated_by = models.ManyToManyField(DC_period_datedby, max_length=100,
		blank=True, help_text="Source providing information about date.",
		related_name="earliestDatedBy",
		verbose_name="Earliest date: Dated by")
	latest_date_lab_number = models.CharField(max_length=100, blank=True,                          #moved these fields from Period table
 		null=True, help_text="pleaseProvideSomeHelptext",
 		verbose_name="Latest date: Lab Number")
	latest_date_14C_age = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Latest date: 14C age (BC/BP")
	latest_date_14C_age_calibrated = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Latest date: 14C age calibrated (BC/BP)")
	latest_date_standard_deviation = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Latest date: Standard deviation (+/-)")
	latest_date_delta13 = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Latest date: delta 13C")
	latest_date_calibration = models.IntegerField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Latest date: Calibration")
	latest_date_date_of_calibration = models.DateField(null=True, blank=True,
		help_text = "pleaseProvideSomeHelptext",
		verbose_name="Latest date: Date of calibration")
	latest_datedated_by = models.ManyToManyField(DC_period_datedby, max_length=100,
		blank=True, help_text="Source providing information about date.",
		related_name="latestDatedBy",
		verbose_name="Latest date: Dated by")
	period_reference = models.ManyToManyField(Book, blank=True,
		help_text= "Bibliographic and web-based reference(s) to publications and other relevant resources on the period.",
		related_name="areatry_referenceForPeriod")
	period_comment = models.TextField(blank=True, null=True,
		help_text = "Additional information on the period not covered in any other field.",)
	settlement_type = models.ManyToManyField(DC_area_settlementtype, blank=True,
		help_text="Classification of settlement.")
	settlement_structure = models.ManyToManyField(DC_area_settlementstructure,
		blank = True, help_text="Layout of settlement.")
	settlement_construction_type = models.ManyToManyField(DC_area_constructiontype,
		blank=True, help_text="Type of buildings.")
	settlement_building_technique = models.ManyToManyField(DC_area_buildingtechnique,
		blank=True, help_text="Method used for fabricating the buildings.")
	settlement_special_features = models.ManyToManyField(DC_area_specialfeatures,  #it was FK field
		blank=True, help_text="Parts of the settlement other than buildings.")
	settlement_human_remains = models.CharField(max_length=3, blank=True,
		null=True, choices=HUMANREMAINS,
		help_text = "Any human remains found in this Settlement?")
#cave&rockshelters fields
	cave_rockshelters_type = models.ForeignKey(DC_area_caverockshelterstype, 
		verbose_name="Cave/rockshelters type", 
		blank=True, null=True,help_text="Type of cave/rockshelter.")
	cave_rockshelters_human_remains = models.CharField(max_length=3, blank=True,
		null=True, choices=HUMANREMAINS,
		help_text = "Any human remains found in this cave or rockshelter?")
	cave_rockshelters_evidence_of_occupation = models.ManyToManyField(
		DC_area_evidenceofoccupation, verbose_name="Cave/rockshelters: evidence of occupation", blank=True,
		help_text="Type of evidence indicating occupation found.")
#quarry fields
	quarry_exploitation_type = models.ManyToManyField(DC_area_exploitationtype,
		blank=True, help_text="Type of extraction.")
	quarry_raw_material = models.ManyToManyField(DC_area_rawmaterial,
		blank=True, help_text="Resource that was extracted.")
#cemetery/graves fields
	cemetery_or_grave = models.CharField(max_length=100, blank=True,
		null=True, choices=GRAVEYESNO)
	cemetery_or_graves_topography = models.ManyToManyField(DC_area_topography,
		blank=True, help_text="Connection of the cemetery/graves with other archaeological /natural or modified landscape features.")
	cemetery_or_graves_mortuary_features = models.ManyToManyField(DC_area_mortuaryfeatures,
		blank=True,	help_text="Parts of the cemetery other than graves.")
	grave_number_of_graves = models.CharField(verbose_name="Grave: number of graves", max_length=100,
		blank=True, null=True, help_text="Number of graves.")  #CharField or models.IntegerField ?
	grave_type =  models.ManyToManyField(DC_area_gravetype,
		blank=True, help_text="Types of graves.")
	grave_type_of_human_remains = models.ManyToManyField(
		DC_area_typeofhumanremains, verbose_name="Grave: type of human remains", blank=True,
		help_text="How the humans were treated after death and buried.")
	grave_estimated_number_of_individuals = models.CharField(verbose_name="Grave: estimated number of individuals", 
		max_length=100, blank=True, null=True,
		help_text="minimum and or maximum")
	grave_age_groups = models.ManyToManyField(DC_area_agegroups, verbose_name="Grave: age groups", 
		blank=True, help_text="Age.")
	grave_sexes = models.ManyToManyField(DC_area_sexes, verbose_name="Grave: sexes", blank=True,
		help_text="Sex.")
	grave_number_of_female_sex = models.IntegerField(verbose_name="Grave: number of female sex", 
		null=True, blank=True, help_text = "Helptext")
	grave_number_of_male_sex = models.IntegerField(verbose_name="Grave: number of male sex", 
		null=True, blank=True, help_text = "Helptext")
	grave_number_of_not_specified_sex = models.IntegerField(verbose_name="Grave: number of not specified sex", 
		null=True, blank=True, help_text = "Helptext")
	grave_manipulations_of_graves = models.ManyToManyField(
		DC_area_manipulationofgraves, verbose_name="Grave: manipulations of graves", blank=True,
		help_text="If and how the space with the graves is marked.")

	description = models.TextField(blank=True, null=True,
		help_text="Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves")
	reference = models.ManyToManyField(Book, blank=True,
		help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.",
		related_name="areatry_reference")
	comment = models.TextField(blank=True, null=True,
		help_text="Additional information not covered in any other field.")

	class Meta:
		ordering =( 'site',)

	def __str__(self):
		return str(self.site)+'_'+str(self.id)

	def get_absolute_url(self):
		return reverse('defcdb:area_list')
