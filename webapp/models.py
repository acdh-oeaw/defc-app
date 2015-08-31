# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django 
#to create, modify, and delete the table
# Feel free to rename the models, but don't rename 
#db_table values or field names.
#
# Also note: You'll have to insert the output of 
#'django-admin sqlcustom [app_label]'
# into your database.
# PA: Add an encoding decleration on the first line
# PA: Changed fieldname type in class Finds to finds_type because type 
#is a python keyword
# PA: It would ease many things if every class would have the same field 
#name for the field which stores the pirmary key (maybe named "id"),
# e.g. this could be used for writing one list_view template used by all
#classes. 

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect

from django.db import models


class Area(models.Model):
    id_area = models.AutoField(db_column='ID_Area', unique=True,
        primary_key=True)  # Field name made lowercase.
    site = models.ForeignKey('Site', db_column='Site_ID')  # Field name made lowercase.
    areanr = models.CharField(db_column='areaNR', max_length=45,
        blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Area'
        unique_together = (('id_area', 'site'),)
        #had to replace "ID_Area" and 'Site_ID' against the field names
        #because while migrating the error occured: 
        #"'ID_Area' refers to the non-existent field 'ID_Area'""


class Period(models.Model):
    CHRONOLOGICALSSYSTEM_CHOICES =(
        ("Anatolia","Anatolia"),
        ("Crete: Evans/Vagnetti", "Crete: Evans/Vagnetti"),
        ("Crete: Tomkins 2007a","Crete: Tomkins 2007a"),
        ("Cyclades: Attika-Kephala culture", "Cyclades: Attika-Kephala culture"),
        ("Cyclades: Saliagos culture", "Cyclades: Saliagos culture"),
        ("Macedonia/Thrace", "Macedonia/Thrace"),
        ("Renfrew 1968", "Renfrew 1968"),
        ("Thessaly", "Thessaly"),
        )
    PERIOD_CHOICES = (
        ("Pre-Pottery Neolithic", "Pre-Pottery Neolithic"),
        ("Pre-Pottery Neolithic/Neolithic", "Pre-Pottery Neolithic/Neolithic"),
        ("Neolithic", "Neolithic"),
        ("Early Chalcolithic", "Early Chalcolithic"),
        ("Middle Chalcolithic", "Middle Chalcolithic"),
        ("Late Chalcolithic", "Late Chalcolithic"),
        )
    id_period = models.AutoField(db_column='ID_Period', primary_key=True)  # Field name made lowercase.
    chronological_system = models.CharField(max_length=100, blank=True,
        null=True, help_text="PLEASE PROVIDE SOME HELPTEXT", 
        choices=CHRONOLOGICALSSYSTEM_CHOICES)
    period = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX", choices=PERIOD_CHOICES)
    absolute_date_from = models.DateField(auto_now=False,
        auto_now_add=False, blank=True, null=True)
    absolute_date_to = models.DateField(auto_now=False, 
        auto_now_add=False, blank=True, null=True)
    dating_method = models.CharField(max_length=100, blank=True, null=True)
    dated_by = models.CharField(max_length=100, blank=True, null=True)
    c14_calibrated = models.CharField(db_column='C14_calibrated', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c14_absolute_from = models.CharField(db_column='C14_absolute_from', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c14_absolute_to = models.CharField(db_column='C14_absolute_to', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reference_ch = models.CharField(db_column='reference_CH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment_ch = models.CharField(db_column='comment_CH', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Period'

    def __unicode__(self):
        return self.period#comment


class ResearchEvent(models.Model):
    RESEARCHTYPE_CHOICES=(
        ("borehole survey", "borehole survey"),
        ("excavation: rescue", "excavation: rescue"),
        ("excavation: research", "excavation: research"),
        ("excavation: underwater", "excavation: underwater"),
        ("excavation: undetermined", "excavation: undetermined"),
        ("MORE TO COME", "MORE TO COME"),
        )
    INSTITUTION_CHOICES = (
        ("Knickerbockerbande", "Knickerbockerbande"),
        ("Drei Fragezeichen","Drei Fragezeichen"),
        ("No values provided yet","No values provided yet"),
        )
    id_research = models.AutoField(db_column='ID_Research', primary_key=True)  # Field name made lowercase.
    research_type = models.CharField(max_length=100, blank=True,
        null=True, help_text="Methods used for researching the site:",
        choices=RESEARCHTYPE_CHOICES)
    institution = models.CharField(max_length=100, blank=True, null=True,
        help_text="Organisation that carried out a research project at the site.",
        choices=INSTITUTION_CHOICES)
    year_of_activity_start_year = models.DateField(auto_now=False,
        auto_now_add=False, blank=True, null=True,
        help_text="Year when research started.")
    year_of_activity_end_year = models.DateField(auto_now=False,
        auto_now_add=False, blank=True, null=True,
        help_text="Year when research ended.")
    project_name = models.CharField(max_length=100, blank=True, null=True,
        help_text="Name of project.")
    project_id = models.CharField(db_column='project_ID', max_length=100,
        blank=True, null=True, help_text="Project unique identifier.")  # Field name made lowercase.
    project_leader = models.CharField(max_length=100, blank=True, null=True,
        help_text="Leader of the research project.")
    reference_rh = models.CharField(db_column='reference_RH',
        max_length=100, blank=True, null=True, 
        help_text="Bibliographic and web-based reference(s) to publications and other relevant resources related to the project.")  # Field name made lowercase.
    comment_rh = models.CharField(db_column='comment_RH', max_length=100,
        blank=True, null=True,
        help_text="Additional information on the research history not covered in any other field.")  # Field name made lowercase.

    class Meta:
        db_table = 'Research_Event'

    def __unicode__(self):
        return self.research_type


class Settlement(models.Model):
    SETTLEMENTTYPE_CHOICES = (
        ("lowland", "lowland"),
        ("tell", "tell"),
        ("tepe", "tepe"),
        )
    CONSTRUCTIONTYPE_CHOICES = (
        ("apsidal", "apsidal"),
        ("circular", "circular"),
        ("one-room", "one-room"),
        ("rectangular", "rectangular"),
        ("Tsangli house", "Tsangli house"),
        )
    BUILDINGTECHNIQUE_CHOICES = (
        ("mud brick", "mud brick"),
        ("pavement", "pavement"),
        ("pisé", "pisé"),# using é causes an encoding error "non ASCII character ... bu tno encoding declared"
        ("plaster wall", "plaster wall"),
        ("stone socket", "stone socket"),
        ("wattle and daub", "wattle and daub"),
        )
    SPECIAL_FEATURES = (
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
    id_settlements = models.AutoField(db_column='ID_Settlement', primary_key=True)  # Field name made lowercase. 
    description = models.CharField(max_length=100, blank=True, null=True,
        help_text="Free text summary account on the settlement.")
    settlement_type = models.CharField(max_length=100, blank=True, null=True,
        help_text="Classification of settlement.",
        choices=SETTLEMENTTYPE_CHOICES)
    construction_type = models.CharField(max_length=100, blank=True,
        null=True, help_text="Method used for fabricating the buildings.",
        choices=CONSTRUCTIONTYPE_CHOICES)
    building_technique = models.CharField(max_length=100, blank=True,
        null=True, help_text="PLEASE PROVIDE HELPTEXT", 
        choices=BUILDINGTECHNIQUE_CHOICES)
    special_features = models.CharField(max_length=100, blank=True,
        null=True, help_text="Parts of the settlement other than buildings.",
        choices=SPECIAL_FEATURES)
    comment = models.CharField(max_length=100, blank=True, null=True, 
        help_text="Additional information not covered in any other field.")
    reference = models.CharField(max_length=100, blank=True, null=True,
        help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.")
    small_findsid_small_finds = models.IntegerField(db_column='small_findsID_small_finds')  # Field name made lowercase.
    interpretationid_interpretation = models.ForeignKey('Interpretation', db_column='InterpretationID_Interpretation')  # Field name made lowercase.

    class Meta:
        db_table = 'Settlement'

    def __unicode__(self):
        return self.settlement_type.encode('utf8')+'_'+str(self.id_settlements).encode('utf8')

    def get_absolute_url(self):
        return reverse('webapp:settlement_list')

class SettlementArea(models.Model):
    id_settlementArea = models.AutoField(db_column='ID_SettlementArea', primary_key=True) # PA: Added id field
    settlementid_settlements = models.ForeignKey('Settlement', db_column='SettlementID_Settlements')  # Field name made lowercase.
    areaid_area = models.ForeignKey('Area', db_column='AreaID_Area')  # Field name made lowercase.

    class Meta:
        db_table = 'Settlement_Area'
        unique_together = (('settlementid_settlements', 'areaid_area'),)


class Site(models.Model):
    REGION_CHOICES = (
        ("Anatolia/East Aegean", "Anatolia/East Aegean"),
        ("Crete", "Crete"),
        ("Cyclades", "Cyclades"),
        ("Macedonia/Thrace","Southern and Central Greece"),
        ("Thessaly", "Thessaly"),
        )
    PROVINCE_CHOICES =(
        ("Adana", "Adana"),
        ("Adiyaman", "Adiyaman"),
        ("Afyon", "Afyon"),
        ("Agri", "Agri"),
        ("Aksaray", "Aksaray"),
        ("Amasya", "Amasya"),
        ("Ankara", "Ankara"),
        ("Antalya", "Antalya"),
        ("Ardahan", "Ardahan"),
        ("Artvin", "Artvin"),
        ("Aydin", "Aydin"),
        ("Balikesir", "Balikesir"),
        ("Bartin", "Bartin"),
        ("Batman", "Batman"),
        ("Bayburt", "Bayburt"),
        ("Bilecik", "Bilecik"),
        ("Bingol", "Bingol"),
        ("Bitlis", "Bitlis"),
        ("Bolu", "Bolu"),
        ("Burdur", "Burdur"),
        ("Bursa", "Bursa"),
        ("Canakkale", "Canakkale"),
        ("Cankiri", "Cankiri"),
        ("Corum", "Corum"),
        ("Denizli", "Denizli"),
        ("Diyarbakir", "Diyarbakir"),
        ("Dodecanese", "Dodecanese"),
        ("Duzce", "Duzce"),
        ("Edirne", "Edirne"),
        ("Elazig", "Elazig"),
        ("Erzincan", "Erzincan"),
        ("Erzurum", "Erzurum"),
        ("Eskisehir", "Eskisehir"),
        ("Gaziantep", "Gaziantep"),
        ("Giresun", "Giresun"),
        ("Gumushane", "Gumushane"),
        ("Hakkari", "Hakkari"),
        ("Hatay", "Hatay"),
        ("Igdir", "Igdir"),
        ("Isparta", "Isparta"),
        ("Istanbul", "Istanbul"),
        ("Izmir", "Izmir"),
        ("Kahramanmaras", "Kahramanmaras"),
        ("Karabuk", "Karabuk"),
        ("Karaman", "Karaman"),
        ("Kars", "Kars"),
        ("Kastamonu", "Kastamonu"),
        ("Kayseri", "Kayseri"),
        ("Kilis", "Kilis"),
        ("Kirikkale", "Kirikkale"),
        ("Kirklareli", "Kirklareli"),
        ("Kirsehir", "Kirsehir"),
        ("Kocaeli", "Kocaeli"),
        ("Konya", "Konya"),
        ("Kutahya", "Kutahya"),
        ("Malatya", "Malatya"),
        ("Manisa", "Manisa"),
        ("Mardin", "Mardin"),
        ("Mersin", "Mersin"),
        ("Mugla", "Mugla"),
        ("Mus", "Mus"),
        ("Nevsehir", "Nevsehir"),
        ("Nigde", "Nigde"),
        ("Ordu", "Ordu"),
        ("Osmaniye", "Osmaniye"),
        ("Rize", "Rize"),
        ("Sakarya", "Sakarya"),
        ("Samsun", "Samsun"),
        ("Sanliurfa", "Sanliurfa"),
        ("Siirt", "Siirt"),
        ("Sinop", "Sinop"),
        ("Sirnak", "Sirnak"),
        ("Sivas", "Sivas"),
        ("Tekirdag", "Tekirdag"),
        ("Tokat", "Tokat"),
        ("Trabzon", "Trabzon"),
        ("Tunceli", "Tunceli"),
        ("Usak", "Usak"),
        ("Van", "Van"),
        ("Yalova", "Yalova"),
        ("Yozgat", "Yozgat"),
        ("Zonguldak", "Zonguldak"),
        ("Xanthos", "Xanthos"),
        )
    COUNTRY_CHOICES = (
        ("Turkey", "Turkey"),
        ("Greece", "Greece"),
        )
    GPSSYSTEM_CHOICES = (
        ("ED50", "European Datum 1950"),
        ("SAD69", "South American Datum 1969"),
        ("GRS80", "Geodetic Reference System 1980"),
        ("NAD83", "North American Datum 1983"),
        ("WGS84", "World Geodetic System 1984"),
        ("NAVD88", "North America Virtual Datum 1988"),
        ("ETRS89", "European Terrestrial Reference System 1989"),
        ("GCJ02", "Chinese Encrypted Datum 2002"),
        ("EPSG", "European Petrol survey Group"),
        ("UTM", "Universal Transverse Mercator"),


        )

    id_site = models.AutoField(db_column='ID_Site', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=350, blank=True, null=True,
        help_text="Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.")
    region = models.CharField(max_length=50, blank=True,
        null=True, help_text="Geographical area where the site is located.",
        choices=REGION_CHOICES)
    province = models.CharField(max_length=50, blank=True,
        null=True, help_text="Name of the state province where site is located.",
        choices = PROVINCE_CHOICES)
    country = models.CharField(max_length=50, blank=True,
        null=True, help_text="Name of the state where site is located.",
        choices=COUNTRY_CHOICES)
    description = models.CharField(max_length=400, blank=True, null=True,
        help_text="Free text summary account on the site.")
    topography = models.CharField(max_length=50, blank=True, null=True,
        help_text="Description of surface shape and features.")
    gps_data_coordinate_system = models.CharField(db_column='GPS_data_coordinate_system',
        max_length=50, blank=True, null=True,
        help_text="Name of system uniquely determining the position of the site.",
        choices=GPSSYSTEM_CHOICES)  # Field name made lowercase.
    gps_data_n = models.CharField(db_column='GPS_data_N', max_length=50,
        blank=True, null=True, help_text="North value of coordinate.")  # Field name made lowercase.
    gps_data_e = models.CharField(db_column='GPS_data_E', max_length=50,
        blank=True, null=True, help_text="East value of coordinate.")  # Field name made lowercase.
    gps_data_z = models.CharField(db_column='GPS_data_Z', max_length=50,
        blank=True, null=True, help_text="Z value of coordinate (elevation).")  # Field name made lowercase.
    coordinate_source = models.CharField(max_length=100, blank=True, null=True,
        help_text="Bibliographic and web-based references to publications and other relevant information on the site.")
    reference_site = models.CharField(db_column='reference_SITE', max_length=100,
        blank=True, null=True, 
        help_text="Bibliographic and web-based references to publications and other relevant information on the site.")  # Field name made lowercase.

    class Meta:
        db_table = 'Site'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('webapp:site_list')


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
    id_finds = models.AutoField(db_column='ID_Finds', primary_key=True)  # Field name made lowercase.
    finds_type = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX",
        choices=FINDS_TYPE_CHOICES)
    material = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX")
    reference = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX")
    comment = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEX")
    interpretationid_interpretation = models.IntegerField(db_column='InterpretationID_Interpretation')  # Field name made lowercase.
    period_id_period = models.ForeignKey('Period', db_column='Period_ID_Period')  # Field name made lowercase.
    research_event_id_research = models.ForeignKey('ResearchEvent', db_column='Research_Event_ID_Research')  # Field name made lowercase.
    area_id_area = models.ForeignKey(Area, db_column='Area_ID_Area')  # Field name made lowercase.
    area_site = models.ForeignKey(Site, db_column='Area_Site_ID')  # Field name made lowercase. PA: Changed Foreing Key form Area to Site

    class Meta:
        db_table = 'Finds'

    def __unicode__(self):
        return self.finds_type.encode('utf8')+'_'+str(self.id_finds).encode('utf8')

    def get_absolute_url(self):
        return reverse('webapp:finds_list')


class Interpretation(models.Model):
    id_interpretation = models.AutoField(db_column='ID_Interpretation', primary_key=True)  # Field name made lowercase.
    findsid_finds = models.ForeignKey('Finds', db_column='findsID_finds')  # Field name made lowercase.

    class Meta:
        db_table = 'Interpretation'


