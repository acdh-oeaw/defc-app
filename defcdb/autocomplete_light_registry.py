# -*- coding: utf-8 -*-
import autocomplete_light
import re, requests, json
from bib.models import Book
from .models import DC_researchevent_institution, ResearchEvent, Name


class ISOAutocomplete(autocomplete_light.AutocompleteListTemplate):
	autocomplete_template = 'defcdb/label_al.html'
	widget_attrs = {
	
	}
	attrs = {
        'data-autocomplete-minimum-characters': 3,
        'placeholder': u'Please start typing language names (in English!) to get suggestions'}
	#choices = [{'ref_name':'Ghotuo', 'isoID':'aaa'},{'ref_name':'Alumu-Tesu', 'isoID':'aab'}]
	
	def choices_for_request(self):
		choices = []
		root = "http://iso639.eos.arz.oeaw.ac.at/api/fuzzysearch/?language="
		parameter = "&format=json"
		q = self.request.GET.get('q')
		url=root+q+parameter
		r = requests.get(url)
		try:
			response = r.json()
			results=response["results"]
			for x in results:
				choices.append({"ref_name":x["ref_name"],"isoID":x["isoID"]})
			return choices
		except:
			choices=[{"ref_name":"""Sorry, something went wrong.
			Please refere to http://www-01.sil.org/iso639-3/codes.asp 
			to find the matching iso639-3 code.
			We apologize for your unceonvenicen."""}]
			return choices

autocomplete_light.register(ISOAutocomplete)


class BookAutocomplete(autocomplete_light.AutocompleteModelBase):
	search_fields=['title', 'author']
	model = Book
	attrs = {
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to get suggestions',
    }

autocomplete_light.register(Book, BookAutocomplete)


class InstitutionAutocomplete(autocomplete_light.AutocompleteModelBase):
	search_fields=['name']
	model = DC_researchevent_institution
	attrs = {
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to get suggestions',
    }

autocomplete_light.register(DC_researchevent_institution, InstitutionAutocomplete)


#class ProjectleaderAutocomplete(autocomplete_light.AutocompleteListBase):
#	allProjectleaders = ResearchEvent.objects.values_list('project_leader')
#	choices = [str(name) for name in allProjectleaders]
#	choices = [re.sub('\(','',name) for name in choices]
#	choices = [re.sub('\)','',name) for name in choices]
#	choices = [re.sub("\'",'',name) for name in choices]
	
class ProjectleaderAutocomplete(autocomplete_light.AutocompleteModelBase):

	search_fields=['project_leader',]
	attrs = {'placeholder': 'Start typing to get suggestions',}
	def choice_label(self, choice):
 		return '{0.project_leader}'.format(choice)

autocomplete_light.register(ResearchEvent,ProjectleaderAutocomplete)


class NameAutocomplete(autocomplete_light.AutocompleteModelBase):

	search_fields=['name',]
	attrs = {'placeholder': 'Start typing to get suggestions',}
	def choice_label(self, choice):
 		return '{0.name}'.format(choice)

autocomplete_light.register(Name,NameAutocomplete)

# class ProjectleaderAutocomplete(autocomplete_light.AutocompleteModelBase):
# 	search_fields=['project_leader']
# 	models = ResearchEvent
# 	attrs = {
#         'placeholder': 'Start typing to get suggestions',
# 	}
# 	def choice_label(self, choice):
# 		return "Hansi"

# autocomplete_light.register(ResearchEvent, ProjectleaderAutocomplete)
