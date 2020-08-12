from django.core.management.base import BaseCommand, CommandError
from inventory.models import *
import csv
import sqlite3
from sqlite3 import Error

idDict = {'Stationary Projectors':'StationaryProjectors', 'Portable Projectors':'Peripherals', 'Projector Lamps':
'Bulbs', 'Printers':'Printers','Mac':'Macs', 'Macs':'Macs', 'Dell Laptops':'Notebooks', 'Desktop Scanners':'DesktopScanners',
'Desktops':'Desktops', 'Notebooks':'Notebooks','Peripherals':'Peripherals', 'Data Center Equipment':'DataCenterEquipment'}

fieldDict = {'Given To':'user', 'Model':'modelName', 'Machine Name':'name', 'Dell Tag':'serialNumber', 'Serial Num':'serialNumber',
'Hardware (MAC) Address':'macAddress', 'Operating System':'OS', 'Comments':'Notes', 'OS Running':'OS','IP Address':'IpAddress',
'HardwareAddress':'macAddress', 'Serial Number':'serialNumber', 'User':'user', 'Hardware Address':'macAddress', 'Bulb':'bulb', 'Name':'name',
'Model #':'serialNumber', 'Caretaker':'user', 'OS':'OS', 'User Type':'userType', 'Notes':'Notes', 'Printer Name':'name', 'Part Number':'partNumber',
'Model Number':'modelNumber', 'Model Name':'modelName', 'Manufacture Year':'manufactureYear', 'Size':'size', 'AppleCare Registration Number':'appleCareNumber',
'Designation':'name', 'Given Date':'givenDate', 'AppleCare Expiration Date':'appleCareExpirationDate', 'Purchase Date':'purchaseDate', 'Purpose':'purpose', 'Printer Type':'modelName',
'Description':'Notes', 'Loaned To':'user', 'Loaned Date':'givenDate', 'Serial':'serialNumber'}
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
		first = False
		for row in data:
			print(row)
			if row[1] != '':
				if first:
					obj.save()
				cur.execute("SELECT * FROM inv_categories WHERE _id__$oid =" +"'"+row[1]+"'")
				cat = cur.fetchall()
				
				for subrow in cat:
					if subrow[5] == "Supplies" or subrow[5] == "Software":
						continue 
					name = subrow[1]
					constructor = globals()[idDict[name]]
					obj = constructor()
					obj.slug = (idDict[name]).lower()
				obj.token = row[0]
				obj.qrcode = 'http://http://127.0.0.1:8000/inventory/equipment/' + 'id=' + obj.token+'/edit' 

			else:
				first = True
				if row[14] == 'Location Type' or row[14] == 'Cartridge Type' or row[14] == 'Printer Count' or row[14]=='Type' or row[14] =='Asset Tag':
					continue
				print(row[14])
				setattr(obj, fieldDict[row[14]], row[15])

















		# with open('inventory/management/commands/inventoryItems.csv', newline = '') as file:
		# 	reader = csv.DictReader(file)
		# 	for row in reader:
		# 		try:
		# 			constructor = globals()[idDict[row['inventory_category_id']]]
		# 		except KeyError:
		# 			continue

		# 		obj = constructor()
		# 		obj.room = row['room']
		# 		obj.building = row['building']
		# 		obj.lastUpdatedUser = row['updated_by']
		# 		obj.dateLastModified = row['updated_at']
		# 		obj.slug = idDict[row['inventory_category_id']].lower()

		# 		cur.execute("SELECT * FROM inventoryData WHERE inventory_item_id =" + row['id'])
		# 		rows = cur.fetchall()

		# 		for subRow in rows:
		# 			if subRow[2] == 'sa6420160r':
		# 				continue
		# 			setattr(obj, fieldDict[subRow[2]], subRow[3])

		# 		#if obj.name == '' or obj.name == 'N/A':
		# 		#	continue
		# 		obj.save()


#delete from inventory_desktops;
#delete from inventory_datacenterequipment;
#delete from inventory_desktopscanners;
#delete from inventory_notebooks;
#delete from inventory_peripherals;
#delete from inventory_printers;
#delete from inventory_stationaryprojectors;