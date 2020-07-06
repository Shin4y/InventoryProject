from django.urls import path

from . import views

app_name = 'inventory'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('desktops/<int:desktop_id>/', views.detailDesktop, name = 'detailDesktop'),
	path('desktops/createDesktop/', views.createDesktop, name = 'createDesktop'),
	path('desktops/thanks/', views.thanks, name = 'thanks'),
	path('desktops/<int:desktop_id>/edit/', views.editDesktop, name = 'editDesktop'),
	path('desktops/displayAllDesktops/', views.displayAllDesktops, name = 'displayAllDesktops'),
	]