from django.db import models
from defcdb.models import Finds, ResearchEvent

# Create your models here.
class Contact(models.Model):
	first_name = models.CharField(blank=True, null=True, max_length=500)
	last_name = models.CharField(blank=True, null=True, max_length=500)
	institution = models.ManyToManyField(ResearchEvent, blank=True)


class Project(models.Model):
	name = models.CharField(blank=True, null=True, max_length=500)
	title = models.CharField(blank=True, null=True, max_length=500)
	source = models.CharField(blank=True, null=True, max_length=500)
	contact = models.ManyToManyField(Contact, blank=True)
	language = models.CharField(blank=True, null=True, max_length=500)
	keywords = models.CharField(blank=True, null=True, max_length=500)
	publisher = models.CharField(blank=True, null=True, max_length=500)
	issued = models.CharField(blank=True, null=True, max_length=500)
	license = models.CharField(blank=True, null=True, max_length=500)
	access_rights = models.CharField(blank=True, null=True, max_length=500)


class Threedmodel(models.Model):
	""" in an 1:1 relation to class Finds"""
	finds = models.ForeignKey(Finds, blank=True, null=True)
	part = models.CharField(blank=True, null=True, max_length=500)
	diameter = models.CharField(blank=True, null=True, max_length=500)
	wall_thickness = models.CharField(blank=True, null=True, max_length=500)
	surface_treatment_i = models.CharField(blank=True, null=True, max_length=500)
	surface_treatment_o = models.CharField(blank=True, null=True, max_length=500)
	surface_color_i = models.CharField(blank=True, null=True, max_length=500)
	surface_color_o = models.CharField(blank=True, null=True, max_length=500)
	decoration_color = models.CharField(blank=True, null=True, max_length=500)
	decoration_description = models.CharField(blank=True, null=True, max_length=500)
	fabric_color = models.CharField(blank=True, null=True, max_length=500)
	hardness = models.CharField(blank=True, null=True, max_length=500)
	sorting = models.CharField(blank=True, null=True, max_length=500)
	density = models.CharField(blank=True, null=True, max_length=500)
	pores = models.CharField(blank=True, null=True, max_length=500)
	core_form = models.CharField(blank=True, null=True, max_length=500)
	core_color = models.CharField(blank=True, null=True, max_length=500)
	inclusion_type = models.CharField(blank=True, null=True, max_length=500)
	inclusion_color = models.CharField(blank=True, null=True, max_length=500)
	inclusion_form = models.CharField(blank=True, null=True, max_length=500)
	inclusion_particle_size = models.CharField(blank=True, null=True, max_length=500)
	inclusion_frequency = models.CharField(blank=True, null=True, max_length=500)
	inclusion_hardness = models.CharField(blank=True, null=True, max_length=500)
	resource_metadata = models.ForeignKey(Project, blank=True, null=True)







