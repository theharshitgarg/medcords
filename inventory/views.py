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


class InventoryItemListGenerics(generics.ListCreateAPIView):
    """
    List all items, or create a new item.
    """

    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    pagination_class = PageNumberPagination

    def get_paginated_response(self, page=1, per_page=10):
        paginator = Paginator(self.queryset, per_page)
        return paginator.page(page)


    def list(self, request):
        page = self.request.GET.get('page')
        per_page = self.request.GET.get('per_page')

        paginated_queryset = self.get_paginated_response(page, per_page)
        serializer = InventoryItemSerializer(paginated_queryset, many=True)
        json = {
            'page': page,
            'data': serializer.data,
            'per_page': request.GET['per_page'],
            'total': paginated_queryset.end_index()-paginated_queryset.start_index()+1
        }

        return Response(json)
