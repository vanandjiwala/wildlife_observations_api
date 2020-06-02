from rest_framework.routers import DefaultRouter
from django.urls import path, include
from observations_api import views


router = DefaultRouter()
router.register('species',views.SpeciesViewSet,base_name='species')
router.register('observations',views.ObservationViewSet,base_name='observations')
router.register('dashboard',views.ObservationViewSet,base_name='dashboard')

urlpatterns = [
    path('', include(router.urls)),
]