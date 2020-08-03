from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'inventory'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<slug:mySlug>/id=<str:secret_id>/', views.editObject, name = 'editObject'),
	path('<slug:mySlug>/create/', views.createObject, name = 'createObject'),
	path('<slug:mySlug>/', views.displayAllObjects, name = 'displayAllObjects'),
	path('<slug:mySlug>/sort=<str:sortBy>/', views.displayAllObjects, name = 'displayAllObjects'),
	path('<slug:mySlug>/batch/', views.batchReplace, name = 'batchReplace'),
	path('<slug:mySlug>/toStorage/<str:name>/<str:room>/<str:building>', views.toStorage, name = 'toStorage'),
	]