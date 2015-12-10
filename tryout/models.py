# -*- coding: utf-8 -*-
from django.db import models
from defcdb.models import DC_period_datingmethod, DC_period_datedby, TrackChanges, Site, DC_area_areatype, Book, Period, DC_area_areatype, DC_chronological_system


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
	area_nr = models.CharField(max_length=45, blank=True, null=True, 
		help_text = "An established identifier for this area", 
		verbose_name="Area ID")
	period = models.ForeignKey(DC_chronological_system, blank = True, null =True, 
		help_text="Period defined by the archaeologist",
		related_name="areatry_period")
	dating_method = models.ManyToManyField(DC_period_datingmethod, blank=True,
		help_text="Method used for dating the site.")
	dated_by = models.ManyToManyField(DC_period_datedby, max_length=100,
		blank=True, help_text="Source providing information about date.")
	c14_calibrated = models.CharField(max_length=100, blank=True,                          #moved these fields from Period table
 		null=True, choices = YESNO, help_text="Date is a calibrated date.")
	c14_absolute_from = models.IntegerField(null=True, blank=True, help_text = "Year when archaeological period started.")
	c14_absolute_to = models.IntegerField(null=True, blank=True, help_text = "Year when archaeological period ended.")
	period_reference = models.ManyToManyField(Book, blank=True,
		help_text= "Bibliographic and web-based reference(s) to publications and other relevant resources on the period.",
		related_name="areatry_referenceForPeriod")
	period_comment = models.TextField(blank=True, null=True,
		help_text = "Additional information on the period not covered in any other field.",)
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
