from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from .views import IllnessDataView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'illness', IllnessDataView, basename='illness')
urlpatterns = [
    path('', include(router.urls)), 
]

