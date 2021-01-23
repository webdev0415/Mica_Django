from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from .views import TreatmentTypeRefDescView, TreatmentTypeRefModelView, TreatmentTypeView
from .views import DrugView, NonDrugView, TreatmentGroupView, TreatmentView
router = routers.DefaultRouter()
router.register(r'types', TreatmentView, 'types')
router.register(r'drug', DrugView, 'drug')
router.register(r'nondrug', NonDrugView, 'nondrug')
router.register(r'treatmentgroup', TreatmentGroupView, 'treatmentgroup')

urlpatterns = [
    path('', include(router.urls)),
]
