from django.forms import ModelForm
from defcdb.models import DC_country, DC_region, DC_province, Site

# class DC_countryForm(ModelForm):
# 	class Meta:
# 		model = DC_country
# 		fields = "__all__"


# class DC_regionForm(ModelForm):
# 	class Meta:
# 		model = DC_region
# 		fields = "__all__"


class DC_provinceForm(ModelForm):
	class Meta:
		model = DC_province
		fields = "__all__"


# class SiteForm(ModelForm):
# 	class Meta:
# 		model = Site
# 		fields = "__all__"

