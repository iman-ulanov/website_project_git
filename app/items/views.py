from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
