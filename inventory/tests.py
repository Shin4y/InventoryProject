from django.test import TestCase
from inventory.models import *

class ObjectTestCase(TestCase):
	def setUp(self):
		desktop = Desktops.objects.create(name = "test", user = "user1", slug = "desktop")
		notebook = Notebooks.objects.create(name = "test", user = "user2", slug = "notebooks")

	def existsAsCommonObject(self):
		commonObjects = commonObject.objects.filter(name = "test")
		self.assertEqual(commonObjects.count(), 2)

	def databaseLinksExist(self):
		r = commonObject.objects.get(user = "user1")
		p = commonObject.objects.get(user = "user2")
		desktop = getattr(r, r.slug)
		self.assertEqual(r.__class__.__name__, "Desktops")
		self.assertEqual(p.__class__.__name__, "Notebooks")



# Create your tests here.
