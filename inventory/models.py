from django.db import models

from django import forms



class commonObject(models.Model):
	name = models.CharField(max_length=50, default = "")
	locationType = models.CharField("Location Type", max_length=50, default = "")
	location = models.CharField(max_length=50, default = "")
	dateLastModified = models.DateTimeField("Date Last Modified", max_length=50, default = '2000-1-1')
	lastUpdatedUser = models.CharField("Last Updated User", max_length=50, default = "")
	Notes = models.CharField(max_length=100)
	modelName = models.CharField("Model Name", max_length=50, default = "")
	token = models.CharField(max_length=30, default = 0)
	slug = models.SlugField(default = '')

class commonObjectForm(forms.ModelForm):
	class Meta:
		model = commonObject
		fields = ['name', 'locationType', 'location', 'Notes', 'modelName']

#class objectManager(models.Model):


class Desktops(commonObject):
	user = models.CharField(max_length=50, default = "")
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")
	macAddress = models.CharField("Mac Address", max_length=50, default = "")
	IPAddress = models.CharField("IP Address", max_length=50, default = "")
	OS = models.CharField("OS Type", max_length=50, default = "")
	userType = models.CharField("User Type", max_length=50, default = "")




class DesktopForm(forms.ModelForm):
	class Meta:
		model = Desktops
		fields = ['user', 'name', 'locationType', 'location', 'Notes', 'modelName',
		'serialNumber', 'macAddress', 'IPAddress', 'OS', 'userType']


class Notebooks(commonObject):
	user = models.CharField(max_length=50, default = "")
	make = models.CharField(max_length=50)
	modelNumber = models.CharField("Model Number", max_length=50, default = "")
	OS = models.CharField("OS Type", max_length=50)
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")
	manufacturedYear = models.CharField("Manufactured Year", max_length=50, default = "")
	size = models.CharField(max_length=50, default = "")
	purpose = models.CharField(max_length=50, default = "")
	userType = models.CharField("User Type", max_length=50, default = "")
	

class NoteBookForm(forms.ModelForm):
	class Meta:
		model = Notebooks
		fields = ['user', 'name', 'locationType', 'location', 'Notes', 'modelName',
		'make', 'modelNumber', 'OS', 'serialNumber', 'manufacturedYear', 'size', 'purpose', 'userType']


class Peripherals(commonObject):
	user = models.CharField(max_length=50, default = "")
	make = models.CharField(max_length=50, default = "")
	givenDate = models.DateTimeField("Given Date", max_length=50, default = "2000-1-1")


class PeripheralForm(forms.ModelForm):
	class Meta:
		model = Peripherals
		fields = ['user', 'name', 'locationType', 'location', 'Notes', 'modelName',
		'make', 'givenDate']


class Printers(commonObject):
	user = models.CharField(max_length=50, default = "")
	cartridgeType = models.CharField("Cartridge Type", max_length=50, default = "")
	macAddress = models.CharField("Mac Address", max_length=50, default = "")
	givenDate = models.DateTimeField("Given Date", max_length=50, default = '2000-1-1')
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")

	
class PrinterForm(forms.ModelForm):
	class Meta:
		model = Printers
		fields = ['user', 'name', 'locationType', 'location', 'Notes', 'modelName',
		'cartridgeType', 'macAddress' , 'givenDate', 'serialNumber']


class StationaryProjectors(commonObject):
	bulb =  models.CharField(max_length=50)
	

class StationaryProjectorForm(forms.ModelForm):
	class Meta:
		model = StationaryProjectors
		fields = ['name', 'locationType', 'location', 'Notes', 'modelName',
		'bulb']


class DesktopScanners(commonObject):
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")

	
	

class DesktopScannersForm(forms.ModelForm):
	class Meta:
		model = DesktopScanners
		fields = ['name', 'locationType', 'location', 'Notes', 'modelName',
		'serialNumber']

	
class DataCenterEquipment(commonObject): #might get rid of later, theres only one entry from 2018
	macAddress = models.CharField("Mac Address", max_length=50, default = "")
	Type = models.CharField(max_length=50, default = "")
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")
	assetTag = models.CharField("Asset Tag", max_length=50, default = "")

	

class DataCenterEquipmentForm(forms.ModelForm):
	class Meta:
		model = DataCenterEquipment
		fields = ['name', 'locationType', 'location', 'Notes', 'modelName',
		'macAddress', 'Type', 'serialNumber', 'assetTag']