from django.test import TestCase, Client
from inventory.models import *
from django.urls import reverse

testData = {'name':'test', 'building':'WWH', 'room':'test', 'Notes':'test', 'modelName':'test', 'user':'test',
 'serialNumber':'1234', 'macAddress':'1234', 'OS':'test', 'userType':'test'}

testDataUpdate = {'name':'updated', 'building':'WWH', 'room':'test', 'Notes':'test', 'modelName':'test', 'user':'test',
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

	def testEditForm(self):
		c = Client()
		response = c.post(reverse('inventory:createObject', args = ['desktops']), testData)
		desktop = Desktops.objects.get(OS = 'test')
		response = c.post(reverse('inventory:editObject', args = ['desktops', desktop.token]), testDataUpdate)
		self.assertEqual(Desktops.objects.get(OS = 'test').name, 'updated')

	def testDisplayAllObjects(self):
		c = Client()
		response = c.post(reverse('inventory:createObject', args = ['desktops']), testData)
		response2 = c.post(reverse('inventory:createObject', args = ['desktops']), testDataUpdate)
		response3 = c.get(reverse('inventory:displayAllObjects', args = ['desktops']))

		self.assertEqual(response3.__class__.__name__, "HttpResponse")

	def testBatchReplace(self):
		return

	def testFaviconIcon(self):
		return

	def testToStorage(self):
		return

# Create your tests here.
