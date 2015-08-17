from django.db import models

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
	reference = models.CharField(max_length=100, blank=True, null=True, 
		help_text= "Bibliographic and web-based reference(s) to publications and other relevant resources on the chronology.")
	#optional? 
	comment = models.CharField(max_length=100, blank=True, null=True, 
		help_text = "Additional information on the chronology not covered in any other field.")
	#optional?

	def __unicode__(self):
		return self.name





