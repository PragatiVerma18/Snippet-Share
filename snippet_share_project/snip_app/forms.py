from django import forms
from .models import Snip
from crispy_forms.helper import FormHelper
class snipForm(forms.ModelForm):
    helper = FormHelper()

    class Meta:
        model=Snip
        fields=('text','title','link_code','lang')
        labels={'title':'Snippet Title','text':'New Snippet','link_code':'Secret Code','lang': 'Syntax Highlighting'}
    