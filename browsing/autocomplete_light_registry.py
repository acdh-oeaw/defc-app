import autocomplete_light
from defcdb.models import Site


class SiteAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name']
    model = Site
    attrs = {
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to get suggestions',
    }

autocomplete_light.register(Site, SiteAutocomplete)
