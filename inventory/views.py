from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime, secrets, re
from .helper import *
from .models import *
from collections import OrderedDict
from operator import itemgetter, attrgetter


def index(request):
	return HttpResponse("Hello, world.")

def createObject(request, mySlug):
	if slugIsValid(mySlug) != True:
		return HttpResponseNotFound(mySlug.capitalize() + " is not a valid object.")

	constructor = globals()[mySlug.capitalize()]
	subObject = constructor()
	myList = list()
	if request.method == 'POST':
		f = commonObjectForm(request.POST)
		if f.is_valid():
			subObject = formDataToObject(request.POST.items(), mySlug, True) #inserts the request data into object, and takes care of token, date, and slug as well
			subObject.save()
			return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (mySlug,)))

	# if a GET (or any other method) we'll create a blank form
	else:
		f = commonObjectForm()
		f = createDynamicForm(subObject)

		return render(request, 'inventory/createObject.html', {'form': f, 'mySlug': mySlug.capitalize})


def editDesktop(request, secret_id, mySlug):

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

			editObject = formDataToObject(request.POST.items(), mySlug, False)
			
			editObject.dateLastModified = datetime.datetime.now()

			editObject.save()
			return HttpResponseRedirect('inventory:displayAllObjects', args = (mySlug,))

	# if a GET (or any other method) we'll create a blank form
	else:
		f = commonObjectForm()
		f = createDynamicForm(editObject)

		for field in f:
			if dontEdit(field):
				f.value = getattr(editObject, field.name)


		return render(request, 'inventory/editDesktop.html', {'form': f, 'objectName': objectName, 'token': editObject.token, 'mySlug': mySlug })


def displayAllObjects(request, mySlug, sortBy = ''):
	
	if slugIsValid(mySlug) != True:
		return HttpResponseNotFound(mySlug.capitalize() + " is not a valid object.")

	objectName = re.sub("([a-z])([A-Z])","\g<1> \g<2>", mySlug) #uncamelcases the slug for visual purposes
	objectname = objectName.lower()
	if slugIsValid(mySlug):
		allSubObjects = getAllSubObjects(mySlug)

		if(sortBy != ''):
			sorted(allSubObjects, key=attrgetter(sortBy))

		return render(request, 'inventory/displayAll.html', {'allObjects':allSubObjects, 'objectName': objectName})

