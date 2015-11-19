# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
from bib.models import Book
from defcdb.models import Site, Area, Finds

class VirtualObject(models.Model):
	name = models.CharField(blank=True, null=True, max_length=200)
	upload_file = models.FileField(upload_to='documents/virtualgallery', blank=True, null=True)
	upload_preview = models.FileField(upload_to='documents/virtualgallery', blank=True, null=True)

	def __str__(self):
		return self.name