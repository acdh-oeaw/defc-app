from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Event(models.Model):
	start_date = models.DateField(blank=True, null=True, max_length=200)
	end_date = models.DateField(blank=True, null=True, max_length=200)
	name = models.CharField(blank=True, null=True, max_length=500)
	place = models.CharField(blank=True, null=True, max_length=200)
	webpage = models.URLField(blank=True, null=True, max_length=200)
	comment = models.TextField(blank=True, null=True, max_length=500)

	class Meta:
		ordering =( '-start_date',)

	def __str__(self):
		return str(self.start_date)+' - '+str(self.end_date)+' '+str(self.name)+' '+str(self.place)+' '+str(self.webpage)

	def get_classname(self):
		"""Returns the name of the class as lowercase string"""
		class_name = str(self.__class__.__name__).lower()
		return class_name

	def get_absolute_url(self):
		return reverse('webpage:about')




