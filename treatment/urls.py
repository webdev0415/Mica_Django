from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import TreatmentTypeRefDescView, TreatmentTypeRefModelView

router = routers.DefaultRouter()
router.register(r'types', TreatmentTypeRefModelView, 'types')

urlpatterns = [
    path('', include(router.urls)),
]
