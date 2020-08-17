from .models import *
from operator import itemgetter, attrgetter
import datetime, secrets, re, pyqrcode, copy


#LOCATION_CHOICES = [('Office', 'Office'), ('Lab', 'Lab'), ('Classroom', 'Classroom'), ('Other, Other')]

def dontEdit(key):
	if key != 'commonobject_ptr_id' and key != 'commonobject_ptr' and key != 'slug' and key != 'token' and key != 'lastUpdatedUser' and key != 'dateLastModified' and key != 'id' and key != 'qrcode':
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
		editObject.qrcode = 'http://http://127.0.0.1:8000/inventory/' + mySlug +'/id=' + editObject.token #NEEDS TO BE CHANGED WHEN OUT OF PRODUCTION

	return

def createDynamicForm(subObject): #Creates general forms by reading all the fields of a model and creating corresponding fields
	f = commonObjectForm()
	for key in subObject._meta.fields:
		if dontEdit(key.name) == False:
			if key.name != 'building' and key.name != 'qrcode': 
				f.fields[key.name] = forms.CharField(initial = getattr(subObject, key.name.replace(" ", "")), label = key.verbose_name)
				# I dont know why the line above needs to strip white space, but it suddenly started happening so its staying there
	f.fields['building'].initial = getattr(subObject, 'building')			
	return f


def getAllSubObjects(mySlug): #Getting all instances of a certain slug and putting into a list
	allObjects = commonObject.objects.filter(slug = mySlug)
	allSubObjects = list()
	for object in allObjects:
		allSubObjects.append(getattr(object, mySlug))

	return allSubObjects

#def sortObjects(allSubObjects, sortBy):
#	sorted(allSubObjects, key = attrgetter(sortBy))
#
#	return

def getListOfFields(mySlug): #getting field names for the table in displayAll.html
	constructor = globals()[mySlug.capitalize()]
	subObject = constructor()
	listOfFields = list()
	for key in subObject._meta.fields:
		if dontEdit(key.name) != True and key.name != "dateLastModified":
			key.name = re.sub("([a-z])([A-Z])","\g<1> \g<2>", key.name)
			listOfFields.append(key.name.title())

	return listOfFields

def getDisplayData(allSubObjects, bigList): #gets data from objects to be displayed in displayAll view/template
	for obj in allSubObjects:
			smallList = list()
			first = True
			for attr, value in obj.__dict__.items():
				if not first and dontEdit(attr) != True:
					smallList.append(value)
				else:
					first = False
			time = datetime.datetime.fromtimestamp(int(obj.dateLastModified)/1000)
			smallList.append(time.strftime("%m/%d/%y"))
			bigList.append(smallList)

	return 

def getTokens(allSubObjects, tokenList): #gets tokens to be used for edit button links for displayAll view/template
	for obj in allSubObjects:
		for attr, value in obj.__dict__.items():
			if attr == 'token':
				tokenList.append(value)

	return 

def swapRoom(y, z): #swaproom function for batchReplace
	roomHolder = y.room
	buildingHolder = y.building
	y.room = z.room
	y.building = z.building
	z.room = roomHolder
	z.building = buildingHolder
	y.save()
	z.save()

	return

def zipSwapData(data, mySlug): #zips the name and user fields together for later convenience. also assigns new users 
	zippedData = zipFields(data)
	zippedDataCopy = copy.deepcopy(zippedData)
	giveNewOwner(zippedDataCopy, mySlug)
	list1 = list()
	list2 = list()
	flag = True
	for name, owner in zippedData:
		if flag == True:
			list1.append(name)
			flag = False
		else:
			list2.append(name)
			flag = True
	return zip(list1, list2)

def giveNewOwner(zippedData, mySlug): #gives the objects named in batch replace new owners based on the zipped data
	counter = 0 #resets every two loops
	name = ''
	owner = ''
	for name, owner in zippedData:
		obj = commonObject.objects.get(name = name)
		getattr(obj, mySlug).user = owner
		getattr(obj, mySlug).save()

def zipFields(data):#zipping the room field and the owner field together
	flag = False #alternates to put owner and room number in different lists to zip together
	list1 = list()
	list2 = list()
	for key in data:
		if key == 'extra_field_count':
			continue
		if 'extra_field_' in key or 'name' in key:
			list1.append(data[key])
		elif 'extra_owner_' in key or 'owner' in key:
			list2.append(data[key])

	return zip(list1, list2)

def camelCasing(words):
	listOfWords = words.split()
	result = ""
	flag = True
	for word in listOfWords:
		if flag == True:
			result = result + word.lower()
			flag = False
		else:
			result = result + word.capitalize()
	return result