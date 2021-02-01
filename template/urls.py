from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from .views import SnomedCodeView, LogicalSymptomGroupView, SymptomTemplateView, SymptomCategoryView, SymptomGroupView
from .views import SymptomGroupView, SymptomCategoryView

router = routers.DefaultRouter()
router.register(r'symptomgroups', SymptomGroupView, 'symptomgroups')
# router.register(r'symptomtemplate', SymptomTemplateView, 'symptomtemplate')
# router.register(r'symptomcategory', SymptomCategoryView, 'symptomcategory')

urlpatterns = [
    path('', include(router.urls)),
]
