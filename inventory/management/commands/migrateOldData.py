from django.core.management.base import BaseCommand, CommandError
from inventory.models import *
import csv
import sqlite3
import sys
from sqlite3 import Error

idDict = {'Stationary Projectors':'Stationaryprojectors', 'Portable Projectors':'Peripherals', 'Projector Lamps':
'Bulbs', 'Printers':'Printers','Mac':'Macs', 'Macs':'Macs', 'Dell Laptops':'Notebooks', 'Desktop Scanners':'Desktopscanners',
'Desktops':'Desktops', 'Notebooks':'Notebooks','Peripherals':'Peripherals', 'Data Center Equipment':'Datacenterequipment'}

fieldDict = {'Given To':'user', 'Model':'modelName', 'Machine Name':'name', 'Dell Tag':'serialNumber', 'Serial Num':'serialNumber',
'Hardware (MAC) Address':'macAddress', 'Operating System':'OS', 'Comments':'Notes', 'OS Running':'OS','IP Address':'IpAddress',
'HardwareAddress':'macAddress', 'Serial Number':'serialNumber', 'User':'user', 'Hardware Address':'macAddress', 'Bulb':'bulb', 'Name':'name',
'Model #':'serialNumber', 'Caretaker':'user', 'OS':'OS', 'User Type':'userType', 'Notes':'Notes', 'Printer Name':'name', 'Part Number':'partNumber',
'Model Number':'modelNumber', 'Model Name':'modelName', 'Manufacture Year':'manufactureYear', 'Size':'size', 'AppleCare Registration Number':'appleCareNumber',
'Designation':'name', 'Given Date':'givenDate', 'AppleCare Expiration Date':'appleCareExpirationDate', 'Purchase Date':'purchaseDate', 'Purpose':'purpose', 'Printer Type':'printerType',
'Description':'Notes', 'Loaned To':'user', 'Loaned Date':'givenDate', 'Serial':'serialNumber', 'Make':'make', 'Hostname':'name'}
class Command(BaseCommand):
	help = 'migrating old database to new database'

	def add_arguments(self, parser):
	   pass

	def create_connection():
	   conn = None;
	   try:
		   conn = sqlite3.connect('sqlite/db/temp.db')
		   return conn
	   except Error as e:
		   print(e)
	   finally:
		   if conn:
			   conn.close()

	def handle(self, *args, **options):	

		conn = sqlite3.connect('inventory/management/commands/sqlite/db/temp.db')
		cur = conn.cursor()

		cur.execute("SELECT * FROM inv_items")
		data = cur.fetchall()
		flag = False
		show = False
		found = False
		counter = 20000000
		for row in data:
			#print(row)
			if row[1] != '':
				if flag:
					obj.save()
					#print("THE OBJ MODEL IS:" + obj.modelName)
					pass
				cur.execute("SELECT * FROM inv_categories WHERE _id__$oid =" +"'"+row[1]+"'")
				cat = cur.fetchall()
				print(cat[0][1])
				for subrow in cat:
					if subrow[5] == "Supplies" or subrow[5] == "Software":
						continue 
					name = subrow[1]
					constructor = globals()[idDict[name]]
					obj = constructor()
					obj.slug = (idDict[name]).lower()
					obj.dateLastModified = row[6]
				obj.token = row[0]
				obj.room = row[10]
				obj.building = row[9]
				obj.qrcode = 'https://cims.nyu.edu/webapps/inventory/equipment/' +obj.token+'/edit'
				if row[14] == 'Location Type' or row[14] == 'Cartridge Type' or row[14] == 'Printer Count' or row[14]=='Type' or row[14] =='Asset Tag':
					continue
				setattr(obj, fieldDict[row[14]], row[15])
				if counter != 0:
					print(fieldDict[row[14]] + ":" + row[15])
					counter = counter-1

			else:
				flag = True
				if row[14] == 'Location Type' or row[14] == 'Cartridge Type' or row[14] == 'Printer Count' or row[14]=='Type' or row[14] =='Asset Tag':
					continue
				if row[15] == 'fhd':
					counter = 10
					found = True
				setattr(obj, fieldDict[row[14]], row[15])
				if counter != 0:						
					print(fieldDict[row[14]] + ":" + row[15])
					print(obj.modelName)
					counter = counter-1

			if found == True and counter == 0:
				d = Desktops.objects.get(name='fhd')
				if d.modelName != 'Precision T3600':
					print("changed modelName to: " + d.modelName)
					Desktops.objects.all().delete()
					Notebooks.objects.all().delete()
					Macs.objects.all().delete()
					Printers.objects.all().delete()
					Stationaryprojectors.objects.all().delete()
					Desktopscanners.objects.all().delete()
					Datacenterequipment.objects.all().delete()
					Peripherals.objects.all().delete()
					CommonObject.objects.all().delete() 
					sys.exit()














