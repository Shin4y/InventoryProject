from django.urls import path

from . import views

app_name = 'inventory'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<slug:mySlug>/<str:secret_id>/', views.editDesktop, name = 'editDesktop'),
	path('<slug:mySlug>/create/', views.createObject, name = 'createObject'),
	path('<slug:mySlug>/', views.displayAllObjects, name = 'displayAllObjects'),
	]