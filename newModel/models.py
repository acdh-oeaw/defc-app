# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from .customTypes import CustomIntegerField

#what about persons????

#################################
#			DC-Classes			#
#################################
class DC_reference_type(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True)

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_researchevent_researchtype(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Methods used for researching the site.")

	def __unicode__(self):
		return self.name

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name


class DC_researchevent_institution(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Organisation that carried out a research project at the site.")

	def __unicode__(self):
		return self.name.encode('utf8')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name

class DC_researchevent_special_analysis(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True,
		help_text="Analyses other than excavation that were carried out to research the site.")

	def __unicode__(self):
		return self.name.encode('utf8')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name


class DC_period_chronologicalsystem(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Name of chronological reference system used for data entry.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_period_name(models.Model):    #added 'period' in order to avoid ambiguity (Ksenia)
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Name of archaeological period for which evidence was found.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_period_datingmethod(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Method used for dating the site.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_period_datedby(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Source providing information about date.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_site_gpssystem(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Name of system uniquely determining the position of the site.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_areatype(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="The type of the area.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_settlementtype(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Classification of settlement.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_constructiontype(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Type of buildings.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_buildingtechnique(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Method used for fabricating the buildings.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_specialfeatures(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Parts of the settlement other than buildings.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_evidenceofgraveshumanremains(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Presence of graves and/or human remains.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_evidenceofoccupation(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Type of evidence indicating occupation found.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_caverockshelterstype(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Type of cave/rockshelter.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_rawmaterial(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Resource that was extracted.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_exploitationtype(models.Model):
	name = models.CharField(max_length=100, blank=True,
        null=True, help_text="Type of extraction.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_topography(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Connection of the cemetery/graves with other archaeological /natural or modified landscape features.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_mortuaryfeatures(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Parts of the cemetery other than graves.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_gravetype(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Types of graves.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_typeofhumanremains(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="How the humans were treated after death and buried.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_agegroups(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Age.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_sexes(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="Sex.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_area_manipulationofgraves(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="If and how the space with the graves is marked.")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_type(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_material(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_amount(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_small_finds_type(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_small_finds_category(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_botany_species(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")
	latin_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_animal_remains_species(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")
	latin_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_animal_remains_completeness(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_animal_remains_part(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_lithics_debitage(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_lithics_modified_tools(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_lithics_core(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_lithics_technology(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_pottery_form(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_pottery_detail(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')


class DC_finds_pottery_decoration(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="PLEASE PROVIDE SOME HELPTEX")

	def __unicode__(self):
		return self.name.encode('utf8')

class DC_province(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The name of the province")
	original_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The original or local name of the province")
	authorityfile_id = models.CharField(max_length=100, blank=True,null=True,
		help_text="Identifier provided by some authority file")

	def __unicode__(self):
		return self.name.encode('utf8')

class DC_country(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The name of the country")
	original_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The original or local name of the country")
	authorityfile_id = models.CharField(max_length=100, blank=True,null=True,
		help_text="Identifier provided by some authority file")

	def __unicode__(self):
		return self.name.encode('utf8')



class DC_region(models.Model):
	name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The name of the region")
	original_name = models.CharField(max_length=100, blank=True,null=True,
		help_text="The original or local name of the region")
	authorityfile_id = models.CharField(max_length=100, blank=True,null=True,
		help_text="Identifier provided by some authority file")
	province = models.ForeignKey(DC_province, blank=True,null=True,
		help_text="The name of the region")
	country = models.ForeignKey(DC_country, blank=True,null=True,
		help_text="The name of the region")

	def __unicode__(self):
		return self.name.encode('utf8')



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
		return self.title.encode('utf8')


class Project(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True,
        help_text="Name of project.") #optional?
	project_id = project_id = models.CharField(max_length=100, blank=True,
		null=True, help_text="Project unique identifier.") #optional?
	project_leader = models.CharField(max_length=100, blank=True, null=True,
        help_text="Leader of the research project.") #optional?

	def __unicode__(self):
		return self.name.encode('utf8')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name


class Region(models.Model):
	name = models.ForeignKey(DC_region, blank=True, 
		null=True, help_text="Name of the region. Follow the ???-Standard")

	def __unicode__(self):
		return self.name.encode('utf8')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name


class Province(models.Model):
	name = models.CharField(max_length = 100, blank=True, 
		null=True, help_text="Name of the province. Follow the ???-Standard")
	authorityfile_id = models.CharField(max_length=100, blank=True, null=True,
        help_text="The id of the authoritiy ???, e.g. GeoNames")

	def __unicode__(self):
		return self.name.encode('utf8')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name


class Country(models.Model):
	name = models.CharField(max_length = 100, blank=True, 
		null=True, help_text="Name of the country/state. Follow the ???-Standard")
	authorityfile_id = models.CharField(max_length=100, blank=True, null=True,
        help_text="The id of the authoritiy ???, e.g. GeoNames")

	def __unicode__(self):
		return self.name.encode('utf8')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name


class ResearchEvent(models.Model):
	research_type = models.ForeignKey(DC_researchevent_researchtype, blank=True,
        null=True, help_text="Methods used for researching the site.") #mandatory? default?
	institution = models.ForeignKey(DC_researchevent_institution, blank=True, null=True,
        help_text="Organisation that carried out a research project at the site.") #mandatory? default?
	year_of_activity_start_year = CustomIntegerField(min_value=0, max_value=9999,
		blank=True, null=True,
        help_text="Year when research started.") # DateField? optional?
	year_of_activity_end_year = CustomIntegerField(min_value=0, max_value=9999,
		blank=True, null=True,
        help_text="Year when research ended.")  # DateField? optional?
	project = models.ForeignKey(Project, blank=True, null=True,
		help_text = "The project providing the context for the research event.")
	special_analysis = models.ForeignKey(DC_researchevent_special_analysis,
		blank=True, null=True,
		help_text="Analyses other than excavation that were carried out to research the site.")
	reference = models.ManyToManyField(Reference, blank=True,
		help_text="Bibliographic and/or web-based reference(s) to publications and other relevant resources related to the project.")
	comment = models.CharField(max_length=100, blank=True, null=True,
        help_text="Additional information on the research history not covered in any other field.")

	def __unicode__(self):
		"""changed to self.id to avoid dependency due to ForeignKey"""
		#return self.area_type.encode('utf8')+'_'+str(self.id).encode('utf8')
		#return str(self.id).encode('utf8')
		return str(self.research_type)+'_'+str(self.institution)+'_'+str(self.id).encode('utf8')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name

	def get_absolute_url(self):
		return reverse('newModel:researchevent_list')

class Period(models.Model):
	chronological_system = models.ForeignKey(DC_period_chronologicalsystem, blank=True,
		null=True, help_text="Name of chronological reference system used for data entry.") #mandatory/optional? choices in extra table?
	name = models.ForeignKey(DC_period_name, blank=True,
		null=True, help_text="Name of archaeological period for which evidence was found.") #mandatory/optional? choices in extra table?
	absolute_date_from = CustomIntegerField(min_value=-9999999, max_value=9999,
		blank=True, null=True, help_text="Year when archaeological period started.") #mandatory/optional? 
	absolute_date_to = CustomIntegerField(min_value=-9999999, max_value=9999,
		blank=True, null=True, 
		help_text="Year when archaeological period ended.") #mandatory/optional? 
	dating_method = models.ForeignKey(DC_period_datingmethod, blank=True, null=True,
		help_text="Method used for dating the site.")
	dated_by = models.ForeignKey(DC_period_datedby, blank=True, null=True,
		help_text="Source providing information about date.") #mandatory/optional?
	c14_calibrated = models.CharField(max_length=100, blank=True, null=True,
		help_text = "Date is a calibrated date.") #mandatory/optional? what kind of values?
	c14_absolute_from = models.CharField(max_length=100, blank=True, null=True,
		help_text = "Year when archaeological period started.") #mandatory/optional? change models.DateField?
	c14_absolute_to = models.CharField(max_length=100, blank=True, null=True,
		help_text = "Year when archaeological period ended.") #mandatory/optional? change models.DateField?
	reference = models.ManyToManyField(Reference, blank=True,
		help_text= "Bibliographic and web-based reference(s) to publications and other relevant resources on the chronology.")
	#optional? implement an reference table?
	comment = models.CharField(max_length=100, blank=True, null=True, 
		help_text = "Additional information on the chronology not covered in any other field.")

	def get_absolute_url(self):
		return reverse('newModel:period_list')

	def __unicode__(self):
		return str(self.chronological_system)+'_'+str(self.name)+' ('+str(self.absolute_date_from)+' to' +str(self.absolute_date_to)+')'

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name


class Site(models.Model):
	name = models.CharField(max_length=350, blank=True, null=True,
        help_text="Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.")
	region = models.ForeignKey(DC_region, blank=True, null=True,
		help_text = "Geographical area where the site is located.") #mandatory?
	description = models.CharField(max_length=400, blank=True, null=True,
        help_text="Free text summary account on the site.") #optional?
	topography = models.CharField(max_length=400, blank=True, null=True,
        help_text="Description of surface shape and features.") #optional?
	gps_data_coordinate_system = models.ForeignKey(DC_site_gpssystem, blank=True,
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
	reference_site = models.ManyToManyField(Reference, blank=True,
		help_text="Bibliographic and web-based references to publications and other relevant information on the site.")#optional?

	def __unicode__(self):
		return str(self.region)+'_'+self.name.encode('utf8')

	def get_absolute_url(self):
		return reverse('newModel:site_list')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name


class Area(models.Model):
	site = models.ForeignKey(Site, blank=True, null=True,
		help_text="The site where this area is located.")
	area_type = models.ForeignKey(DC_area_areatype, blank=True, null=True,
		help_text = "The type of the area.")
	area_nr = models.CharField(max_length=45,blank=True, null=True, 
		help_text = "An established identifier for this area") #does something like this exist?
	stratigraphical_unit_id = models.CharField(max_length=100, blank=True,
		null=True, 
		help_text="The identifier of the area´s stratigraphical unit")
	geographical_reference = models.CharField(max_length=100, blank=True,
		null=True, help_text="Locats the Area in the Site")
	period = models.ForeignKey(Period, blank=True, null=True, 
		help_text="PLEASE PROVIDE SOME HELPTEX")
	description = models.CharField(max_length=100, blank=True, null=True,
        help_text="Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves")
	reference = models.ManyToManyField(Reference, blank=True,
		help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.")
#settlement fields
	settlement_type = models.ForeignKey(DC_area_settlementtype, blank=True, null=True,
        help_text="Classification of settlement.")
	settlement_constructiontype = models.ForeignKey(DC_area_constructiontype,
		blank=True, null=True, help_text="Type of buildings.")
	settlement_building_technique = models.ForeignKey(DC_area_buildingtechnique, blank=True,
        null=True, help_text="Method used for fabricating the buildings.")
	settlement_special_features = models.ForeignKey(DC_area_specialfeatures,
		blank=True, null=True, help_text="Parts of the settlement other than buildings.")
#cave&rockshelters fields
	cave_rockshelters_type = models.ForeignKey(DC_area_caverockshelterstype, blank=True,
		null=True,help_text="Type of cave/rockshelter.")
	cave_rockshelters_evidence_of_graves_human_remains = models.ForeignKey(
		DC_area_evidenceofgraveshumanremains, blank=True, null=True,
        help_text="Presence of graves and/or human remains.")
	cave_rockshelters_evidence_of_occupation = models.ForeignKey(
		DC_area_evidenceofoccupation, blank=True, null=True,
        help_text="Type of evidence indicating occupation found.")
#quarry fields
	quarry_exploitation_type = models.ForeignKey(DC_area_exploitationtype, blank=True,
		null=True, help_text="Type of extraction.")
	quarry_raw_material = models.ForeignKey(DC_area_rawmaterial, blank=True, null=True,
        help_text="Resource that was extracted.")
#cemetery/graves fields
	cemetery_graves_topography = models.ForeignKey(DC_area_topography,
		blank=True, null=True,
        help_text="Connection of the cemetery/graves with other archaeological /natural or modified landscape features.")
	cemetery_graves_mortuary_features = models.ForeignKey(DC_area_mortuaryfeatures,
		blank=True, null=True,
        help_text="Parts of the cemetery other than graves.")
	cemetery_graves_number_of_graves = models.CharField(max_length=100,
		blank=True, null=True, help_text="Number of graves.")  #CharField or IntegerField ?
	cemetery_graves_grave_type =  models.ForeignKey(DC_area_gravetype,
		blank=True, null=True, help_text="Types of graves.")
	cemetery_graves_type_of_human_remains = models.ForeignKey(
		DC_area_typeofhumanremains,
		blank=True, null=True, 
		help_text="How the humans were treated after death and buried.")
	cemetery_graves_estimated_number_of_individuals = models.CharField(
		max_length=100, blank=True, null=True,
		help_text="minimum and or maximum")
	cemetery_graves_age_groups = models.ForeignKey(DC_area_agegroups, blank=True,
		null=True, help_text="Age.")
	cemetery_graves_sexes = models.ForeignKey(DC_area_sexes, blank=True,
		null=True, help_text="Sex.")
	cemetery_graves_manipulations_of_graves = models.ForeignKey(
    	DC_area_manipulationofgraves, blank=True, null=True,
        help_text="If and how the space with the graves is marked.")

	def __unicode__(self):
		"""changed to self.id to avoid dependency due to ForeignKey"""
		#return self.area_type.encode('utf8')+'_'+str(self.id).encode('utf8')
		return str(self.site)+'_'+str(self.area_type)+'_'+str(self.id)

	def get_absolute_url(self):
		return reverse('newModel:area_list')

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name
###################################################
#Not sure about this
#small_findsid_small_finds = models.IntegerField(models.CharField(
#	max_length=100, blank=True, null=True)  # small finds and finds are the same or not?
#interpretationid_interpretation = models.ForeignKey('Interpretation', ) 
#what is this?type of field (plain text or int)?
########################################################


class Finds(models.Model):
    area = models.ForeignKey(Area, blank=True, null=True,
    	help_text="PLEASE PROVIDE SOME HELPTEX")
    finds_type = models.ForeignKey(DC_finds_type, blank=True, null=True, 
    	help_text="PLEASE PROVIDE SOME HELPTEX") 
# small finds properties
    small_finds_type = models.ForeignKey(DC_finds_small_finds_type,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
    small_finds_category = models.ForeignKey(DC_finds_small_finds_category,
		blank=True, null=True, 
		help_text="either a tool, jewellery or figurines")
# Botany
    botany_species = models.ForeignKey(DC_finds_botany_species,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
# Animal remains
    animal_remains_species = models.ForeignKey(DC_finds_animal_remains_species,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
    animal_remains_completeness = models.ForeignKey(DC_finds_animal_remains_completeness,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
    animal_remains_part = models.ForeignKey(DC_finds_animal_remains_part,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
# Lithics
    lithics_debitage = models.ForeignKey(DC_finds_lithics_debitage,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
    lithics_modified_tools = models.ForeignKey(DC_finds_lithics_modified_tools,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
    lithics_cores = models.ForeignKey(DC_finds_lithics_core,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
    lithics_technology = models.ForeignKey(DC_finds_lithics_technology,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
# Pottery
    pottery_form = models.ForeignKey(DC_finds_pottery_form,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
    pottery_detail = models.ForeignKey(DC_finds_pottery_detail,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
    pottery_decoration = models.ForeignKey(DC_finds_pottery_decoration,
		blank=True, null=True, help_text="PLEASE PROVIDE SOME HELPTEX")
# common fields
    amount = models.ForeignKey(DC_finds_amount, blank=True, null=True,
    	help_text="PLEASE PROVIDE SOME HELPTEX")
    material = models.ForeignKey(DC_finds_material, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX")
    research_event = models.ForeignKey(ResearchEvent, blank=True, null=True,
    	help_text="PLEASE PROVIDE SOME HELPTEX")
    reference = models.ManyToManyField(Reference, blank=True,
        help_text="PLEASE PROVIDE SOME HELPTEX")
    comment = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX")


    def get_classname(self):
    	class_name = str(self.__class__.__name__).lower()
    	return class_name

    def get_absolute_url(self):
    	return reverse('newModel:finds_list')

    def __unicode__(self):
    	return str(self.area)+'_'+str(self.finds_type)+'_'+str(self.id)
    #maybe use Autoslug modul, see:
    # https://pythonhosted.org/django-autoslug/
