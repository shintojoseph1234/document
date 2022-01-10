"""
Serializers required for api app
"""
# REST imports
from rest_framework import serializers
# local imports
from api import models


class OverviewSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Overview API
    """
    url = serializers.HyperlinkedIdentityField(view_name="api:content-detail")

    class Meta:
        model = models.Content
        fields = (
            "url",
        )

class ContentSerializer(serializers.ModelSerializer):
    """
    Serializer for Content model
    """
    class Meta:
        model = models.Content
        fields = (
            "id",
            "title",
            "timestamp",
            "created_by",
        )


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for Tag model
    """
    class Meta:
        model = models.Tag
        fields = (
            "title",
        )
