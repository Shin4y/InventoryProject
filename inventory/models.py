from django.db import models
from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import StrictButton
import pyqrcode

BUILDING_CHOICES = [('WWH', 'WWH'), ('60FifthAve', '60FifthAve'), ('Other', 'Other')]


class commonObject(models.Model):
	#locationType = models.CharField("Location Type", max_length=50, default = "", not used often in the last inventory system, I think I'm just going to leave this out. 
	#	choices = LOCATION_CHOICES)
	building = models.CharField("Building", max_length=50, default ='WWH', choices = BUILDING_CHOICES)
	name = models.CharField("Name", max_length=255, default = "")
	room = models.CharField("Room", max_length=50, default = "")
	lastUpdatedUser = models.CharField("Last Updated User", max_length=50, default = "")
	modelName = models.CharField("Model Name", max_length=255, default = "")
	token = models.CharField(max_length=100, default = 0)
	slug = models.SlugField(default = '', max_length = 256)
	dateLastModified = models.CharField("Date Last Modified", max_length=50, default = '1581370547000')
	Notes = models.CharField(max_length=200)
	qrcode = models.CharField(max_length = 100, default = 'http://google.com')
 
class commonObjectForm(forms.ModelForm):
	field_order = []
	class Meta:
		model = commonObject
		fields = ['building']

#class objectManager(models.Model):

class blankForm(forms.Form):
	field_order = []

class Desktops(commonObject):
	user = models.CharField("User", max_length=50, default = "")
	serialNumber = models.CharField("Serial Number", max_length=255, default = "")
	macAddress = models.CharField("Mac Address", max_length=255, default = "")
	IpAddress = models.CharField("IP Address", max_length=50, default = "")
	OS = models.CharField("OS Type", max_length=50, default = "")
	userType = models.CharField("User Type", max_length=50, default = "")

class Macs(commonObject):
	serialNumber = models.CharField("Serial Number", max_length=255, default = "")
	partNumber = models.CharField("Part Number", max_length=255, default = "")
	modelNumber = models.CharField("Model Number", max_length=255, default = "")
	size = models.CharField("Size", max_length=255, default = "")
	manufactureYear = models.CharField("Manufactured Year", max_length=255, default = "")
	appleCareNumber = models.CharField("AppleCare Registration Number", max_length=255, default = "")
	appleCareExpirationDate = models.CharField("AppleCare Expiration Date", max_length=255, default = "")
	designation = models.CharField("Designation", max_length=255, default = "")
	user = models.CharField("Given To", max_length=255, default = "")
	userType = models.CharField("User Type", max_length=255, default = "")
	purchaseDate = models.CharField("Purchase Date", max_length=255, default = "")
	purpose = models.CharField("Purpose", max_length=255, default = "")
	givenDate = models.CharField("Given Date", max_length = 255, default = "")

class Notebooks(commonObject):
	user = models.CharField("User", max_length=50, default = "")
	make = models.CharField("Make", max_length=50)
	modelNumber = models.CharField("Model Number", max_length=50, default = "")
	OS = models.CharField("OS Type", max_length=50)
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")
	manufacturedYear = models.CharField("Manufactured Year", max_length=50, default = "")
	size = models.CharField("Size", max_length=50, default = "")
	purpose = models.CharField("Purpose", max_length=50, default = "")
	userType = models.CharField("User Type", max_length=50, default = "")
	

class Peripherals(commonObject):
	user = models.CharField(max_length=50, default = "")
	make = models.CharField(max_length=50, default = "")
	givenDate = models.CharField("Given Date", max_length=50, default = "2000-1-1")


class Printers(commonObject):
	user = models.CharField(max_length=50, default = "")
	cartridgeType = models.CharField("Cartridge Type", max_length=50, default = "")
	macAddress = models.CharField("Mac Address", max_length=50, default = "")
	givenDate = models.DateTimeField("Given Date", max_length=50, default = '2000-1-1')
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")


class Stationaryprojectors(commonObject):
	bulb =  models.CharField("Bulb", max_length=50)

	
class Desktopscanners(commonObject):
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")


	
class Datacenterequipment(commonObject): #might get rid of later, theres only one entry from 2018
	macAddress = models.CharField("Mac Address", max_length=50, default = "")
	Type = models.CharField("Type", max_length=50, default = "")
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")
	assetTag = models.CharField("Asset Tag", max_length=50, default = "")

class Printercartridges(commonObject):
	cartridgeType = models.CharField(max_length=50)
	printerCount = models.CharField(max_length=50)
	quantity = models.CharField(max_length=50)

##########################################################################################

## Following models are not related to physical inventory objects ##

class RecentObject(models.Model):
	commonId = models.IntegerField() ## corresponds to commonobject id field
	slug = models.SlugField()

	