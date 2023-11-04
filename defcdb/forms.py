# -*- coding: utf-8 -*-
from django import forms
from dal import autocomplete

# autocomplete.autodiscover()
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field

from .models import (
    Area,
    ResearchEvent,
    Site,
    Finds,
    Interpretation,
    DC_researchevent_institution,
    Name,
)
from bib.models import Book


class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        # exclude =['reference', 'period_reference']
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AreaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))
        instance = getattr(self, "instance", None)
        if instance and instance.pk:
            self.fields["site"].widget.attrs[
                "readonly"
            ] = True  # lock some fields in editing mode from editing
            self.fields["site"].widget.attrs["disabled"] = True
            self.fields["area_type"].widget.attrs["readonly"] = True
            self.fields["area_type"].widget.attrs["disabled"] = True

    def clean_site(self):
        instance = getattr(self, "instance", None)
        if instance and instance.pk:
            return instance.site
        else:
            return self.cleaned_data["site"]

    def clean_area_type(self):
        instance = getattr(self, "instance", None)
        if instance and instance.pk:
            return instance.area_type
        else:
            return self.cleaned_data["area_type"]


class ResearcheventForm(forms.ModelForm):
    class Meta:
        model = ResearchEvent
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ResearcheventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))


class FindsForm(forms.ModelForm):
    research_event = forms.ModelChoiceField(
        queryset=ResearchEvent.objects.all(),
        help_text="Project/ Research the finds are related to.",
        required=False,
    )

    class Meta:
        model = Finds
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(FindsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))
        instance = getattr(self, "instance", None)
        if instance and instance.pk:
            self.fields["area"].widget.attrs["readonly"] = True
            self.fields["area"].widget.attrs["disabled"] = True
            self.fields["finds_type"].widget.attrs["readonly"] = True
            self.fields["finds_type"].widget.attrs["disabled"] = True

    def clean_area(self):
        instance = getattr(self, "instance", None)
        if instance and instance.pk:
            return instance.area
        else:
            return self.cleaned_data["area"]

    def clean_finds_type(self):
        instance = getattr(self, "instance", None)
        if instance and instance.pk:
            return instance.finds_type
        else:
            return self.cleaned_data["finds_type"]

    # def clean_finds_type(self):  ###second option, also works
    # 	if self.instance:
    # 		return self.instance.area
    # 	else:
    # 		return self.cleaned_data.get('area')

    # http://stackoverflow.com/questions/324477/in-a-django-form-how-to-make-a-field-readonly-or-disabled-so-that-it-cannot-b


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        # exclude=["alternative_name"]
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SiteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))


class InterpretationForm(forms.ModelForm):
    class Meta:
        model = Interpretation
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(InterpretationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))


class form_user_login(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(form_user_login, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Login"))
