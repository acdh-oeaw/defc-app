# -*- coding: utf-8 -*-
import autocomplete_light
from bib.models import Book

class BookAutocomplete(autocomplete_light.AutocompleteModelBase):
	search_fields=['title', 'author']
	model = Book
	attrs = {
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to get suggestions',
    }

autocomplete_light.register(Book, BookAutocomplete)
