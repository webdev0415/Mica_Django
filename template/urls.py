from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import SymptomsView, CategoryView, SectionView, SymptomGroupsView

router = routers.DefaultRouter()
router.register(r'symptomgroups', SymptomGroupsView, 'symptomgroups')

urlpatterns = [
    path('', include(router.urls)),
]
