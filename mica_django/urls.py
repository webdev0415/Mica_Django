"""mica_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include,re_path
# from illness.views import IllnessDataView
# from rest_framework import routers


# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'illness', IllnessDataViewSet, basename='illness')

urlpatterns = [
    # re_path('2070Services/mica/api/', include((router.urls, "api"), namespace="api")),
    re_path('2070Services/mica/api/', include('illness.urls')),
    path('admin/', admin.site.urls),
    # path('treatment/', include('treatment.urls')),
    # path('generic/', include('generic.urls')),
    path('2070Services/mica/api/template/', include('template.urls')),
    # path('treatment/', include('treatment.urls')),
    # path('generic/', include('generic.urls')),
    # path('illness/', include('illness.urls')),
]
