from django import forms 
from defcdb.models import DC_country, DC_region, DC_province, Site
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div


# class SearchForm(forms.Form):
# 	search_term = forms.CharField(max_length=250, required = False)

class SearchForm(forms.Form):
	choices = (
		('Thessaly', 'Thessaly'),
		('Crete', 'Crete'),
		('Southern and Central Greece, Cyclades', 'Southern and Central Greece, Cyclades'),
		)

	region = forms.ChoiceField(choices = choices)

# class DC_countryForm(ModelForm):
# 	class Meta:
# 		model = DC_country
# 		fields = "__all__"


# class DC_regionForm(ModelForm):
# 	class Meta:
# 		model = DC_region
# 		fields = "__all__"


class DC_provinceForm(forms.ModelForm):
	class Meta:
		model = DC_province
		fields = "__all__"


# class SiteForm(ModelForm):
# 	class Meta:
# 		model = Site
# 		fields = "__all__"

