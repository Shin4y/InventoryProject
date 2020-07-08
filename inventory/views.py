from django.shortcuts import render
from django.http import HttpResponse
import datetime, secrets
from .helper import *
from .models import *
from collections import OrderedDict
# Create your views here.



def index(request):
	return HttpResponse("Hello, world.")

def createDesktop(request, mySlug):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		data = request.POST
		breakhere
		# check whether it's valid:

		if form.is_valid():
			newDesktop = form.save()
			newDesktop.token = secrets.token_urlsafe(20)
			newDesktop.time = datetime.datetime.now()
			#need to add the user thing here
			newDesktop.save()
			
			return redirect('inventory/displayAllDesktops.html')

	# if a GET (or any other method) we'll create a blank form
	else:
		f = DesktopForm()
		constructor = globals()[mySlug.capitalize()]
		subObject = constructor()
		for key in subObject._meta.fields:
			f.fields[key.name] = forms.CharField()


		return render(request, 'inventory/createDesktop.html', {'form': f, 'mySlug': mySlug.capitalize})


def editDesktop(request, secret_id):

	editDesktop = Desktops.objects.get(id = secret_id)
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = DesktopForm(request.POST)
		# check whether it's valid:

		if form.is_valid():
			data = request.POST.copy()
			#newDesktop = Desktops(name=data.get('name'), locationType=data.get('locationType'), location=data.get('name'),
			#	dateLastModified=datetime.datetime.now(), Notes=data.get('Notes'), modelName=data.get('modelName'), user=data.get('user'),
			#	serialNumber=data.get('serialNumber'), macAddress=data.get('macAddress'), IPAddress=data.get('IPAddress'),
			#	OS=data.get('OS'), userType=data.get('userType'))
			
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

	allObjects = commonObject.objects.filter(slug = mySlug)
	allSubObjects = list()
	for object in allObjects:
		subObject = getattr(object, 'desktops')
		allSubObjects.append(subObject)

	return render(request, 'inventory/displayAll.html', {'allObjects':allSubObjects, 'objectName': 'Desktops'})

def detailDesktop(request, desktop_id):
	return HttpResponse("hello")