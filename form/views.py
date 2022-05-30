from django.shortcuts import render

from .forms import PatientForm,PatientPureForn

from .models import PatientRegistrationForm

def patient_add(request):
	form=PatientForm() 
	if request.method == "POST":
		form=PatientForm(request.POST)
		if form.is_valid():
			form.save()
			print(form.cleaned_data)
		else:
			print(form.errors)
	context = {
		"form": form 
	}
	return render(request,"form/form_view.html",context)
# Create your views here.
