# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.core.paginator import Paginator


from .models import InventoryItem
from .serializers import InventoryItemSerializer


@csrf_exempt
def inventory_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class InventoryItemPagination(PageNumberPagination):
    page_size_query_param = 'per_page'

    def get_paginated_response(self, data):
        return Response({
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
