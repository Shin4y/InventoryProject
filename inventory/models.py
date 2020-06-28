from django.db import models

#class inventoryTemplate(models.Model): I'll think about changing this later to make the code cleaner
#	name = models.CharField(max_length=100) but for now I don't want an inventorytemplate table
#	user = models.CharField(max_length=50) in the database 
#	locationType = models.CharField(max_length=50)
#	location = models.CharField(max_length=50)
#	dateLastModified = models.DateTimeField(editable=False)
#	macAddress = models.CharField(max_length=50)
#	IPAddress = models.CharField(max_length=50)
#	userType = models.CharField(max_length=50)
#	Notes = models.CharField(max_length=50)
#	lastUpdatedUser = models.CharField(max_length=50)


class Desktops(models.Model):
	name = models.CharField(max_length=100)
	user = models.CharField(max_length=50)
	modelName = models.CharField(max_length=50)
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

class Notebooks(models.Model):
	locationType = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	make = models.CharField(max_length=50)
	modelNumber = models.CharField(max_length=50)
	OS = models.CharField(max_length=50)
	serialNumber = models.CharField(max_length=50)
	manufacturedYear = models.CharField(max_length=50)
	size = models.CharField(max_length=50)
	designation = models.CharField(max_length=50)
	givenTo = models.CharField(max_length=50)
	purpose = models.CharField(max_length=50)
	userType = models.CharField(max_length=50)
	dateLastModified = models.DateTimeField(editable=False)
	lastUpdatedUser = models.CharField(max_length=50)

class Peripherals(models.Model):
	locationType = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	make = models.CharField(max_length=50)
	designation = models.CharField(max_length=50)
	givenTo = models.CharField(max_length=50)
	givenDate = models.CharField(max_length=50)
	dateLastModified = models.DateTimeField(editable=False)
	lastUpdatedUser = models.CharField(max_length=50)

class Printers(models.Model):
	name = models.CharField(max_length=100)
	modelName = models.CharField(max_length=50)
	locationType = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	cartridgeType = models.CharField(max_length=50)
	macAddress = models.CharField(max_length=50)
	user = models.CharField(max_length=50)
	givenDate = models.CharField(max_length=50)
	dateLastModified = models.DateTimeField(editable=False)
	lastUpdatedUser = models.CharField(max_length=50)
	serialNumber = models.CharField(max_length=50)
	notes = models.CharField(max_length=500)


class stationaryProjectors(models.Model):
	locationType = models.CharField(max_length=50)
	location =  models.CharField(max_length=50)
	modelName =  models.CharField(max_length=50)
	bulb =  models.CharField(max_length=50)
	lastUpdatedUser = models.CharField(max_length=50)
	dateLastModified = models.CharField(max_length=50)

class desktopScanners(models.Model):
	locationType =  models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	user = models.CharField(max_length=50)
	modelName = models.CharField(max_length=50)
	serialNumber = models.CharField(max_length=50)
	comments = models.CharField(max_length=400)
	lastUpdatedUser = models.CharField(max_length=50)
	dateLastModified = models.CharField(max_length=50) 

class dataCenterEquipment(models.Model): #might get rid of later, theres only one entry from 2018
	locationType = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	macAddress = models.CharField(max_length=50)
	Type = models.CharField(max_length=50)
	serialNumber = models.CharField(max_length=50)
	assetTag = models.CharField(max_length=50)
	comments = models.CharField(max_length=400)
	lastUpdatedUser = models.CharField(max_length=50)
	dateLastModified = models.CharField(max_length=50)