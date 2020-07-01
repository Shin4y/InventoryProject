from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import *
# Create your views here.

def index(request):
	return HttpResponse("Hello, world.")

def createDesktop(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = DesktopForm(request.POST)
		# check whether it's valid:

		if form.is_valid():
			data = request.POST.copy()
			newDesktop = Desktops(name=data.get('name'), locationType=data.get('locationType'), location=data.get('name'),
				dateLastModified=datetime.datetime.now(), Notes=data.get('Notes'), modelName=data.get('modelName'), user=data.get('user'),
				serialNumber=data.get('serialNumber'), macAddress=data.get('macAddress'), IPAddress=data.get('IPAddress'),
				OS=data.get('OS'), userType=data.get('userType'))

			newDesktop.save()

			time = datetime.datetime.now()

			response = 'The current time is %s'
			return HttpResponse("Response: " + response % time)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = DesktopForm()

		return render(request, 'inventory/createDesktop.html', {'form': form})

def thanks(request):
	return HttpResponse("Thanks for creating a desktop.")

def detailDesktop(request, desktop_id):
	return HttpResponse("hello")