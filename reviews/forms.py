from django import forms
from .models import Student, Hostel

class ReviewForm(forms.Form):
	student = forms.ModelChoiceField(queryset=Student.objects.all())
	hostel = forms.ModelChoiceField(queryset=Hostel.objects.all())
	rating = forms.IntegerField(min_value=1, max_value=5)
	review = forms.CharField(widget=forms.Textarea)

	def clean_rating(self):
		rating = self.cleaned_data['rating']
		if rating < 1 or rating > 5:
			raise forms.ValidationError('Rating must be between 1 and 5')
		return rating


class ComplaintForm(forms.Form):
	complaint = forms.CharField(widget=forms.Textarea)
	resolved = forms.BooleanField(required=False)
