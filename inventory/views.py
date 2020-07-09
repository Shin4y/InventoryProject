from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime, secrets
from .helper import *
from .models import *
from collections import OrderedDict


def index(request):
	return HttpResponse("Hello, world.")

def createDesktop(request, mySlug):
	if slugIsValid(mySlug):

		constructor = globals()[mySlug.capitalize()]
		subObject = constructor()
		myList = list()
		if request.method == 'POST':
			f = commonObjectForm(request.POST)
			if f.is_valid():
				subObject = formDataToObject(request.Post.items(), mySlug) #inserts the request data into object, and takes care of token, date, and slug as well
				subObject.save()
				return HttpResponseRedirect(reverse('inventory:displayAllObjects', args = (mySlug,)))

		# if a GET (or any other method) we'll create a blank form
		else:
			f = commonObjectForm()
			f = createDynamicForm()

			return render(request, 'inventory/createDesktop.html', {'form': f, 'mySlug': mySlug.capitalize})


def editDesktop(request, secret_id):

	editDesktop = Desktops.objects.get(id = secret_id)
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = DesktopForm(request.POST)
		# check whether it's valid:

		if form.is_valid():
			data = request.POST.copy()
			editDesktop.dateLastModified = datetime.datetime.now()
			editDesktop.name = data.get('name')
			for field in form:
				setattr(editDesktop, field.name, data.get(field.name))

			editDesktop.save()
			return HttpResponseRedirect("the name is %s" % data.get('name'))

	# if a GET (or any other method) we'll create a blank form
	else:
		form = DesktopForm(instance = editDesktop)
		#form = DesktopForm(initial = {'name' : editDesktop.name, 'location': editDesktop.location, 'locationType':editDesktop.locationType, 
		#	'serialNumber':editDesktop.serialNumber, 'macAddress':editDesktop.macAddress, 'IPAddress':editDesktop.IPAddress,
		#	'OS':editDesktop.OS, 'userType':editDesktop.userType})

		return render(request, 'inventory/editDesktop.html', {'form': form, 'desktop': editDesktop})


def displayAllObjects(request, mySlug):

	if slugIsValid(mySlug):
		allObjects = commonObject.objects.filter(slug = mySlug)
		allSubObjects = list()
		for object in allObjects:
			subObject = getattr(object, 'desktops')
			allSubObjects.append(subObject)

		return render(request, 'inventory/displayAll.html', {'allObjects':allSubObjects, 'objectName': 'Desktops'})

def detailDesktop(request, desktop_id):
	return HttpResponse("hello")