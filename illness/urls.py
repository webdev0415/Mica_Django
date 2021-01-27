from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import IllnessListView, IllnessCreateView, IllnessUpdateView

router = routers.DefaultRouter()
# router.register(r'illness', IllnessView, 'illness')

urlpatterns = [
    # path('', include(router.urls)),
    path('create', IllnessCreateView.as_view()),
    path('<str:icd10_code>/', IllnessListView.as_view()),
    path('<str:icd10_code>/update', IllnessUpdateView.as_view()),
]

