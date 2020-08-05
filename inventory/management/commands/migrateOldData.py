from django.core.management.base import BaseCommand, CommandError
from inventory.models import *
import csv
import sqlite3
from sqlite3 import Error

idDict = {'1':'DesktopScanners', '2':'Desktops', '3':'MacDisplayAdapter', '4':'Desktops', '5':'Printers', '6':'Software', 
'7':'StationaryProjectors','8':'Notebooks','9':'Notebooks','10':'Desktops','11':'Peripherals','12':'Peripherals',
'13':'Peripherals', '14':'Peripherals','15':'', '16':''}

fieldDict = {'Given To':'user', 'Model':'model', 'Machine Name':'name', 'Dell Tag':'serialNumber', 'Serial Num':'serialNumber',
'Hardware (MAC) Address':'macAddress', 'Operating System':'OS', 'Comments':'Notes', 'OS Running':'OS','IP Address':'IpAddress',
'HardwareAddress':'macAddress'}
class Command(BaseCommand):
    help = 'migrating old database to new database'

    def add_arguments(self, parser):
       pass

   def create_connection():
       """ create a database connection to a database that resides
           in the memory
       """
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

    	conn = create_connection()
    	cur = conn.cursor()
		with open('inventoryItems.csv', newline = '') as file:
			reader = csv.DictReader(csvfile)
			for row in reader:
				constructor = globals()[idDict[row['inventory_category_id']]]
				obj = constructor()
				obj.room = row['room']
				obj.building = row['building']
				obj.lastUpdatedUser = row['updated_by']
				obj.dateLastModified = row['updated_at']
				cur.execute("SELECT * FROM inventoryData WHERE inventory_item_id = '4'")
				rows = cur.fetchall()

				for subRow in rows:
					setattr(obj, fieldDict[row[field]], row[value])
				obj.save()
