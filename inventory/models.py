# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class InventoryItem(models.Model):
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " : " + str(self.quantity)

    @property
    def is_available(self):
        return self.check_quantity()

    def check_quantity(self, quantity=0):
        return self.quantity >= quantity

    def purchase(self, quantity):
        resp = {
            "errros": [],
            "status": True
        }
        if quantity > 0 and self.check_quantity(quantity):
            self.quantity -= quantity

        else:
            raise Exception("Invalid Quantity")

# class PurchaseItem(models.Model):
# 	purchased_on = models.DateTimeField(default=timezone.now)
# 	items = models.ListField()


# class Purchase(models.Model):
# 	purchased_on = models.DateTimeField(default=timezone.now)
# 	items = models.

# 	def __unicode__(self):
# 		return self.purchased_on.strftime("%d %b %Y %H:%M:%S")

# 	def is_available(self):
# 		return self.quantity > 0
