from django import forms
from crispy_forms.helper import FormHelper

from defcdb.models import DC_province


class DC_provinceForm(forms.ModelForm):
    class Meta:
        model = DC_province
        fields = ["authorityfile_id", "lat", "lng"]

    def __init__(self, *args, **kwargs):
        super(DC_provinceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
