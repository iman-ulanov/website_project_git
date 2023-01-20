from rest_framework import serializers

from website_project_git.app.items.models import Item


class ItemSerializer(serializers.Serializer):
    class Meta:
        model = Item
        fields = '__all__'
