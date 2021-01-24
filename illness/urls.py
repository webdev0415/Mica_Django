from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import CategoryView, IllnessView

router = routers.DefaultRouter()
router.register(r'category', CategoryView, 'category')
router.register(r'illness', IllnessView, 'illness')

urlpatterns = [
    path('', include(router.urls)),
]
