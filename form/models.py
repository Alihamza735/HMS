from django.db import models

class PatientRegistrationForm(models.Model):
	title 	   	  = models.CharField(max_length=10)
	first_name    = models.CharField(max_length=30)
	last_name     = models.CharField(max_length=30)
	date_of_birthday = models.DateField()
	suffix 		  = models.CharField(max_length=20)
	mother_First_ame = models.CharField(max_length=20)
	mother_last_name = models.CharField(max_length=20)
	ssn = models.CharField(max_length=20)
	gender = models.CharField(max_length=10)
	martial_Status = models.CharField(max_length=15) 
	language = models.CharField(max_length=20)
	race = models.CharField(max_length=20)
	sex = models.CharField(max_length=20)
	address_line_1 = models.CharField(max_length=80 ,default='Enter your address')
	address_line_2 = models.CharField(max_length=50 ,default='Enter your address')
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=20)
	zip_code=models.CharField(max_length=20)
	country =models.CharField(max_length=30)
	specialty = models.CharField (max_length=20)
	primary_name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30)
	reffering = models.CharField(max_length=20)
	facility = models.CharField(max_length=40)
	name = models.CharField(max_length=50)
	contact = models.CharField(max_length=15)
	relationship=models.CharField(max_length=20)


	


# eate your models here.
