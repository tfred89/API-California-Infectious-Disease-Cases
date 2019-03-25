# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, renderers, viewsets
from rest_framework.response import Response
from healthdata_api.models import Disease
from healthdata_api.serializers import DiseaseSerializer

# Model view of all preventable disease cases by county in California since 2001
class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

''' For the following three views, only the first 10 results are displayed
to avoid large query sets on a single page. With more time, it is better practice
to manually confgiure the pagination settings of non-generic viewsets
'''
#Model view of preventable disease cases diplayed by specified year
class YearDetailView(viewsets.ModelViewSet):
    def get_queryset(self):
        if 'year' in self.kwargs:
            return Disease.objects.filter(year=self.kwargs['year'])[:10]
        else:
            return Disease.objects.all()

    lookup_field = 'year'
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

#Model view of preventable disease cases diplayed by specified county
class CountyDetailView(viewsets.ModelViewSet):
    def get_queryset(self):
        if 'county' in self.kwargs:
            return Disease.objects.filter(county=self.kwargs['county'])[:10]
        else:
            return Disease.objects.all()

    lookup_field = 'county'
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

#Model view of preventable disease cases diplayed by specified disease name
class DiseaseDetailView(viewsets.ModelViewSet):
    def get_queryset(self):
        if 'disease_name' in self.kwargs:
            return Disease.objects.filter(disease_name=self.kwargs['disease_name'])[:10]
        else:
            return Disease.objects.all()

    lookup_field = 'disease_name'
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)
