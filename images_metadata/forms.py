from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import ImageThesaurus


class ImageThesaurusForm(ModelForm):
    class Meta:
        model = ImageThesaurus
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ImageThesaurusForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))
