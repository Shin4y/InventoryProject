from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
import datetime, secrets
from .helper import *
from .models import *
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
	myList = list()
	if request.method == 'POST':
		f = commonObjectForm(request.POST)
		if f.is_valid():
			formDataToObject(subObject, request.POST.items(), mySlug, True) #inserts the request data into object, and takes care of token, date, and slug as well
			subObject.save()
			return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (mySlug,)))

	# if a GET (or any other method) we'll create a blank form
	else:
		f = commonObjectForm()
		f = createDynamicForm(subObject)

		objectName = re.sub("([a-z])([A-Z])","\g<1> \g<2>", mySlug)
		objectName = objectName.lower()

		return render(request, 'inventory/createObject.html', {'form': f, 'mySlug': mySlug, 'objectName': objectName})


def editObject(request, secret_id, mySlug):

	if slugIsValid(mySlug) != True:
		return HttpResponseNotFound(mySlug.capitalize() + " is not a valid object.")

	editObject = commonObject.objects.get(token = secret_id)
	editObject = getattr(editObject, mySlug)
	objectName = re.sub("([a-z])([A-Z])","\g<1> \g<2>", mySlug) #splitting up words and lowercasing
	objectName = objectName.lower()
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		f = commonObjectForm(request.POST)
		# check whether it's valid:

		if f.is_valid():

			formDataToObject(editObject, request.POST.items(), mySlug, False)
			
			editObject.dateLastModified = datetime.datetime.now()

			editObject.save()
			return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (mySlug,)))

	# if a GET (or any other method) we'll create a blank form
	else:
		f = commonObjectForm()
		f = createDynamicForm(editObject)

		for field in f:
			if dontEdit(field.name):
				field.value = getattr(editObject, field.name)


		return render(request, 'inventory/editObject.html', {'form': f, 'objectName': objectName, 'token': editObject.token, 'mySlug': mySlug })


def displayAllObjects(request, mySlug, sortBy = ''):
	
	if slugIsValid(mySlug) != True:
		return HttpResponseNotFound(mySlug.capitalize() + " is not a valid object.")

	objectName = re.sub("([a-z])([A-Z])","\g<1> \g<2>", mySlug) #uncamelcases the slug for visual purposes
	objectname = objectName.lower()
	listOfFields = getListOfFields(mySlug)
	
	allSubObjects = getAllSubObjects(mySlug)
	#red = allSubObjects
	e = sortBy
	if(sortBy != ''):
		allSubObjects.sort(key=lambda x: getattr(x, sortBy), reverse = True)
	bigList, tokenList = ([] for i in range(2))
	getDisplayData(allSubObjects, bigList)
	getTokens(allSubObjects, tokenList)

	masterList = zip(bigList, tokenList)

	return render(request, 'inventory/displayAll.html', {'data':masterList, 'objectName': objectName, 'listOfFields':listOfFields})
			#data is a 2d list of object data}
	#listOfFields is a list of field strings to put at the top of the table

def faviconView(request):	
	faviconView = RedirectView.as_view(url='/static/inventory/images/favicon.ico', permanent=True)

def batchReplace(request, mySlug):

	if slugIsValid(mySlug) != True:
		return HttpResponseNotFound(mySlug.capitalize() + " is not a  valid object.")

	if request.method == "POST":
		form = BatchForm(request.POST, extra = request.POST.get('extra_field_count'))
		if form.is_valid():
			data = zipSwapData(form.cleaned_data)
			for item1, item2 in data:
				y = commonObject.objects.get(name = item1)
				z = commonObject.objects.get(name = item2)
				swapRoom(getattr(y, mySlug), getattr(z, mySlug))
				
			return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (mySlug,)))

		#something
	else:
		form = BatchForm()
		form.helper.form_action = reverse('inventory:batchReplace', args = (mySlug,))
		return render(request, 'inventory/batchReplace.html', {'form' : form, 'mySlug': mySlug})

	return

def toStorage(request, mySlug, name):
	return