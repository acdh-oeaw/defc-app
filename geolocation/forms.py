from django import forms 
from defcdb.models import DC_country, DC_region, DC_province, Site, DC_chronological_system
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div


def getChoices(allregions):
    """ Turns returns of a queryset into a tuple of tuples like: 
    (
    	("string1", "string1"),
    	("string2", "string2"),
	) """

    choices = []
    for x in allregions:
        firstValue = tuple([(x)])
        secondValue = tuple([(x)])
        firstAndSecond = tuple(firstValue+secondValue)
        choices.append(firstAndSecond)
    choices.append(('','----------'))
    return tuple(choices)


class SearchForm(forms.Form):
    allregions = DC_region.objects.all()
    allregions = ["%s" % x for x in allregions]
    regionChoices = getChoices(allregions)
    region = forms.ChoiceField(choices = regionChoices)
    period_names = DC_chronological_system.objects.all().values_list('period_name')
    period_names = ["%s" % x for x in period_names]
    periodChoices = getChoices(period_names)
    period = forms.ChoiceField(choices = periodChoices)


class DC_provinceForm(forms.ModelForm):
	class Meta:
		model = DC_province
		fields = "__all__"


# class SiteForm(ModelForm):
# 	class Meta:
# 		model = Site
# 		fields = "__all__"

# class DC_countryForm(ModelForm):
# 	class Meta:
# 		model = DC_country
# 		fields = "__all__"


# class DC_regionForm(ModelForm):
# 	class Meta:
# 		model = DC_region
# 		fields = "__all__"