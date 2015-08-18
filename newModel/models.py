# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse


#what about persons????

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
        help_text="Source providing information about the global position of site.")#optional?
	reference_site = models.ForeignKey(Reference, blank=True, null=True, 
        help_text="Bibliographic and web-based references to publications and other relevant information on the site.")#optional?

	def __unicode__(self):
		return self.name.encode('utf8')

	def get_absolute_url(self):
		return reverse('newModel:site_list')


class Area(models.Model):
	AREATYPE_CHOICES = (
		("Settlement", "Settlement"),
		("Caves and Rockshelters", "Caves and Rockshelters"),
		("Quarry", "Quarry"),
		("Cemetery/Grave", "Cemetery/Grave"),		
		)
#filds of settlements
	SETTLEMENTTYPE_CHOICES = (
		("lowland", "lowland"),
        ("tell", "tell"),
        ("tepe", "tepe"),
        )	#taken from "\ownCloud\DEFC\Database_Examples_alltables_KB.xlsx"
	CONSTRUCTIONTYPE_CHOICES = (
		("apsidal",  "apsidal"),
        ("circular", "circular"),
        ("one-room", "one-room"),
        ("rectangular", "rectangular"),
        ("Tsangli house", "Tsangli house"),
        )
	BUILDINGTECHNIQUE_CHOICES = (
		("mud brick", "mud brick"),
        ("pavement", "pavement"),
        ("pisé", "pisé"),
        ("plaster wall", "plaster wall"),
        ("stone socket", "stone socket"),
        ("wattle and daub", "wattle and daub"),
        )
	SPECIALFEATURES_CHOICES = (
		("bench", "bench"),
        ("channel", "channel"),
        ("hearth", "hearth"),
        ("pit", "pit"),
        ("post-hole", "post-hole"),
        ("stone setting", "stone setting"),
        ("storage building", "storage building"),
        ("storage pit", "storage pit"),
        ("storage vessel", "storage vessel"),
        ("well", "well"),
        ("oven", "oven"),
        )
#field of caves&rockshelters
	EVIDENCEOFGRAVES_HUMANREMAINS_CHOICES = ( 
        ("not present", "not present"),
        ("present", "present"),
        )
	EVIDENCEOFOCCUPATION_CHOICES = (
		("fire place", "fire place"),
        ("storage facilities", "storage facilities"),
        ("post-hole", "post-hole"),
        ("stone setting", "stone setting"),
        ("pit", "pit"),
        )
	CAVESANDROCKSHELTERSTYPES_CHOICES = (
		("cave", "cave"),
        ("rock shelter", "rock shelter"),
        )
#fields of Quarry
	RAWMATERIAL_CHOICES = (
		("obsidian", "obsidian"),
        ("copper", "copper"),
        ("limestone", "limestone"),
        ("flint", "flint"),
        ("chert", "chert"),
        ("clay", "clay"),
        )
	EXPLOITATIONTYPE_CHOICES = (
		("pinge", "pinge"),
        ("shaft mining", "shaft mining"),
        ("surface", "surface"),
        )
#fields of Cemetery/Graves
	TOPOGRAPHY_CHOICES = (
		("intra mural", "intra mural"),
        ("extra mural", "extra mural"),
        ("in cave", "in cave"),
        ("next to cave", "next to cave"),
        ("part of house", "part of house"),
        )
	MORTUARYFEATURES_CHOICES = (
		("pyre", "pyre"),
        ("separating wall", "separating wall"),
        ("platform", "platform"),
        )
	GRAVETYPES_CHOICES = (
		("cist grave", "cist grave"),
        ("pit grave", "pit grave"),
        ("vessel", "vessel"),
        ("none recorded", "none recorded"),
        )
	TYPEOFHUMANREMAINS_CHOICES = (
		("cremations", "cremations"),
        ("inhumations: complete bodies", "inhumations: complete bodies"),
        ("secondary deposition", "secondary deposition"),
        )
	AGEGROUPS_CHOICES = (
		("neonate", "neonate"),
        ("infans I (0-6)", "infans I (0-6)"),
        ("infans II (7-12)", "infans II (7-12)"),
        ("juvenile (13-18)", "juvenile (13-18)"),
        ("adult (19-40)", "adult (19-40)"),
        ("adult-mature (19-45)", "adult-mature (19-45)"),
        ("mature (41-60)", "mature (41-60)"),
        ("mature-senile (51-70)", "mature-senile (51-70)"),
        ("senile (60-)", "senile (60-)"),
        ("not recorded", "not recorded"),
        ("part of specialist report", "part of specialist report"),
        ("immature", "immature"),
        ("mature", "mature"),
        ("children", "children"),
        ("adults", "adults"),
        )
	SEXES_CHOICES = (
		("male individuals: no.", "male individuals: no."),
        ("female individuals: no.", "female individuals: no."),
        ("not specified: no.", "not specified: no."),
        ("part of specialist report", "part of specialist report"),
        )
	MANIPULATIONOFGRAVES_CHOICES = (
		("consecutive burials", "consecutive burials"),
        ("construction of settlement", "construction of settlement"),
        ("looting", "looting"),
        ("none recorded", "none recorded"),
        )
#common fields for area	
	site = models.ForeignKey(Site, blank=True, null=True,
		help_text="The site where this area is located.")
	area_type = models.CharField(max_length=100, blank=True, null=True,
		help_text = "The type of the area", choices=AREATYPE_CHOICES)
	area_nr = models.CharField(max_length=45,blank=True, null=True, 
		help_text = "An established identifier for this area") #does something like this exist?
	period = models.ForeignKey(Period, blank=True, null=True, 
		help_text="PLEASE PROVIDE SOME HELPTEX")
	description = models.CharField(max_length=100, blank=True, null=True,
        help_text="Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves")
	reference = models.ForeignKey(Reference, blank=True, null=True,
        help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.")
#settlement fields
	settlement_type = models.CharField(max_length=100, blank=True, null=True,
        help_text="Classification of settlement.",
        choices=SETTLEMENTTYPE_CHOICES)
	settlement_constructiontype = models.CharField(max_length=100,
		blank=True, null=True, help_text="Type of buildings.", 
		choices=CONSTRUCTIONTYPE_CHOICES)
	settlement_building_technique = models.CharField(max_length=100, blank=True,
        null=True, help_text="Method used for fabricating the buildings.",
        choices = BUILDINGTECHNIQUE_CHOICES)
	settlement_special_features = models.CharField(max_length=100,
		blank=True, null=True, choices=SPECIALFEATURES_CHOICES,
        help_text="Parts of the settlement other than buildings.")
#cave&rockshelters fields
	cave_rockshelters_type = models.CharField(max_length=100, blank=True,
		null=True,
        help_text="Type of cave/rockshelter.",
        choices=CAVESANDROCKSHELTERSTYPES_CHOICES)
	cave_rockshelters_evidence_of_graves_human_remains = models.CharField(
		max_length=100, blank=True, null=True,
        help_text="Presence of graves and/or human remains.",
        choices=EVIDENCEOFGRAVES_HUMANREMAINS_CHOICES)
	cave_rockshelters_evidence_of_occupation = models.CharField(
		max_length=100, blank=True, null=True,
        help_text="Type of evidence indicating occupation found.",
        choices=EVIDENCEOFOCCUPATION_CHOICES)
#quarry fields
	quarry_exploitation_type = models.CharField(max_length=100, blank=True,
		null=True, help_text="Type of extraction.",
		choices=EXPLOITATIONTYPE_CHOICES)
	quarry_raw_material = models.CharField(max_length=100, blank=True, null=True,
        help_text="Resource that was extracted.",
        choices=RAWMATERIAL_CHOICES)
#cemetery/graves fields
	cemetery_graves_topography = models.CharField(max_length=100,
		blank=True, null=True,
        help_text="Connection of the cemetery/graves with other archaeological /natural or modified landscape features.",
        choices=TOPOGRAPHY_CHOICES)
	cemetery_graves_mortuary_features = models.CharField(max_length=100,
		blank=True, null=True,
        help_text="Parts of the cemetery other than graves.",
        choices=MORTUARYFEATURES_CHOICES)
	cemetery_graves_number_of_graves = models.CharField(max_length=100,
		blank=True, null=True, help_text="Number of graves.")  #CharField or IntegerField ?
	cemetery_graves_grave_type =  models.CharField(max_length=100,
		blank=True, null=True, help_text="Types of graves.",
		choices=GRAVETYPES_CHOICES)
	cemetery_graves_type_of_human_remains = models.CharField(max_length=100,
		blank=True, null=True, choices=TYPEOFHUMANREMAINS_CHOICES,
		help_text="How the humans were treated after death and buried.")
	cemetery_graves_estimated_number_of_individuals = models.CharField(
		max_length=100, blank=True, null=True,
		help_text="minimum and or maximum")
	cemetery_graves_age_groups = models.CharField(max_length=100, blank=True,
		null=True, help_text="Age.", choices=AGEGROUPS_CHOICES)
	cemetery_graves_sexes = models.CharField(max_length=100, blank=True,
		null=True, help_text="Sex", choices=SEXES_CHOICES)
	cemetery_graves_manipulations_of_graves = models.CharField(
    	max_length=100, blank=True, null=True,
        help_text="If and how the space with the graves is marked.",
        choices=MANIPULATIONOFGRAVES_CHOICES)

	def __unicode__(self):
		return self.area_type.encode('utf8')

	def get_absolute_url(self):
		return reverse('newModel:area_list')
###################################################
#Not sure about this
#small_findsid_small_finds = models.IntegerField(models.CharField(
#	max_length=100, blank=True, null=True)  # small finds and finds are the same or not?
#interpretationid_interpretation = models.ForeignKey('Interpretation', ) 
#what is this?type of field (plain text or int)?
########################################################

class Finds(models.Model):
    FINDS_TYPE_CHOICES = (
        ("Fire dog", "Fire dog"),
        ("Arrowshaft smoother", "Arrowshaft smoother"),
        ("Bucranium", "Bucranium"),
        ("and many more", "and many more"),
        )
    MATERIAL_CHOICES = (
        ("stone", "stone"),
        ("obsidian", "obsidian"),
        ("fabrics", "fabrics"),
        ("and some more", "and some more"),
        )
    finds_type = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX",
        choices=FINDS_TYPE_CHOICES)
    material = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX")
    reference = models.ForeignKey(Reference, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX")
    comment = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX")
    #interpretationid_interpretation = models.IntegerField(db_column='InterpretationID_Interpretation')
    area = models.ForeignKey(Area, blank=True, null=True,
    	help_text="PLEASE PROVIDE SOME HELPTEX") 
    research_event = models.ForeignKey(ResearchEvent, blank=True, null=True,
    	help_text="PLEASE PROVIDE SOME HELPTEX")
    def __unicode__(self):
        return self.finds_type.encode('utf8')+'_'+str(self.id_finds).encode('utf8')
