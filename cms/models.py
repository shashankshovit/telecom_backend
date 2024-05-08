from django.db import models

class Plan(models.Model):
	Plan_Status = models.TextChoices("Active", "Inactive")
	name = models.CharField("Plan name", max_length=50, unique=True)
	cost = models.IntegerField("Plan cost")
	validity = models.IntegerField("Plan validity")
	status = models.CharField("Plan status", choices=Plan_Status)

	def __str__(self):
		return self.name

class Customer(models.Model):
	name = models.CharField("Full name", max_length=100)
	dob = models.DateTimeField("Date of birth")
	email = models.CharField("Customer email", max_length=100, unique=True)
	aadhaar = models.CharField("Customer aadhaar", max_length=12)
	reg_date = models.DateTimeField("Registration date")
	mob = models.CharField("Customer mobile number", max_length=10, unique=True)
	plan = models.ManyToManyField(Plan)

	def __str__(self):
		return self.name+self.mob
