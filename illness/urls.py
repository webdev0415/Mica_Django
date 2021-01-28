from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from .views import IllnessDataViewSet, IllnessListView, IllnessCreateView, IllnessUpdateView

router = routers.DefaultRouter()
# router.register(r'illness', IllnessView, 'illness')
router.register(r'illness/', IllnessDataViewSet, 'illness')
urlpatterns = [
    path('', include(router.urls)), 
    # path('create', IllnessCreateView.as_view()),
    # path('<str:icd10_code>/', IllnessDataViewSet, 'illness'),
    # path('<str:icd10_code>/update', IllnessUpdateView.as_view()),
]

