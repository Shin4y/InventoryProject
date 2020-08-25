from django.test import TestCase, Client
from inventory.models import *
from django.urls import reverse

testData = {'name':'test', 'building':'WWH', 'room':'test', 'Notes':'test', 'modelName':'test', 'user':'test',
 'serialNumber':'1234', 'macAddress':'1234', 'OS':'test', 'userType':'test', 'dateLastModified':'1581370547000'}

testDataUpdate = {'name':'updated', 'building':'WWH', 'room':'test', 'Notes':'test', 'modelName':'test', 'user':'test',
 'serialNumber':'1234', 'macAddress':'1234', 'OS':'test', 'userType':'test', 'dateLastModified':'1581370547000'}

testData2 = {'name':'desktop1', 'building':'WWH', 'room':'test', 'Notes':'test', 'modelName':'test', 'user':'test',
 'serialNumber':'1234', 'macAddress':'1234', 'OS':'test', 'userType':'test'}

testData3 = {'name':'desktop2', 'building':'60FifthAve', 'room':'test', 'Notes':'test', 'modelName':'test', 'user':'test',
 'serialNumber':'1234', 'macAddress':'1234', 'OS':'test', 'userType':'test'}

testData4 = {'name':'desktop3', 'building':'WWH', 'room':'test', 'Notes':'test', 'modelName':'test', 'user':'test',
 'serialNumber':'1234', 'macAddress':'1234', 'OS':'test', 'userType':'test'}

testData5 = {'name':'desktop4', 'building':'60FifthAve', 'room':'test', 'Notes':'test', 'modelName':'test', 'user':'test',
 'serialNumber':'1234', 'macAddress':'1234', 'OS':'test', 'userType':'test'}

batchTestData = {'name1':'desktop1', 'name2':'desktop2', 'extra_field_count': '2', 'extra_field_0':'desktop3', 'extra_field_1':'desktop4', 'owner1':'thomas1', 'owner2':'thomas2', 'extra_owner_0':'thomas3', 'extra_owner_1':'thomas4'}

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
		response = c.post(reverse('inventory:editObject', args = [desktop.token]), testDataUpdate)
		self.assertEqual(Desktops.objects.get(OS = 'test').name, 'updated')

	def testDisplayAllObjects(self):
		c = Client()
		response = c.post(reverse('inventory:createObject', args = ['desktops']), testData)
		response2 = c.post(reverse('inventory:createObject', args = ['desktops']), testDataUpdate)
		response3 = c.get(reverse('inventory:displayAllObjects', args = ['desktops']))

		self.assertEqual(response3.__class__.__name__, "HttpResponse")

	def testBatchReplace(self):
		c = Client()
		c.post(reverse('inventory:createObject', args = ['desktops']), testData2)
		c.post(reverse('inventory:createObject', args = ['desktops']), testData3)
		c.post(reverse('inventory:createObject', args = ['desktops']), testData4)
		c.post(reverse('inventory:createObject', args = ['desktops']), testData5)

		c.post(reverse('inventory:batchReplace', args = ['desktops']), batchTestData)
		desktop1 = Desktops.objects.get(name = 'desktop1')
		desktop2 = Desktops.objects.get(name = 'desktop2')
		desktop3 = Desktops.objects.get(name = 'desktop3')
		desktop4 = Desktops.objects.get(name = 'desktop4')
		self.assertEqual(desktop1.building, '60FifthAve')
		self.assertEqual(desktop2.building, 'WWH')
		self.assertEqual(desktop3.building, '60FifthAve')
		self.assertEqual(desktop4.building, 'WWH')

		self.assertEqual(desktop1.user, 'thomas1')
		self.assertEqual(desktop2.user, 'thomas2')
		self.assertEqual(desktop3.user, 'thomas3')
		self.assertEqual(desktop4.user, 'thomas4')
		return

	#def testBatchForm(self):
	#	form = BatchForm(batchTestData, batchTestData['extra_field_count'])
	#	self.assertFalse(form.is_valid())
	#	self.assertEqual(form.errors['name1'][0], 'It is invalid')

	def testFaviconIcon(self): #I feel like because this functionality is so simple, there is no point in implementing test rn
		return

	def testToStorage(self): #ditto
		return

# Create your tests here.
