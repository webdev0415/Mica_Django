from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import BodyPartView

router = routers.DefaultRouter()
router.register(r'all', BodyPartView, 'all')

urlpatterns = [
    path('bodyparts', include(router.urls)),
]
