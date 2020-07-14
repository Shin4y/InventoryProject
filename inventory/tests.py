from django.test import TestCase
from inventory.models import *

class ObjectTestCase(TestCase):
	def setUp(self):
		desktop = Desktop(name = "test", slug = "desktop")
		
# Create your tests here.
