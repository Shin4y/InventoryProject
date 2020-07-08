from django.urls import path

from . import views

app_name = 'inventory'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('Desktops/<int:secret_id>/', views.editDesktop, name = 'editDesktop'),
	path('<slug:mySlug>/createDesktop/', views.createDesktop, name = 'createDesktop'),
	path('<slug:mySlug>/', views.displayAllObjects, name = 'displayAllObjects'),
	]