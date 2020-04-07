from django import forms
from .models import Snip
from crispy_forms.helper import FormHelper
class snipForm(forms.ModelForm):
    helper = FormHelper()

    class Meta:
        model=Snip
        fields=('text','title','link_code','lang')
        labels={'title':'Snippet Title','text':'New Snippet','link_code':'Secret Code','lang': 'Syntax Highlighting'}

class searchForm(forms.Form):
    helper = FormHelper()
    search = forms.CharField(max_length=100, widget= forms.TextInput
                           (attrs={'class':'is-small input is-info', 'placeholder':'Search Text Here'}))
    