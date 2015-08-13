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
    id_area = models.AutoField(db_column='ID_Area', unique=True, primary_key=True)  # Field name made lowercase.
    site = models.ForeignKey('Site', db_column='Site_ID')  # Field name made lowercase.
    areanr = models.CharField(db_column='areaNR', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Area'
        unique_together = (('id_area', 'site'),)


class Interpretation(models.Model):
    id_interpretation = models.AutoField(db_column='ID_Interpretation', primary_key=True)  # Field name made lowercase.
    findsid_finds = models.ForeignKey('Finds', db_column='findsID_finds')  # Field name made lowercase.

    class Meta:
        db_table = 'Interpretation'


class Period(models.Model):
    id_period = models.AutoField(db_column='ID_Period', primary_key=True)  # Field name made lowercase.
    chronological_system = models.CharField(max_length=100, blank=True, null=True)
    period = models.CharField(max_length=100, blank=True, null=True)
    absolute_date_from = models.CharField(max_length=100, blank=True, null=True)
    absolute_date_to = models.CharField(max_length=100, blank=True, null=True)
    dating_method = models.CharField(max_length=100, blank=True, null=True)
    dated_by = models.CharField(max_length=100, blank=True, null=True)
    c14_calibrated = models.CharField(db_column='C14_calibrated', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c14_absolute_from = models.CharField(db_column='C14_absolute_from', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c14_absolute_to = models.CharField(db_column='C14_absolute_to', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reference_ch = models.CharField(db_column='reference_CH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment_ch = models.CharField(db_column='comment_CH', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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
        managed = False
        db_table = 'Research_Event'


class Settlement(models.Model):
    id_settlements = models.AutoField(db_column='ID_Settlement', primary_key=True)  # Field name made lowercase. 
    description = models.CharField(max_length=100, blank=True, null=True)
    settlement_type = models.CharField(max_length=100, blank=True, null=True)
    construction_type = models.CharField(max_length=100, blank=True, null=True)
    building_technique = models.CharField(max_length=100, blank=True, null=True)
    special_features = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    small_findsid_small_finds = models.IntegerField(db_column='small_findsID_small_finds')  # Field name made lowercase.
    interpretationid_interpretation = models.ForeignKey(Interpretation, db_column='InterpretationID_Interpretation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Settlement'


class SettlementArea(models.Model):
    id_settlementArea = models.AutoField(db_column='ID_SettlementArea', primary_key=True) # PA: Added id field
    settlementid_settlements = models.ForeignKey(Settlement, db_column='SettlementID_Settlements')  # Field name made lowercase.
    areaid_area = models.ForeignKey(Area, db_column='AreaID_Area')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Settlement_Area'
        unique_together = (('settlementid_settlements', 'areaid_area'),)


class Site(models.Model):
    id_site = models.AutoField(db_column='ID_Site', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=350, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    topography = models.CharField(max_length=50, blank=True, null=True)
    gps_data_coordinate_system = models.CharField(db_column='GPS_data_coordinate_system', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps_data_n = models.CharField(db_column='GPS_data_N', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps_data_e = models.CharField(db_column='GPS_data_E', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps_data_z = models.CharField(db_column='GPS_data_Z', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coordinate_source = models.CharField(max_length=100, blank=True, null=True)
    reference_site = models.CharField(db_column='reference_SITE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Site'


class Finds(models.Model):
    id_finds = models.AutoField(db_column='ID_Finds', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    interpretationid_interpretation = models.IntegerField(db_column='InterpretationID_Interpretation')  # Field name made lowercase.
    period_id_period = models.ForeignKey(Period, db_column='Period_ID_Period')  # Field name made lowercase.
    research_event_id_research = models.ForeignKey(ResearchEvent, db_column='Research_Event_ID_Research')  # Field name made lowercase.
    area_id_area = models.ForeignKey(Area, db_column='Area_ID_Area')  # Field name made lowercase.
    area_site = models.ForeignKey(Site, db_column='Area_Site_ID')  # Field name made lowercase. PA: Changed Foreing Key form Area to Site

    class Meta:
        managed = False
        db_table = 'finds'
