# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect
from django.forms import Textarea

from .customTypes import CustomIntegerField


#################################
#			DC-Classes			#
#################################
class DC_reference_type(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True)

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_researchevent_researchtype(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Methods used for researching the site.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return unicode(self.name)

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = unicode(self.__class__.__name__).lower()
		return class_name


class DC_researchevent_institution(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True,
		help_text="Organisation that carried out a research project at the site.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name
		
	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = unicode(self.__class__.__name__).lower()
		return class_name

class DC_researchevent_special_analysis(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True,
		help_text="Analyses other than excavation that were carried out to research the site.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = unicode(self.__class__.__name__).lower()
		return class_name


class DC_site_geographicalreferencesystem(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Name of system uniquely determining the position of the site.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_areatype(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="The type of the area.")

	class Meta:
		ordering = ('name', )                  #to order dropdown lists alphabetically

	def __unicode__(self):
		return self.name


class DC_area_settlementtype(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Classification of settlement.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_settlementstructure(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Layout of settlement.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_constructiontype(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Type of buildings.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_buildingtechnique(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Method used for fabricating the buildings.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_specialfeatures(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Parts of the settlement other than buildings.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_evidenceofgraveshumanremains(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Presence of graves and/or human remains.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_evidenceofoccupation(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Type of evidence indicating occupation found.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_caverockshelterstype(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Type of cave/rockshelter.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_rawmaterial(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Resource that was extracted.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_exploitationtype(models.Model):
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Type of extraction.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_topography(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Connection of the cemetery/graves with other archaeological /natural or modified landscape features.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_mortuaryfeatures(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Parts of the cemetery other than graves.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_gravetype(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Types of graves.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_typeofhumanremains(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="How the humans were treated after death and buried.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_agegroups(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Age.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_sexes(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Sex.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_area_manipulationofgraves(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="If and how the space with the graves is marked.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_type(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )


	def __unicode__(self):
		return self.name


class DC_finds_material(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_amount(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_small_finds_type(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_small_finds_category(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_botany_species(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")
	latin_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_animal_remains_species(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")
	latin_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_animal_remains_completeness(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_animal_remains_part(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_lithics_debitage(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_lithics_modified_tools(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_lithics_core(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )
	
	def __unicode__(self):
		return self.name


class DC_finds_lithics_technology(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_pottery_form(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_pottery_detail(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_finds_pottery_decoration(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_country(models.Model):
	name = models.CharField(max_length=100, blank=True,
		help_text="The name of the country")
	original_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The original or local name of the country")
	authorityfile_id = models.CharField(max_length=100, blank=True,null=True,
		help_text="Identifier provided by some authority file")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_region(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The name of the region")
	original_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The original or local name of the region")
	authorityfile_id = models.CharField(max_length=100, blank=True,null=True,
		help_text="Identifier provided by some authority file")
	country = models.ForeignKey(DC_country, blank=True, null=True,
		help_text="The name of the country")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_province(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The name of the province")
	original_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The original or local name of the province")
	authorityfile_id = models.CharField(max_length=100, blank=True,null=True,
		help_text="Identifier provided by some authority file")
	region = models.ForeignKey(DC_region, blank=True,null=True,
		help_text="The name of the country")

	def __unicode__(self):
		return unicode(self.region)+'_'+self.name

######DCs for Interpretation######
class DC_interpretation_productiontype(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Types of production for which evidence was found.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name

class DC_interpretation_subsistencetype(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Types of livelihood for which evidence was found.")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_chronological_system(models.Model):
	cs_name = models.CharField(max_length=100, blank=True,
 		null=True, help_text="Name of the chronological system.")
	period_name = models.CharField(max_length=100, blank=True,
 		null=True, help_text="Name of archaeological period for which evidence was found.")
	start_date1_BC = CustomIntegerField(blank=True, null=True)
	start_date2_BC = CustomIntegerField(blank=True, null=True)
	end_date1_BC = CustomIntegerField(blank=True, null=True)
	end_date2_BC = CustomIntegerField(blank=True, null=True)
	region = models.ForeignKey(DC_region, blank=True, null=True)


	def __unicode__(self):
		return unicode(self.region)+'_'+unicode(self.cs_name)+'_'+unicode(self.period_name)+'_'+unicode(self.start_date1_BC)


class DC_period_datingmethod(models.Model):
	name= models.CharField(max_length=100, blank=True,
 		null=True, help_text="please provide helptext")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name


class DC_period_datedby(models.Model):
	name= models.CharField(max_length=100, blank=True,
 		null=True, help_text="please provide helptext")

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name



#####################################
#		content tables				#
#####################################


class Reference(models.Model):
	reference_type = models.ForeignKey(DC_reference_type, blank=True,
		null=True, help_text = "The type of the resource.")
	title = models.CharField(max_length=100, blank=True, null=True,
		help_text="The title of the ressource.")
	creator = models.CharField(max_length=100, blank=True, null=True,
		help_text="The person who is main responsible for creating the resource")
	creation_time = CustomIntegerField(min_value=0, max_value=9999,
		blank=True, null=True,
		help_text="The date of the creation date of the ressource.")
	# note: maybe use dc-vocabulary or maybe follow Zotero/Citavi?
	url = models.URLField(max_length=100, blank=True, null=True,
		help_text="The URL to the ressource")

	def __unicode__(self):
		return self.title

class ResearchEvent(models.Model):
	research_type = models.ManyToManyField(DC_researchevent_researchtype,
		blank=True, help_text="Methods used for researching the site.") #mandatory? default?
	institution = models.ManyToManyField(DC_researchevent_institution,
		blank=True, 
		help_text="Organisation that carried out a research project at the site.") #mandatory? default?
	year_of_activity_start_year = CustomIntegerField(min_value=0, max_value=9999,
		blank=True, null=True,
		help_text="Year when research started.") # DateField? optional?
	year_of_activity_end_year = CustomIntegerField(min_value=0, max_value=9999,
		blank=True, null=True,
		help_text="Year when research ended.")  # DateField? optional?
	project_name = models.CharField(max_length=100, blank=True, null=True,
		help_text="Name of project.") #optional?
	project_id = models.CharField(max_length=100, blank=True,
		null=True, help_text="Project unique identifier.") #optional?
	project_leader = models.CharField(max_length=100, blank=True, null=True,
		help_text="Leader of the research project.") #optional?
	special_analysis = models.ManyToManyField(DC_researchevent_special_analysis,
		blank=True,
		help_text="Analyses other than excavation that were carried out to research the site.")
	reference = models.ManyToManyField(Reference, blank=True,
		help_text="Bibliographic and/or web-based reference(s) to publications and other relevant resources related to the project.")
	comment = models.TextField(blank=True, null=True,
		help_text="Additional information on the research history not covered in any other field.")

	#def __unicode__(self):
		#value = ''
		#f len(self.research_type.all()) > 0:
			#value += unicode(self.research_type.all()[0])
		#if len(self.institution.all()) > 0:
			#value += '_' + unicode(self.institution.all()[0])
		#return value
	#def __unicode__(self):
		#return unicode(self.research_type.all()[0])+'_'+unicode(self.institution.all()[0])
	def __unicode__(self):
		return unicode("/".join([unicode(x) for x in self.research_type.all()])+"_"+"/".join([unicode(x) for x in self.institution.all()]))

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = unicode(self.__class__.__name__).lower()
		return class_name

	def get_absolute_url(self):
		return reverse('newModel:researchevent_list')



class Period(models.Model):
	YESNO = (
		("yes", "yes"),
		("no", "no")
		)
	system = models.ForeignKey(DC_chronological_system, blank=True,
		null=True, help_text="Name of the chronological system.")
	dating_method = models.ManyToManyField(DC_period_datingmethod, blank=True,
		help_text="Method used for dating the site.")
	dated_by = models.ManyToManyField(DC_period_datedby, max_length=100,
		blank=True, help_text="Source providing information about date.")
	c14_calibrated = models.CharField(max_length=100, blank=True,
 		null=True, choices = YESNO, help_text="Date is a calibrated date.")
	reference = models.ManyToManyField(Reference, blank=True,
		help_text= "Bibliographic and web-based reference(s) to publications and other relevant resources on the chronology.")
	comment = models.TextField(blank=True, null=True,
		help_text = "Additional information on the chronology not covered in any other field.")

	def get_absolute_url(self):
		return reverse('newModel:period_list')

	def __unicode__(self):
		return unicode(self.system)

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = unicode(self.__class__.__name__).lower()
		return class_name


class Site(models.Model):
	name = models.CharField(max_length=350, blank=True, null=True,
		help_text="Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.")
	alias_name = models.CharField(max_length=350, blank=True, null=True,
		help_text="Alias name of the site.")
	alternative_name = models.CharField(max_length=350, blank=True, null=True,
		help_text="Alternative name of the site.")
	province = models.ForeignKey(DC_province, blank=True, null=True,
		help_text = "Geographical area where the site is located.") #mandatory?
	description = models.TextField(blank=True, null=True,
		help_text="Free text summary account on the site.") #optional?
	topography = models.CharField(max_length=400, blank=True, null=True,
		help_text="Description of surface shape and features.") #optional?
	geographical_coordinate_reference_system = models.ForeignKey(DC_site_geographicalreferencesystem, blank=True,
		null=True, help_text="Name of system uniquely determining the position of the site.")#optional?
	gps_data_n = models.CharField(max_length=50, blank=True, null=True,
		help_text="North value of coordinate.")
	gps_data_e = models.CharField(max_length=50, blank=True,
		null=True, help_text="East value of coordinate.")#optional?
	gps_data_z = models.CharField(max_length=50, blank=True, null=True, 
		help_text="Z value of coordinate (elevation).")#optional?
	coordinate_source = models.CharField(max_length=100, blank=True, 
		null=True,
		help_text="Source providing information about the global position of site.")#optional?
	number_of_activity_periods = models.CharField(max_length=100, blank=True, null=True,
		help_text="Number of times past activity was recorded at the site.")
	reference_site = models.ManyToManyField(Reference, blank=True,
		help_text="Bibliographic and web-based references to publications and other relevant information on the site.")#optional?
	comment = models.TextField(blank=True, null=True,
		help_text="Additional information on the site not covered in any other field.")

	def __unicode__(self):
		return unicode(self.province)+'_'+unicode(self.name)

	def get_absolute_url(self):
		return reverse('newModel:site_list')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = unicode(self.__class__.__name__).lower()
		return class_name


class Area(models.Model):
	GRAVEYESNO = (
		("cemetery", "cemetery"),
		("grave", "grave")
		)
	HUMANREMAINS = (
		("yes", "yes"),
		("no", "no"),
		)
	site = models.ForeignKey(Site, blank=True, null=True,
		help_text="The site where this area is located.")
	area_type = models.ForeignKey(DC_area_areatype, blank=True, null=True,
		help_text = "The type of the area.")
	area_nr = models.CharField(max_length=45, blank=True, null=True, 
		help_text = "An established identifier for this area") #does something like this exist?
	stratigraphical_unit_id = models.CharField(max_length=100, blank=True,
		null=True, 
		help_text="The identifier of the area´s stratigraphical unit")
	geographical_reference = models.CharField(max_length=100, blank=True,
		null=True, help_text="Locates the Area in the Site")
	period = models.ManyToManyField(Period, blank=True,      #what period is this: should be the one created
		help_text="PLEASE PROVIDE SOME HELPTEX")
	description = models.TextField(blank=True, null=True,
		help_text="Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves")
	reference = models.ManyToManyField(Reference, blank=True,
		help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.")
	comment = models.TextField(blank=True, null=True,
		help_text="Additional information not covered in any other field.")
#settlement fields
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
	settlement_human_remains = models.CharField(max_length=3,blank=True,
		null=True, choices=HUMANREMAINS,
		help_text = "Any human remains found in this Settlement?")
#cave&rockshelters fields
	cave_rockshelters_type = models.ForeignKey(DC_area_caverockshelterstype, blank=True,
		null=True,help_text="Type of cave/rockshelter.")
	cave_rockshelters_evidence_of_graves_human_remains = models.ForeignKey(
		DC_area_evidenceofgraveshumanremains, blank=True, null=True,
		help_text="Presence of graves and/or human remains.")
	cave_rockshelters_evidence_of_occupation = models.ManyToManyField(
		DC_area_evidenceofoccupation, blank=True,
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
	grave_number_of_graves = models.CharField(max_length=100,
		blank=True, null=True, help_text="Number of graves.")  #CharField or IntegerField ?
	grave_type =  models.ManyToManyField(DC_area_gravetype,
		blank=True, help_text="Types of graves.")
	grave_type_of_human_remains = models.ManyToManyField(
		DC_area_typeofhumanremains, blank=True,
		help_text="How the humans were treated after death and buried.")
	grave_estimated_number_of_individuals = models.CharField(
		max_length=100, blank=True, null=True,
		help_text="minimum and or maximum")
	grave_age_groups = models.ManyToManyField(DC_area_agegroups,
		blank=True, help_text="Age.")
	grave_sexes = models.ManyToManyField(DC_area_sexes, blank=True,
		help_text="Sex.")
	grave_sexes_number = models.IntegerField(null=True, blank=True, help_text = "Helptext")
	grave_manipulations_of_graves = models.ManyToManyField(
		DC_area_manipulationofgraves, blank=True,
		help_text="If and how the space with the graves is marked.")

	def __unicode__(self):
		"""changed to self.id to avoid dependency due to ForeignKey"""
		#return self.area_type+'_'+unicode(self.id)
		return unicode(self.site)+'_'+unicode(self.area_type)+'_'+unicode(self.id)

	def get_absolute_url(self):
		return reverse('newModel:area_list')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = unicode(self.__class__.__name__).lower()
		return class_name


class Finds(models.Model):
	CONFIDENCE_CHOICES=(
		("1", "1"),
		("2", "2"),
		("3", "3"),
		("4", "4"),
		("5", "5"),
		)
	area = models.ForeignKey(Area, blank=True, null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")
	finds_type = models.ForeignKey(DC_finds_type, blank=True, null=True,
		help_text="Type of the finds.") 
# small finds properties
	small_finds_category = models.ForeignKey(DC_finds_small_finds_category,
		blank=True, null=True,
		help_text="Either a tool, jewellery or figurines")
	small_finds_type = models.ManyToManyField(DC_finds_small_finds_type,
		blank=True, help_text="Type of small find.")
# Botany
	botany_species = models.ManyToManyField(DC_finds_botany_species,
		blank=True, help_text="Species the botanical sample / find belongs to.")
# Animal remains
	animal_remains_species = models.ManyToManyField(
		DC_finds_animal_remains_species,
		blank=True, help_text="Species the zoological sample / find belongs to.")
	animal_remains_completeness = models.ForeignKey(
		DC_finds_animal_remains_completeness,
		blank=True, null=True, help_text="Condition of the zoological sample / find (complete or part).")
	animal_remains_part = models.ManyToManyField(
		DC_finds_animal_remains_part,
		blank=True, help_text="Part of the species the sample / find belongs to.")
# Lithics
	lithics_debitage = models.ManyToManyField(DC_finds_lithics_debitage,
		blank=True, help_text="Which basic form used (for tools).")
	lithics_modified_tools = models.ManyToManyField(
		DC_finds_lithics_modified_tools,
		blank=True,help_text="Kind of tool which was made out of the debitage.")
	lithics_cores = models.ManyToManyField(DC_finds_lithics_core,
		blank=True, help_text="Type of the cores.")
	lithics_technology = models.ManyToManyField(DC_finds_lithics_technology,
		blank=True, help_text="Which technology was used to produce the debitage or tools.")
# Pottery
	pottery_form = models.ManyToManyField(DC_finds_pottery_form,
		blank=True, help_text="Form of pottery.")  #it appears as 'shape' in definitions doc but i kept 'form'
	pottery_detail = models.ManyToManyField(DC_finds_pottery_detail,
		blank=True, help_text="Pottery type.")
	pottery_decoration = models.ManyToManyField(DC_finds_pottery_decoration,
		blank=True, help_text="Type of decoration.")
# common fields
	amount = models.ForeignKey(DC_finds_amount, blank=True, null=True,
		help_text="Amount of finds.")
	material = models.ManyToManyField(DC_finds_material, blank=True,
		help_text="Material used for find.")
	confidence = models.CharField(max_length=50, blank=True, null=True,
		help_text="Confidence in finds", choices = CONFIDENCE_CHOICES)
	research_event = models.ForeignKey(ResearchEvent, blank=True, null=True,
		help_text="Related research event.")
	reference = models.ManyToManyField(Reference, blank=True,
		help_text="Relevant resources on the finds.")
	comment = models.TextField(blank=True, null=True,
		help_text="Additional information not covered in any other field.")


	def get_classname(self):
		class_name = unicode(self.__class__.__name__).lower()
		return class_name

	def get_absolute_url(self):
		return reverse('newModel:finds_list')

	def __unicode__(self):
		return unicode(self.area)+'_'+unicode(self.finds_type)+'_'+unicode(self.id)
	#maybe use Autoslug modul, see:
	# https://pythonhosted.org/django-autoslug/

#######new class Interpretation(this is a chosen name for Subsistence&Production)######
class Interpretation(models.Model):
	finds = models.ManyToManyField(Finds, blank=True,   
		help_text="PLEASE PROVIDE SOME HELPTEX")
	description = models.TextField(blank=True, null=True,
		help_text="Free text summary account on subsistence & production of the site.")
	production_type = models.ManyToManyField(DC_interpretation_productiontype,
		blank=True,	help_text="Types of production for which evidence was found.")
	subsistence_type = models.ManyToManyField(DC_interpretation_subsistencetype,
		blank=True, help_text="Types of livelihood for which evidence was found.")
	reference = models.ManyToManyField(Reference, blank=True,
		help_text="Bibliographic and web-based reference(s)to publications and other relevant resources on industry & subsistence of the site/phase of the site.")
	comment = models.TextField(blank=True, null=True,
		help_text="Additional information on subsistence and production not covered in any other field.")

	def get_classname(self):
		class_name = unicode(self.__class__.__name__).lower()
		return class_name

	def get_absolute_url(self):
		return reverse('newModel:interpretation_list')

	def __unicode__(self):
		return 'Interpretation'+'_'+unicode(self.finds)+'_'+unicode(self.id)
