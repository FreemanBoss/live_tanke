from django import forms
from .models import Hostel, Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number', 'address']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'amount', 'payment_date', 'payment_method']

class HostelForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    capacity = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)

class RoomForm(forms.Form):
    hostel = forms.ModelChoiceField(queryset=Hostel.objects.all())
    room_number = forms.IntegerField()
    room_type = forms.CharField(max_length=20)
    capacity = forms.IntegerField()
    price = forms.DecimalField()

class ComplaintForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    complaint = forms.CharField(widget=forms.Textarea)
