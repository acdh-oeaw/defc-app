# -*- coding: utf-8 -*-
import autocomplete_light
import re
from bib.models import Book
from .models import DC_researchevent_institution, ResearchEvent


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


class ProjectleaderAutocomplete(autocomplete_light.AutocompleteListBase):
	allProjectleaders = ResearchEvent.objects.values_list('project_leader')
	choices = [str(name) for name in allProjectleaders]
	choices = [re.sub('\(','',name) for name in choices]
	choices = [re.sub('\)','',name) for name in choices]
	choices = [re.sub("\'",'',name) for name in choices]
	
autocomplete_light.register(ProjectleaderAutocomplete)


# class ProjectleaderAutocomplete(autocomplete_light.AutocompleteModelBase):
# 	search_fields=['project_leader']
# 	models = ResearchEvent
# 	attrs = {
# 		'data-autocomplete-minimum-characters': 2,
#         'placeholder': 'Start typing to get suggestions',
# 	}
# 	def choice_label(self, choice):
# 		return "Hansi"

# autocomplete_light.register(ResearchEvent, ProjectleaderAutocomplete)
