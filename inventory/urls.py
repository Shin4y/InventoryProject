from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	#path('<desktops/int:desktop_id>/', views.detailDesktop, name = 'detailDesktop'),
	path('<desktops/createDesktop/', views.createDesktop, name = 'createDesktop'),
	path('<desktops/thanks/', views.thanks, name = 'thanks'),
	]