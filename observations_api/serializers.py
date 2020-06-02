from rest_framework import serializers
from observations_api import models


class SpeciesSerializer(serializers.ModelSerializer):
    """Serializer for species data"""
    class Meta:
        model = models.Species
        fields = ['id','name','sc_name']


class ObservationSerializer(serializers.ModelSerializer):
    """Serializer for observation related data"""
    class Meta:
        model = models.Observation
        fields = ['id','species','observer','country','state','location','lat','long']
        extra_kwargs = {'observer': {'read_only': True},
                        'species': {'read_only': True}}


