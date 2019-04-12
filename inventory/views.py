# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

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


class InventoryItemListGenerics(generics.ListCreateAPIView):
    """
    List all items, or create a new item.
    """

    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    pagination_class = PageNumberPagination

    #TODO: pagination

    def list(self, request):
        print self.request.GET
        queryset = self.get_queryset()
        serializer = InventoryItemSerializer(queryset, many=True)
        return Response(serializer.data)


