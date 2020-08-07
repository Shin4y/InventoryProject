from django.core.management.base import BaseCommand, CommandError
from inventory.models import *
import csv
import sqlite3
from sqlite3 import Error

idDict = {'1':'DesktopScanners', '2':'Desktops', '3':'MacDisplayAdapter', '4':'Desktops', '5':'Printers', '6':'Software', 
'7':'StationaryProjectors','8':'Notebooks','9':'Notebooks','10':'Desktops','11':'Peripherals','12':'Peripherals',
'13':'Peripherals', '14':'Peripherals','15':'', '16':''}

fieldDict = {'Given To':'user', 'Model':'modelName', 'Machine Name':'name', 'Dell Tag':'serialNumber', 'Serial Num':'serialNumber',
'Hardware (MAC) Address':'macAddress', 'Operating System':'OS', 'Comments':'Notes', 'OS Running':'OS','IP Address':'IpAddress',
'HardwareAddress':'macAddress', 'Serial Number':'serialNumber', 'User':'user', 'Hardware Address':'macAddress', 'Bulb':'bulb', 'Name':'name',
'Model #':'serialNumber', 'Caretaker':'user'}
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
		with open('inventory/management/commands/inventoryItems.csv', newline = '') as file:
			reader = csv.DictReader(file)
			for row in reader:
				try:
					constructor = globals()[idDict[row['inventory_category_id']]]
				except KeyError:
					continue

				obj = constructor()
				obj.room = row['room']
				obj.building = row['building']
				obj.lastUpdatedUser = row['updated_by']
				obj.dateLastModified = row['updated_at']
				obj.slug = idDict[row['inventory_category_id']].lower()

				cur.execute("SELECT * FROM inventoryData WHERE inventory_item_id =" + row['id'])
				rows = cur.fetchall()

				for subRow in rows:
					if subRow[2] == 'sa6420160r':
						continue
					setattr(obj, fieldDict[subRow[2]], subRow[3])

				#if obj.name == '' or obj.name == 'N/A':
				#	continue
				obj.save()


#delete from inventory_desktops;
#delete from inventory_datacenterequipment;
#delete from inventory_desktopscanners;
#delete from inventory_notebooks;
#delete from inventory_peripherals;
#delete from inventory_printers;
#delete from inventory_stationaryprojectors;