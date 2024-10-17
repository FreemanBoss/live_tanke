from django import forms
from hostel.models import Hostel

class AgentForm(forms.Form):
	name = forms.CharField(max_length=200, label='Agent Name')
	contact_info = forms.CharField(max_length=200, label='Agent Contact Info')
	hostels = forms.ModelMultipleChoiceField(queryset=Hostel.objects.all())
