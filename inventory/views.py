from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
import datetime, secrets
from .helper import *
from .models import *
from .forms import *
from collections import OrderedDict
from operator import itemgetter, attrgetter
from django.forms import formset_factory


def index(request):
	return render(request, 'inventory/index.html')

def createObject(request, mySlug):
	if slugIsValid(mySlug) != True:
		return HttpResponseNotFound(mySlug.capitalize() + " is not a valid object.")

	constructor = globals()[mySlug.capitalize()]
	subObject = constructor()
	#myList = list()
	if request.method == 'POST':
		f = commonObjectForm(request.POST)
		if f.is_valid():
			formDataToObject(subObject, request.POST.items(), mySlug, True) #inserts the request data into object, and takes care of token, date, and slug as well
			subObject.save()
			return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (mySlug,)))

	# if a GET (or any other method) we'll create a blank form
	else:
		#f = commonObjectForm()
		f = createDynamicForm(subObject)

		objectName = re.sub("([a-z])([A-Z])","\g<1> \g<2>", mySlug)
		objectName = objectName.lower()

		return render(request, 'inventory/createObject.html', {'form': f, 'mySlug': mySlug, 'objectName': objectName})


def editObject(request, secret_id):

	editObject = commonObject.objects.get(token = secret_id)
	editObject = getattr(editObject, editObject.slug)
	objectName = re.sub("([a-z])([A-Z])","\g<1> \g<2>", editObject.slug) #splitting up words and lowercasing
	objectName = objectName.lower()
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		f = commonObjectForm(request.POST)
		# check whether it's valid:

		if f.is_valid():

			formDataToObject(editObject, request.POST.items(), editObject.slug, False)
			
			editObject.dateLastModified = datetime.datetime.now()

			editObject.save()
			return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (editObject.slug,)))

	# if a GET (or any other method) we'll create a blank form
	else:
		#f = commonObjectForm()
		f = createDynamicForm(editObject)

		# for field in f:
		# 	if dontEdit(field.name) == False:
		# 		f.field_order.append(field.name)

		# f.field_order.remove('Notes')
		# f.field_order.append('Notes')
		

		return render(request, 'inventory/editObject.html', {'form': f, 'objectName': objectName, 'token': editObject.token, 'mySlug': editObject.slug, 'qrcode':editObject.qrcode})


def displayAllObjects(request, mySlug, sortBy = 'building'):
	
	if slugIsValid(mySlug) != True:
		return HttpResponseNotFound(mySlug.capitalize() + " is not a valid object.")

	objectName = re.sub("([a-z])([A-Z])","\g<1> \g<2>", mySlug) #uncamelcases the slug for visual purposes
	objectname = objectName.lower()
	listOfFields = getListOfFields(mySlug)
	
	allSubObjects = getAllSubObjects(mySlug)
	sortBy = camelCasing(sortBy)
	if(sortBy != ''):
		allSubObjects.sort(key=lambda x: getattr(x, sortBy), reverse = False)
	bigList, tokenList = ([] for i in range(2))
	getDisplayData(allSubObjects, bigList)
	getTokens(allSubObjects, tokenList)

	masterList = zip(bigList, tokenList)

	return render(request, 'inventory/displayAll.html', {'data':masterList, 'objectName': objectName, 'listOfFields':listOfFields, 'mySlug':mySlug})
			#data is a 2d list of object data}
	#listOfFields is a list of field strings to put at the top of the table

def faviconView(request):	
	faviconView = RedirectView.as_view(url='/static/inventory/images/favicon.ico', permanent=True)

def batchReplace(request, mySlug):

	if slugIsValid(mySlug) != True:
		return HttpResponseNotFound(mySlug.capitalize() + " is not a valid object.")

	if request.method == "POST":
		e = request.POST
		form = BatchForm(request.POST, extra = request.POST.get('extra_field_count'))
		if form.is_valid():
			data = zipSwapData(form.cleaned_data, mySlug)
			for item1, item2 in data: #actually swaps the rooms.
				y = commonObject.objects.get(name = item1)
				z = commonObject.objects.get(name = item2)
				swapRoom(getattr(y, mySlug), getattr(z, mySlug))
				
			return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (mySlug,)))
		return HttpResponse(form.errors)
	else:
		form = BatchForm()
		form.helper.form_action = reverse('inventory:batchReplace', args = (mySlug,))
		return render(request, 'inventory/batchReplace.html', {'form' : form, 'mySlug': mySlug})

	return

def toStorage(request, mySlug, name, room, building): #moves object to storage.
	if slugIsValid(mySlug) != True:
		return HttpResponseNotFound(mySlug.capitalize() + " is not a valid object.")

	if name == "":
		return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (mySlug,)))

	obj = commonObject.objects.get(token = name)
	obj.room = room
	obj.building = building

	try:#incase the model doesn't have a user attribute
		obj.user = ""
	except AttributeError:
		pass
	obj.save()
	return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (mySlug,)))