from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import SymptomView, CategoryView, SectionView, SymptomGroupView

router = routers.DefaultRouter()
router.register(r'symptomgroups', SymptomGroupView, 'symptomgroups')

urlpatterns = [
    path('', include(router.urls)),
]
