# -*- coding: utf-8 -*-

from django.db import models


class Reference(models.Model):
	REFERENCETYPE_CHOICES = (
		("printed", "printed"),
		("website", "website"),
		)
	reference_type = models.CharField(max_length=100, blank=True,
		null=True, choices = REFERENCETYPE_CHOICES, 
		help_text = "The type of the ressource.")
	title = models.CharField(max_length=100, blank=True, null=True,
		help_text="The title of the ressource.")
	creator = models.CharField(max_length=100, blank=True, null=True,
		help_text="The person who is main responsible for creating the resource")
	creation_time = models.DateField(blank=True, null=True,
		help_text="The date of the creation date of the ressource")
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


class Region(models.Model):
	name = models.CharField(max_length = 100, blank=True, 
		null=True, help_text="Name of the region. Follow the ???-Standard")
	authorityfile_id = models.CharField(max_length=100, blank=True, null=True,
        help_text="The id of the authoritiy ???, e.g. GeoNames")

	def __unicode__(self):
		return self.name.encode('utf8')


class Province(models.Model):
	name = models.CharField(max_length = 100, blank=True, 
		null=True, help_text="Name of the province. Follow the ???-Standard")
	authorityfile_id = models.CharField(max_length=100, blank=True, null=True,
        help_text="The id of the authoritiy ???, e.g. GeoNames")

	def __unicode__(self):
		return self.name.encode('utf8')


class Country(models.Model):
	name = models.CharField(max_length = 100, blank=True, 
		null=True, help_text="Name of the country/state. Follow the ???-Standard")
	authorityfile_id = models.CharField(max_length=100, blank=True, null=True,
        help_text="The id of the authoritiy ???, e.g. GeoNames")

	def __unicode__(self):
		return self.name.encode('utf8')


class ResearchEvent(models.Model):
	RESEARCHTYPE_CHOICES = (
		("borehole survey", "borehole survey"),
        ("excavation: rescue", "excavation: rescue"),
        ("excavation: research", "excavation: research"),
        ("excavation: underwater", "excavation: underwater"),
        ("excavation: undetermined", "excavation: undetermined"),
        ("MORE TO COME", "MORE TO COME"),
        )
	INSTITUTION_CHOICES = (
		("No values provided yet", "No values provided yet"),
		)
	research_type = models.CharField(max_length=100, blank=True,
        null=True, help_text="Methods used for researching the site:",
        choices=RESEARCHTYPE_CHOICES) #mandatory? default?
	institution = models.CharField(max_length=100, blank=True, null=True,
        help_text="Organisation that carried out a research project at the site.",
        choices=INSTITUTION_CHOICES) #mandatory? default?
	year_of_activity_start_year = models.DateField(auto_now=False,
        auto_now_add=False, blank=True, null=True,
        help_text="Year when research started.") # DateField? optional?
	year_of_activity_end_year = models.DateField(auto_now=False,
        auto_now_add=False, blank=True, null=True,
        help_text="Year when research ended.")  # DateField? optional?
	project = models.ForeignKey(Project, blank=True, null=True,
		help_text = "The project providing the context for the research event.")
# wouldn´t it make sense to exclude these project-related information to 
# another table/class?
	reference = models.ForeignKey(Reference, blank=True, null=True,
		help_text="Bibliographic and/or web-based reference(s) to publications and other relevant resources related to the project.")
	#maybe create an extra table for bibliographic references? use a ManyToMany relation?
	comment = models.CharField(max_length=100, blank=True, null=True,
        help_text="Additional information on the research history not covered in any other field.")

	def __unicode__(self):
		return self.research_type.encode('utf8')+'_'+str(self.id).encode('utf8')


class Period(models.Model):
	CHRONOLOGICAL_SYSTEM_CHOICES = (
		("Anatolia", "Anatolia"),
		("Crete:Evans/Vagnetti", "Crete:Evans/Vagnetti"),
		("Crete:Tomkins 2007a","Crete:Tomkins 2007a"),
		("more to come", "more to come"),
		)
	NAME_CHOICES = (
		("Pre-Pottery Neolithic","Pre-Pottery Neolithic"),
		("Pre-Pottery Neolithic/Neolithic", "Pre-Pottery Neolithic/Neolithic"),
		("Neolithic","Early Chalcolithic"),
		("more to come", "more to come"),
		)
	DATING_METHOD_CHOICES = (
		("radiocarbon dating", "radiocarbon dating"),
		("dendrochronology", "dendrochronology"),
		("material culture", "material culture"),
		("none recorded", "none recorded"),
		)
	DATED_BY_CHOICES = (
		("charcoal", "charcoal"),
		("bone", "bone"),
		("grain", "grain"),
		("Samen", "Samen"),
		)
	chronological_system = models.CharField(max_length=100, blank=True,
		null=True, help_text="Name of chronological reference system used for data entry.",
		choices = CHRONOLOGICAL_SYSTEM_CHOICES) #mandatory/optional? choices in extra table?
	name = models.CharField(max_length=100, blank=True,
		null=True, help_text="Name of archaeological period for which evidence was found.",
		choices = NAME_CHOICES) #mandatory/optional? choices in extra table?
	absolute_date_from = models.CharField(max_length=100, blank=True,
		null=True, help_text="Year when archaeological period started.") #mandatory/optional? change models.DateField?
	# see: http://stackoverflow.com/questions/15857797/bc-dates-in-python
	absolute_date_to = models.CharField(max_length=100, blank=True,
		null=True, help_text="Year when archaeological period ended.") #mandatory/optional? change models.DateField?
	dating_method = models.CharField(max_length=100, blank=True, null=True,
		help_text="Method used for dating the site.",
		choices = DATING_METHOD_CHOICES)
	dated_by = models.CharField(max_length=100, blank=True, null=True,
		choices = DATED_BY_CHOICES,
		help_text="Source providing information about date.") #mandatory/optional?
	c14_calibrated = models.CharField(max_length=100, blank=True, null=True,
		help_text = "Date is a calibrated date.") #mandatory/optional? what kind of values?
	c14_absolute_from = models.CharField(max_length=100, blank=True, null=True,
		help_text = "Year when archaeological period started.") #mandatory/optional? change models.DateField?
	c14_absolute_to = models.CharField(max_length=100, blank=True, null=True,
		help_text = "Year when archaeological period ended.") #mandatory/optional? change models.DateField?
	reference = models.ForeignKey(Reference, blank=True, null=True, 
		help_text= "Bibliographic and web-based reference(s) to publications and other relevant resources on the chronology.")
	#optional? implement an reference table?
	comment = models.CharField(max_length=100, blank=True, null=True, 
		help_text = "Additional information on the chronology not covered in any other field.")
	#optional?

	def __unicode__(self):
		return self.name


class Site(models.Model):
	GPSSYSTEM_CHOICES = (
		("Google map", "Google map"),
        ("GPS", "GPS"),
        ("literature", "literature"),
        )
	name = models.CharField(max_length=350, blank=True, null=True,
        help_text="Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.")
	region = models.ForeignKey(Region, blank=True, null=True,
		help_text = "Geographical area where the site is located.") #mandatory?
	province = models.ForeignKey(Province, blank=True, null=True,
		help_text = "Name of the state province where site is located.") #mandatory?
	country = models.ForeignKey(Country, blank=True, null=True,
		help_text = "Name of the state where site is located.") #mandatory?
	description = models.CharField(max_length=400, blank=True, null=True,
        help_text="Free text summary account on the site.") #optional?
	topography = models.CharField(max_length=400, blank=True, null=True,
        help_text="Description of surface shape and features.") #optional?
	gps_data_coordinate_system = models.CharField(max_length=50, blank=True,
		null=True, choices=GPSSYSTEM_CHOICES,
		help_text="Name of system uniquely determining the position of the site.")#optional?
	gps_data_n = models.CharField(max_length=50, blank=True, null=True,
		help_text="North value of coordinate.")
	gps_data_e = models.CharField(max_length=50, blank=True,
		null=True, help_text="East value of coordinate.")#optional?
	gps_data_z = models.CharField(max_length=50, blank=True, null=True, 
		help_text="Z value of coordinate (elevation).")#optional?
	coordinate_source = models.CharField(max_length=100, blank=True, 
		null=True,
        help_text="Bibliographic and web-based references to publications and other relevant information on the site.")#optional?
	reference_site = models.CharField(max_length=100, blank=True, null=True, 
        help_text="Bibliographic and web-based references to publications and other relevant information on the site.")#optional?

	def __unicode__(self):
		return self.name.encode('utf8')
