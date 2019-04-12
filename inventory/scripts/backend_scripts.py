import os, sys
import django
import random


sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')
django.setup()

from inventory import models

print models.InventoryItem.objects.count()

for i in xrange(100):
	item = models.InventoryItem(
			name='I' + str(i), 
			quantity=random.randint(100, 10000)
		)
	print "item crated", item
	item.save()