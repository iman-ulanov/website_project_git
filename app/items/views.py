from django.shortcuts import render
from rest_framework import viewsets

from website_project_git.app.items.models import Item
from website_project_git.app.items.serializers import ItemSerializer


# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
