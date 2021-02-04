from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import TreatmentTypeRefModelView
router = routers.DefaultRouter(trailing_slash=False)
router = routers.DefaultRouter()
router.register(r'types', TreatmentTypeRefModelView, 'types')

urlpatterns = [
    path('', include(router.urls)),
]
