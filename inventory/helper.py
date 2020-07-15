from .models import *
from operator import itemgetter, attrgetter
import datetime, secrets

def dontEdit(key):
	if key.name != 'commonobject_ptr' and key.name != 'slug' and key.name != 'token' and key.name != 'lastUpdatedUser' and key.name != 'dateLastModified' and key.name != 'id':
		return False

	return True

def slugIsValid(mySlug):
	if commonObject.objects.filter(slug = mySlug).exists():
		return True
	return False

def formDataToObject(formData, mySlug, newObject):
	constructor = globals()[mySlug.capitalize()]
	subObject = constructor()
	for key, val in formData:
		if key != 'csrfmiddlewaretoken':
			setattr(subObject, key, val)

	subObject.dateLastModified = datetime.datetime.now()
	if newObject == True:
		subObject.slug = mySlug
		subObject.token = secrets.token_urlsafe(20)

	return subObject

def createDynamicForm(subObject):
	f = commonObjectForm()
	for key in subObject._meta.fields:
		if dontEdit(key) == False:
			f.fields[key.name] = forms.CharField(label = key.verbose_name)

	return f             

def getAllSubObjects(mySlug):
	allObjects = commonObject.objects.filter(slug = mySlug)
	allSubObjects = list()
	for object in allObjects:
		allSubObjects.append(getattr(object, mySlug))

	return allSubObjects

def sortObjects(allSubObjects, sortBy):
	sorted(allSubObjects, key = attrgetter(sortBy))

	return


