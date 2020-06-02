from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.response import Response

from observations_api import serializers
from observations_api import models


class SpeciesViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SpeciesSerializer
    queryset = models.Species.objects.all()


class ObservationViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ObservationSerializer

    def get_queryset(self):
        return models.Observation.objects.filter(observer=self.request.user.id)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(observer=self.request.user)



#TODO: Make it dynamic and useful. Play with the permissions to get better understanding.
class DashboardViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    serializer_class = serializers.ObservationSerializer