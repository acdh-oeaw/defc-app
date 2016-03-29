from django.db import models

# Create your models here.
from bib.models import Book
from defcdb.models import (DC_finds_pottery_decoration, DC_finds_pottery_detail,
    DC_finds_pottery_form, DC_finds_small_finds_type, DC_region)


class ImageThesaurus(models.Model):
    name = models.CharField(blank=True, null=True, max_length=500)
    pottery_decoration = models.ForeignKey(DC_finds_pottery_decoration, blank=True, null=True)
    pottery_detail = models.ForeignKey(DC_finds_pottery_detail, blank=True, null=True)
    pottery_form = models.ForeignKey(DC_finds_pottery_form, blank=True, null=True)
    small_finds = models.ForeignKey(DC_finds_small_finds_type, blank=True, null=True)
    region = models.ManyToManyField(DC_region, blank=True)
    creator = models.CharField(blank=True, null=True, max_length=500)
    image = models.FileField(upload_to='static/images', blank=True, null=True)
    thumbnail = models.FileField(upload_to='static/thumbnails', blank=True, null=True)
    literature = models.ForeignKey(Book, blank=True, null=True)
    page = models.CharField(blank=True, null=True, max_length=100)
    filename = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return str(self.name)+'_'+str(self.id)


################# in template use something like this ###################################
		# {% if object.pottery_decoration != None %}
  #           {{ object.pottery_decoration }}
  #         {% elseif object.pottery_detail != None %}
  #           {{ object.pottery_detail }}
  #         {% elseif object.pottery_form != None %}
  #           {{ object.pottery_form }}
  #        {% else %}
  #           {{ object.small_finds }}

  #         {% endif %}

############################### OR second option #######################################
#  class Pottery_decoration_images(models.Model):
#   	pottery_decoration_name = ForeignKey(DC_finds_pottery_decoration, blank=True, null=True)
#   	creator = CharField(blank=True, null=True, max_length=500)
# 	image = models.FileField(upload_to='static/images',
# 		blank=True, null=True)
# 	thumbnail = model.FileField(upload_to='static/thumbnails',
# 		blank=True, null=True)
# 	literature = ForeignKey(Book, blank=True, null=True)
# 	page = CharField(blank=True, null=True, max_length=100)

# def __str__(self):
# 	return str(self.pottery_decoration_name)+'_'+str(self.id)


#  class Pottery_detail_images(models.Model):
#   	pottery_detail_name = ForeignKey(DC_finds_pottery_detail, blank=True, null=True)
#   	creator = CharField(blank=True, null=True, max_length=500)
# 	image = models.FileField(upload_to='static/images',
# 		blank=True, null=True)
# 	thumbnail = model.FileField(upload_to='static/thumbnails',
# 		blank=True, null=True)
# 	literature = ForeignKey(Book, blank=True, null=True)
# 	page = CharField(blank=True, null=True, max_length=100)

# def __str__(self):
# 	return str(self.pottery_detail_name)+'_'+str(self.id)


#  class Pottery_form_images(models.Model):
#   	pottery_form_name = ForeignKey(DC_finds_pottery_form, blank=True, null=True)
#   	creator = CharField(blank=True, null=True, max_length=500)
# 	image = models.FileField(upload_to='static/images',
# 		blank=True, null=True)
# 	thumbnail = model.FileField(upload_to='static/thumbnails',
# 		blank=True, null=True)
# 	literature = ForeignKey(Book, blank=True, null=True)
# 	page = CharField(blank=True, null=True, max_length=100)

# def __str__(self):
# 	return str(self.pottery_form_name)+'_'+str(self.id)


# class Small_finds_images(models.Model):
#   	small_finds_name = ForeignKey(DC_finds_small_finds_type, blank=True, null=True)
#   	creator = CharField(blank=True, null=True, max_length=500)
# 	image = models.FileField(upload_to='static/images',
# 		blank=True, null=True)
# 	thumbnail = model.FileField(upload_to='static/thumbnails',
# 		blank=True, null=True)
# 	literature = ForeignKey(Book, blank=True, null=True)
# 	page = CharField(blank=True, null=True, max_length=100)

# def __str__(self):
# 	return str(self.small_finds_name)+'_'+str(self.id)

#########################################################################