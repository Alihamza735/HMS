from django import forms

from .models import PatientRegistrationForm

class PatientForm(forms.ModelForm):
	class Meta:
		model = PatientRegistrationForm
		fields ='__all__'


class PatientPureForn(forms.Form):
	title=forms.CharField(max_length=5)
	first_name=forms.CharField(max_length=20)
	last_name=forms.CharField(max_length=20)
	date_of_birth=forms.CharField(max_length=20)
	suffix 		  = forms.CharField(max_length=20)
	mother_First_ame = forms.CharField(max_length=20)
	mother_last_name = forms.CharField(max_length=20)
	ssn = forms.CharField(max_length=20)
	gender = forms.CharField(max_length=10)
	martial_Status = forms.CharField(max_length=15) 
	language = forms.CharField(max_length=20)
	race = forms.CharField(max_length=20)
	sex = forms.CharField(max_length=20)
	address_line_1 = forms.CharField(max_length=80 )
	address_line_2 = forms.CharField(max_length=50 )
	city = forms.CharField(max_length=30)
	state = forms.CharField(max_length=20)
	zip_code=forms.CharField(max_length=20)
	country =forms.CharField(max_length=30)
	specialty = forms.CharField (max_length=20)
	primary_name = forms.CharField(max_length=30)
	second_name = forms.CharField(max_length=30)
	reffering = forms.CharField(max_length=20)
	facility = forms.CharField(max_length=40)
	name = forms.CharField(max_length=50)
	contact = forms.CharField(max_length=15)
	relationship=forms.CharField(max_length=20)
