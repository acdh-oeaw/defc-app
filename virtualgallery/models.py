# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
from bib.models import Book
from defcdb.models import Site, Area, Finds

class VirtualObject(models.Model):
	name = models.CharField(blank=True, null=True, max_length=200)
	catalogue_ID = models.CharField(blank=True, null=True, max_length=25,
		help_text = "Value from 'CatalogueID' from 'Pottery_Schachermeyr_bearb'.")
	site = models.ForeignKey(Site, blank=True, null=True,
		help_text="Site the Objectes is related with")
	model_created_by = models.CharField(blank=True, null=True, max_length=250,
		help_text="Name of the person who is responsible for the creation of the 3D model.")
	upload_file = models.FileField(upload_to='documents/virtualgallery',
		blank=True, null=True)
	upload_preview = models.FileField(upload_to='documents/virtualgallery',
		blank=True, null=True)

	def __str__(self):
		return self.name