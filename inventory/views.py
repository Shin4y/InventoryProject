from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Hello, world.")

def createDesktop(request):
	return HttpResponse("Hello")

def thanks(request):
	return HttpResponse("Thanks for creating a desktop.")

def detailDesktop(request):
	return HttpResponse("hello")