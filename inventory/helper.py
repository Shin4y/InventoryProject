from .models import *
from operator import itemgetter, attrgetter
import datetime, secrets

#LOCATION_CHOICES = [('Office', 'Office'), ('Lab', 'Lab'), ('Classroom', 'Classroom'), ('Other, Other')]

def dontEdit(key):
	if key.name != 'commonobject_ptr' and key.name != 'slug' and key.name != 'token' and key.name != 'lastUpdatedUser' and key.name != 'dateLastModified' and key.name != 'id':
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
	for key in subObject._meta.fields:
		if dontEdit(key) == False:
			if key.name != 'locationType':
				f.fields[key.name] = forms.CharField(label = key.verbose_name)


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

