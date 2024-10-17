from django import forms
from users.models import Student, Agent

class ConversationForm(forms.Form):
	student = forms.ModelChoiceField(queryset=Student.objects.all())
	agent = forms.ModelChoiceField(queryset=Agent.objects.all())
	subject = forms.CharField(max_length=200)
	timestamp = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
	is_ready = forms.BooleanField(required=False)
	is_archived = forms.BooleanField(required=False)
