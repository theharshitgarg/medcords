# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import csrf_exempt

from .models import InventoryItem
from .serializers import InventoryItemSerializer
from . import serializers


class InventoryItemPagination(PageNumberPagination):
    page_size_query_param = 'per_page'

    def get_paginated_response(self, data):
        return JsonResponse({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total': self.page.paginator.count,
            'count': self.get_page_size(self.request),
            'results': data,
        })


class InventoryItemListGenerics(generics.ListCreateAPIView):
    """
    List all items, or crate a new item.
    """

    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    pagination_class = InventoryItemPagination

    def list(self, request):
        paginated_queryset = self.paginate_queryset(self.get_queryset())
        serializer = InventoryItemSerializer(paginated_queryset, many=True)

        return self.get_paginated_response(serializer.data)


class InventoryPurchaseGenerics(generics.CreateAPIView):
    """
    Make a purchase, either all items are purchased or nore.
    """

    serializer_class = serializers.PurchaseSerializer

    def update_inventory(self):
        s = serializers.PurchaseSerializer(self.request.data)
        resp = s.update_inventory()

        return resp

    def post(self, request):
        response = self.update_inventory()

        return JsonResponse(response)
