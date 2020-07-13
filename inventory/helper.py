from .models import *
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
			f.fields[key.name] = forms.CharField()

	return f             