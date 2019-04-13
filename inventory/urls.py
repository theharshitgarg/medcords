from django.conf.urls import url

# from .views import inventory_list
from inventory import views

urlpatterns = [
    url(r'purchase', views.InventoryPurchaseGenerics.as_view()),
    url(r'', views.InventoryItemListGenerics.as_view()),
]
