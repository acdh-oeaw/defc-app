# -*- coding: utf-8 -*-
from django.db import models


class Book(models.Model):
    zoterokey = models.CharField(max_length=100, primary_key=True)
    item_type = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    publication_title = models.CharField(max_length=100, blank=True, null=True)
    short_title = models.CharField(max_length=500, blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=100, blank=True, null=True)
    issn = models.CharField(max_length=100, blank=True, null=True)
    doi = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return (
            str(self.author)
            + " "
            + str(self.title)
            + " "
            + str(self.publication_year)
            + " "
            + str(self.place)
        )
