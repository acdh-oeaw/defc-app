from django.db import models
from defcdb.models import Finds, DC_researchevent_institution


class Contact(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=500)
    last_name = models.CharField(blank=True, null=True, max_length=500)
    institution = models.ManyToManyField(DC_researchevent_institution, blank=True)


class Project(models.Model):
    name = models.CharField(blank=True, null=True, max_length=500)
    title = models.CharField(blank=True, null=True, max_length=500)
    source = models.CharField(blank=True, null=True, max_length=500)
    contact = models.ManyToManyField(Contact, blank=True)
    language = models.CharField(blank=True, null=True, max_length=500)
    keywords = models.CharField(blank=True, null=True, max_length=500)
    publisher = models.CharField(blank=True, null=True, max_length=500)
    issued = models.CharField(blank=True, null=True, max_length=500)
    license = models.CharField(blank=True, null=True, max_length=500)
    access_rights = models.CharField(blank=True, null=True, max_length=500)


class Inclusion(models.Model):
    inclusion_id = models.CharField(blank=True, null=True, max_length=100)
    inclusion_type = models.CharField(blank=True, null=True, max_length=500)
    inclusion_color = models.CharField(blank=True, null=True, max_length=500)
    inclusion_form = models.CharField(blank=True, null=True, max_length=500)
    inclusion_particle_size = models.CharField(blank=True, null=True, max_length=500)
    inclusion_frequency = models.CharField(blank=True, null=True, max_length=500)
    inclusion_hardness = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return str(self.inclusion_id) + '_' + self.inclusion_type + '_' + self.inclusion_color


class Threedmodel(models.Model):
    """ in an 1:1 relation to class Finds"""
    model_id = models.CharField(blank=True, null=True, max_length=100)
    finds = models.ForeignKey(Finds, blank=True, null=True)
    part = models.CharField(blank=True, null=True, max_length=500)
    diameter = models.CharField(blank=True, null=True, max_length=500)
    wall_thickness = models.CharField(blank=True, null=True, max_length=500)
    surface_treatment_i = models.CharField(blank=True, null=True, max_length=500)
    surface_treatment_o = models.CharField(blank=True, null=True, max_length=500)
    surface_color_i = models.CharField(blank=True, null=True, max_length=500)
    surface_color_o = models.CharField(blank=True, null=True, max_length=500)
    decoration_color = models.CharField(blank=True, null=True, max_length=500)
    decoration_description = models.CharField(blank=True, null=True, max_length=500)
    fabric_color = models.CharField(blank=True, null=True, max_length=500)
    hardness = models.CharField(blank=True, null=True, max_length=500)
    sorting = models.CharField(blank=True, null=True, max_length=500)
    density = models.CharField(blank=True, null=True, max_length=500)
    pores = models.CharField(blank=True, null=True, max_length=500)
    core_form = models.CharField(blank=True, null=True, max_length=500)
    core_color = models.CharField(blank=True, null=True, max_length=500)
    inclusion = models.ManyToManyField(Inclusion, blank=True)
    resource_metadata = models.ForeignKey(Project, blank=True, null=True)
    model_file = models.FileField(upload_to='models', blank=True, null=True)
    model_thumbnail = models.FileField(
        upload_to='thumbnails', blank=True, null=True)
    model_metadata = models.FileField(
        upload_to='metadata', blank=True, null=True)
    model_parameters = models.FileField(
        upload_to='parameters', blank=True, null=True)
