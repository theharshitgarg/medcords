from rest_framework import serializers
from django.core import exceptions
from .models import InventoryItem


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ("id", "quantity", "name")


class PurchaseItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    quantity = serializers.IntegerField(read_only=True)


class PurchaseSerializer(serializers.Serializer):
    items = PurchaseItemSerializer(many=True)

    def update_inventory(self):
        errors = []
        objs = {
            "passed": [],
            "failed": [],
        }

        for item in self.data['items']:
            try:
                item_obj = InventoryItem.objects.get(id=item["id"])
                item_obj.purchase(item["quantity"])
                objs["passed"].append({
                    "status": True,
                    "id": item_obj,
                })

            except exceptions.ObjectDoesNotExist as err:
                errors.append({"id": item["id"], "error": "Invalid ID"})
                objs["failed"].append({
                    "status": False,
                    "id": item["id"],
                })

            except Exception as err:
                errors.append({"id": item["id"], "error": str(err)})
                objs["failed"].append({
                    "status": False,
                    "id": item["id"],
                })

        resp = {
            "status": True,
            "errors": [],
        }

        if not objs["failed"]:
            resp["status"] = False
            resp["errors"] = {
                "des": "Update failed",
                "errors": errors
            }
        else:
            for obj in objs["passed"]:
                obj["id"].save()

        return resp
