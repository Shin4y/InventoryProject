from django.db import models
from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import StrictButton

BUILDING_CHOICES = [('WWH', 'WWH'), ('60FifthAve', '60FifthAve'), ('Other', 'Other')]


class commonObject(models.Model):
	#locationType = models.CharField("Location Type", max_length=50, default = "", not used often in the last inventory system, I think I'm just going to leave this out. 
	#	choices = LOCATION_CHOICES)
	building = models.CharField("Building", max_length=50, default ='WWH', choices = BUILDING_CHOICES)
	name = models.CharField("Name", max_length=50, default = "")
	room = models.CharField("Location", max_length=50, default = "")
	dateLastModified = models.DateTimeField("Date Last Modified", max_length=50, default = '2000-1-1')
	lastUpdatedUser = models.CharField("Last Updated User", max_length=50, default = "")
	Notes = models.CharField(max_length=100)
	modelName = models.CharField("Model Name", max_length=50, default = "")
	token = models.CharField(max_length=30, default = 0)
	slug = models.SlugField(default = '')

class commonObjectForm(forms.ModelForm):
	class Meta:
		model = commonObject
		fields = ['name', 'building', 'room', 'Notes', 'modelName']

#class objectManager(models.Model):


class Desktops(commonObject):
	user = models.CharField("User", max_length=50, default = "")
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")
	macAddress = models.CharField("Mac Address", max_length=50, default = "")
	IpAddress = models.CharField("IP Address", max_length=50, default = "")
	OS = models.CharField("OS Type", max_length=50, default = "")
	userType = models.CharField("User Type", max_length=50, default = "")




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
	givenDate = models.DateTimeField("Given Date", max_length=50, default = "2000-1-1")


class Printers(commonObject):
	user = models.CharField(max_length=50, default = "")
	cartridgeType = models.CharField("Cartridge Type", max_length=50, default = "")
	macAddress = models.CharField("Mac Address", max_length=50, default = "")
	givenDate = models.DateTimeField("Given Date", max_length=50, default = '2000-1-1')
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")


class StationaryProjectors(commonObject):
	bulb =  models.CharField("Bulb", max_length=50)

	
class DesktopScanners(commonObject):
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")


	
class DataCenterEquipment(commonObject): #might get rid of later, theres only one entry from 2018
	macAddress = models.CharField("Mac Address", max_length=50, default = "")
	Type = models.CharField("Type", max_length=50, default = "")
	serialNumber = models.CharField("Serial Number", max_length=50, default = "")
	assetTag = models.CharField("Asset Tag", max_length=50, default = "")


##########################################################################################

class BatchForm(forms.Form): #a form used to swap name 1 and name 2 machines. names refer to the name field of said machines
	name1 = forms.CharField(max_length=50)
	name2 = forms.CharField(max_length=50)
	extra_field_count = forms.CharField(widget=forms.HiddenInput())

	def __init__(self, *args, **kwargs):
		extra_fields = kwargs.pop('extra', 0)
		super(BatchForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'swapForm'
		self.helper.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-1'
		self.helper.field_class = 'col-md-3'
		self.helper.form_show_labels = False
		self.helper.render_hidden_fields = True
		self.fields['extra_field_count'].initial = extra_fields

		self.helper.layout = Layout(
		    Field('name1', placeholder = 'Name 1'),
		    Field('name2', placeholder = 'Name 2')
		)

		for index in range(int(extra_fields)):
			# generate extra fields in the number specified via extra_fields
			self.fields['extra_field_{index}'.format(index=index)] = \
				forms.CharField()


	