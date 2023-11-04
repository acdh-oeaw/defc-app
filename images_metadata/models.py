from django.db import models

# Create your models here.
from bib.models import Book
from defcdb.models import (
    DC_finds_pottery_decoration,
    DC_finds_pottery_detail,
    DC_finds_pottery_form,
    DC_finds_small_finds_type,
    DC_region,
)


class ImageThesaurus(models.Model):
    name = models.CharField(blank=True, null=True, max_length=500)
    pottery_decoration = models.ForeignKey(
        DC_finds_pottery_decoration, blank=True, null=True
    )
    pottery_detail = models.ForeignKey(DC_finds_pottery_detail, blank=True, null=True)
    pottery_form = models.ForeignKey(DC_finds_pottery_form, blank=True, null=True)
    small_finds = models.ForeignKey(DC_finds_small_finds_type, blank=True, null=True)
    region = models.ManyToManyField(DC_region, blank=True)
    creator = models.CharField(blank=True, null=True, max_length=500)
    image = models.FileField(upload_to="images", blank=True, null=True)
    literature = models.ForeignKey(Book, blank=True, null=True)
    page = models.CharField(blank=True, null=True, max_length=100)
    filename = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return str(self.name) + "_" + str(self.id)
