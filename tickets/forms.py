from django import forms
from tickets.models import LogIdeas

class LogIdeaForm(forms.ModelForm):
    class Meta:
        model = LogIdeas
        fields = ("name","description")   # NOTE: the trailing comma is required