# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Area(models.Model):
    id_area = models.AutoField(db_column='ID_Area', unique=True, primary_key=True)  
    # Field name made lowercase.
    site = models.ForeignKey('Site', db_column='Site_ID')  
    # Field name made lowercase.
    areanr = models.CharField(db_column='areaNR', max_length=45, blank=True, null=True)  
    # Field name made lowercase.

    class Meta:
        db_table = 'Area'
        unique_together = (('id_area', 'site'),)
        #had to replace "ID_Area" and 'Site_ID' against the field names
        #because while migrating the error occured: 
        #"'ID_Area' refers to the non-existent field 'ID_Area'""


class Period(models.Model):
    CHRONOLOGICALSSYSTEM_CHOICES = (
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
    chronological_system = models.CharField(max_length=100, blank=True, null=True,
        help_text="PLEASE PROVIDE SOME HELPTEXT",
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


class ResearchEvent(models.Model):
    id_research = models.AutoField(db_column='ID_Research', primary_key=True)  # Field name made lowercase.
    research_type = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    year_of_activity_start_year = models.CharField(max_length=100, blank=True, null=True)
    year_of_activity_end_year = models.CharField(max_length=100, blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.CharField(db_column='project_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    project_leader = models.CharField(max_length=100, blank=True, null=True)
    reference_rh = models.CharField(db_column='reference_RH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment_rh = models.CharField(db_column='comment_RH', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Research_Event'


class Site(models.Model):
    
    REGION_CHOICES_EN = (
        ("Anatolia/East Aegean", "Anatolia/East Aegean"),
        ("Crete", "Crete"),
        ("Cyclades", "Cyclades"),
        ("Macedonia/Thrace","Southern and Central Greece"),
        ("Thessaly", "Thessaly"),
        )
    PROVINCE_CHOICES_EN =(
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
        ("Google map", "Google map"),
        ("GPS", "GPS"),
        ("literature", "literature"),
        )

    id_sites = models.AutoField(db_column='ID_Site', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=350, blank=True, null=True,
        help_text="Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.")
    name_geonames = models.CharField(max_length=20, blank=True, null=True,
        help_text="Holds the GeoNames-ID belonging to the name-field") # or any other usable id-provider
    region = models.CharField(max_length=50, blank=True,
        null=True, help_text="Geographical area where the site is located.", 
        choices=REGION_CHOICES_EN)
    province = models.CharField(max_length=50, blank=True,
        null=True, help_text="Name of the state province where site is located.",
        choices = PROVINCE_CHOICES_EN)
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
	
    def __str__(self):
        return self.name	


class Finds(models.Model):
    id_finds = models.AutoField(db_column='ID_finds', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    interpretationid_interpretation = models.IntegerField(db_column='InterpretationID_Interpretation')  # Field name made lowercase.
    period_id_period = models.ForeignKey(Period, db_column='Period_ID_Period')  # Field name made lowercase.
    research_event_id_research = models.ForeignKey(ResearchEvent, db_column='Research_Event_ID_Research')  # Field name made lowercase.
    area_id_area = models.ForeignKey(Area, db_column='Area_ID_Area', related_name='ID_Area')  # Field name made lowercase.
    area_site = models.ForeignKey(Area, db_column='Area_Site_ID', related_name='Site')  # Field name made lowercase.
#here I had to add 'related'
    class Meta:
        db_table = 'finds'
