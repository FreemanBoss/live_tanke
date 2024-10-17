from django import forms
from users.models import Student

class PaymentForm(forms.Form):
	student = forms.ModelChoiceField(queryset=Student.objects.all())
	amount = forms.DecimalField(max_digits=10, decimal_places=2)
	payment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
	payment_method = forms.CharField(max_length=200)
