from django import forms
from django.contrib.auth.models import User
from .models import Profile

class StudentForm(forms.Form):
	user = forms.ModelChoiceField(queryset=User.objects.all())
	profile = forms.ModelChoiceField(queryset=Profile.objects.all())


from django import forms
from .models import Student

class SearchHistoryForm(forms.Form):
	student = forms.ModelChoiceField(queryset=Student.objects.all())
	search_query = forms.CharField(max_length=200)
	search_result = forms.CharField(widget=forms.Textarea)
