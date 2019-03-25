"""bwell_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from healthdata_api import views
from rest_framework import routers

''' rest_framework routers used to handle automatic URL routing. The following
paths are available:
/api/v1/california-disease-cases                 - list view of all cases
/api/v1/california-disease-cases/<primary key>   - detail view of indiviudal instance
/api/v1/cases-by-year/<year>                     - view of cases in a given year 2001 onward
/api/v1/cases-by-county/<county>                 - view of cases by county name
/api/v1/cases-by-disease/<disease_name           - view of cases by disease name
'''
router = routers.DefaultRouter()
router.register(r'california-disease-cases', views.DiseaseViewSet, base_name='case_list')
router.register(r'cases-by-year', views.YearDetailView)
router.register(r'cases-by-county', views.CountyDetailView)
router.register(r'cases-by-disease', views.DiseaseDetailView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls, namespace='api')),
]
