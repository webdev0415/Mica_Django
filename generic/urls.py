from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import BodyPartsView

router = routers.DefaultRouter()
router.register(r'all', BodyPartsView, 'all')

urlpatterns = [
    path('bodyparts', include(router.urls)),
]
