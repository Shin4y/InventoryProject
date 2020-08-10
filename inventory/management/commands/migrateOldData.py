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
'Model #':'serialNumber', 'Caretaker':'user', 'OS':'OS', 'User Type':'userType', 'Notes':'Notes', 'Printer Name':'name'}
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
			if row[1] != '':
				if first:
					obj.save()
				cur.execute("SELECT * FROM inv_categories WHERE _id__$oid =" +"'"+row[1]+"'")
				cat = cur.fetchall()
				print(len(cat))
				for row in cat:
					if row[5] == "Supplies" or row[5] == "Software":
						continue 
					name = row[1]
					constructor = globals()[idDict[name]]
					obj = constructor()

			else:
				first = True
				if row[14] == 'Location Type' or 'Cartridge Type':
					continue
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