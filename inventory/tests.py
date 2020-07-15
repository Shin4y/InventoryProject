from django.test import TestCase
from inventory.models import *

class ObjectTestCase(TestCase):
	def setUp(self):
		desktop = Desktops.objects.create(name = "test", user = "user1", slug = "desktop")
		notebook = Notebooks.objects.create(name = "test", user = "user2", slug = "notebooks")

	def existsAsCommonObject(self):
		commonObjects = commonObject.objects.filter(name = "test")
		self.assertEqual(commonObjects.count(), 2)

	def existsAsDesktop(self):
		desktop =  Desktops.objects.get(name = "test")
		self.assertEqual(desktop.user, 'user1')

	def existsAsNotebook(self):
		notebook = Notebooks.objects.get(name = "test")
		self.assertEqual(notebook.user, 'user2')

	def databaseLinksExist(self):
		r = commonObject.objects.get(user = "user1")
		p = commonObject.objects.get(user = "user2")
		desktop = getattr(r, r.slug)
		self.assertEqual(r.__class__.__name__, "Desktops")
		self.assertEqual(p.__class__.__name__, "Notebooks")

	def testCreateForm(self):
		data = {
			'name' : 'formtest'
			'user' : 'testperson'
			'slug' : 'desktop'
		}

		response = self.client.POST(reverse('inventory:createObject'), data)
		# requires some reading and testing that I don't really want to do right now for 
		# the next 3 tests

	def testEditForm(self):
		return

	def displayAllObjects(self):
		return



# Create your tests here.
