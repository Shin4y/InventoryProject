from .models import *
from operator import itemgetter, attrgetter
import datetime, secrets
import re

#LOCATION_CHOICES = [('Office', 'Office'), ('Lab', 'Lab'), ('Classroom', 'Classroom'), ('Other, Other')]

def dontEdit(key):
	if key != 'commonobject_ptr_id' and key != 'commonobject_ptr' and key != 'slug' and key != 'token' and key != 'lastUpdatedUser' and key != 'dateLastModified' and key != 'id':
		return False

	return True

def slugIsValid(mySlug): #Won't work if there isn't an instance of that kind of model already in the database, even if a table 
	if commonObject.objects.filter(slug = mySlug).exists(): #for that model already exists.
		return True
	return False

def formDataToObject(editObject, formData, mySlug, newObject):#Because forms are generalized, there is no built in method (to my knowledge)
	#constructor = globals()[mySlug.capitalize()]#that will auto create model object from form. This is the method I built to do that.
	#subObject = constructor()

	for key, val in formData:
		if key != 'csrfmiddlewaretoken':
			setattr(editObject, key, val)

	editObject.dateLastModified = datetime.datetime.now()
	if newObject == True:
		editObject.slug = mySlug
		editObject.token = secrets.token_urlsafe(20)

	return

def createDynamicForm(subObject): #Creates general forms by reading all the fields of a model and creating corresponding fields
	f = commonObjectForm()
	z = 0
	for key in subObject._meta.fields:
		if dontEdit(key.name) == False:
			if key.name != 'building': 
				f.fields[key.name] = forms.CharField(initial = getattr(subObject, key.name), label = key.verbose_name)

	f.fields['building'].initial = getattr(subObject, 'building')			
	return f

def getAllSubObjects(mySlug): #Getting all instances of a certain slug and putting into a list
	allObjects = commonObject.objects.filter(slug = mySlug)
	allSubObjects = list()
	for object in allObjects:
		allSubObjects.append(getattr(object, mySlug))

	return allSubObjects

def sortObjects(allSubObjects, sortBy):
	sorted(allSubObjects, key = attrgetter(sortBy))

	return

def getListOfFields(mySlug): #getting field names for the table in displayAll.html
	constructor = globals()[mySlug.capitalize()]
	subObject = constructor()
	listOfFields = list()
	for key in subObject._meta.fields:
		if dontEdit(key.name) != True:
			key.name = re.sub("([a-z])([A-Z])","\g<1> \g<2>", key.name)
			listOfFields.append(key.name.title())

	return listOfFields

def getDisplayData(allSubObjects, bigList):
	for obj in allSubObjects:
			smallList = list()
			first = True
			for attr, value in obj.__dict__.items():
				if not first and dontEdit(attr) != True:
					smallList.append(value)
				else:
					first = False
			bigList.append(smallList)

	return 

def getTokens(allSubObjects, tokenList):
	for obj in allSubObjects:
		for attr, value in obj.__dict__.items():
			if attr == 'token':
				tokenList.append(value)

	return 

def swapRoom(y, z):
	roomHolder = y.room
	buildingHolder = y.building
	y.room = z.room
	y.building = z.building
	z.room = roomHolder
	z.building = buildingHolder
	y.save()
	z.save()

def zipSwapData(data):
	list1 = list()
	list2 = list()
	flag = True
	for key in data:
		if key == 'extra_field_count':
			continue
		if flag == True:
			list1.append(data[key])
			flag = False
		else:
			list2.append(data[key])
			flag = True

	return zip(list1, list2)
