from django.test import TestCase, Client
from inventory.models import *
from django.urls import reverse

testData = {'name':'test', 'locationType':'WWH', 'location':'test', 'Notes':'test', 'modelName':'test', 'user':'test',
 'serialNumber':'1234', 'macAddress':'1234', 'OS':'test', 'userType':'test'}


class ObjectTestCase(TestCase):
	def setUp(self):
		desktop = Desktops.objects.create(name = "test", modelName = "model1", slug = "desktops")
		notebook = Notebooks.objects.create(name = "test", modelName = "model2", slug = "notebooks")

	def testExistsAsCommonObject(self):
		commonObjects = commonObject.objects.filter(name = "test")
		self.assertEqual(commonObjects.count(), 2)

	def testExistsAsDesktop(self):
		desktop =  Desktops.objects.get(name = "test")
		self.assertEqual(desktop.modelName, 'model1')

	def testExistsAsNotebook(self):
		notebook = Notebooks.objects.get(name = "test")
		self.assertEqual(notebook.modelName, 'model2')

	def testDatabaseLinksExist(self):
		r = commonObject.objects.get(modelName = "model1")
		p = commonObject.objects.get(modelName = "model2")
		desktop = getattr(r, r.slug)
		notebook = getattr(p, p.slug)
		self.assertEqual(desktop.__class__.__name__, "Desktops")
		self.assertEqual(notebook.__class__.__name__, "Notebooks")

	def testCreateForm(self):
		 
		c = Client()
		response = c.post(reverse('inventory:createObject', args = ['desktops']), testData)
		self.assertEqual(response.__class__.__name__, 'HttpResponseRedirect')
		self.assertEqual(Desktops.objects.get(OS = 'test').macAddress, '1234')

		# requires some reading and testing that I don't really want to do right now for 
		# the next 3 tests

	def testEditForm(self):
		c = Client()
		desktop = Desktops.objects.get(OS = 'test')
		secret = desktop.token
		response = c.post(reverse('inventory:editObject', args = [token, 'desktops']), )
		return

	def displayAllObjects(self):
		return



# Create your tests here.
