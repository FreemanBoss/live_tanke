from django import forms
from students.models import Student
from hostel.models import Hostel
from hostel.models import Room

class BookingForm(forms.Form):
	student = forms.ModelChoiceField(queryset=Student.objects.all())
	hostel = forms.ModelChoiceField(queryset=Hostel.objects.all())
	room = forms.ModelChoiceField(queryset=Room.objects.all())
	status = forms.CharField(max_length=20)

	def clean_status(self):
		status = self.cleaned_data['status']
		if status not in ['booked', 'pending', 'cancelled']:
			raise forms.ValidationError('Invalid status')
		return status

class PaymentForm(forms.Form):
	amount = forms.DecimalField(max_digits=10, decimal_places=2)
	payment_method = forms.CharField(max_length=20)
	transaction_id = forms.CharField(max_length=50)
	date_paid = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

	def clean_amount(self):
		amount = self.cleaned_data['amount']
		if amount < 0:
			raise forms.ValidationError('Amount cannot be negative')
		return amount
