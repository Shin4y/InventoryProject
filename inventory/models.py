from django.db import models

class Desktops(models.Model):
	name = models.CharField(max_length=100)
	user = models.CharField(max_length=50)
	locationType = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	dateLastModified = models.DateTimeField(editable=False)
	serialNumber = models.CharField(max_length=50)
	macAddress = models.CharField(max_length=50)
	IPAddress = models.CharField(max_length=50)
	OS = models.CharField(max_length=50)
	userType = models.CharField(max_length=50)
	Notes = models.CharField(max_length=50)
	lastUpdatedUser = models.CharField(max_length=50)

	# Create your models here.
