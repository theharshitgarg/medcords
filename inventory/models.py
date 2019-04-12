# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class InventoryItem(models.Model):
	quantity = models.IntegerField(default=0)
	name = models.CharField(max_length=100)


	def __unicode__(self):
		return self.name + " : " + self.quantity

	def is_available(self):
		return self.quantity > 0

	