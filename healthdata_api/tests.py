# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Disease
from .serializers import DiseaseSerializer


# test for model functionality
class BaseModelTest(APITestCase):
    def setUp(self):
        self.a_case = Disease.objects.create(
            disease_name='night blindness',
            county='orange',
            year=2030,
            sex='male',
            number_of_cases=100,
            population=100000,
            rate=0.1,
            CI_lower=0.0,
            CI_upper=0.4
        )

    def test_db(self):
        self.assertEqual(self.a_case.disease_name, 'night blindness')
        self.assertEqual(self.a_case.county, 'orange')
        self.assertEqual(self.a_case.year, 2030)
        self.assertEqual(self.a_case.rate, 0.1)
        self.assertEqual(self.a_case.CI_upper, 0.4)


# tests for API views
class ViewTestCase(BaseModelTest):
    client = APIClient()
    # 'post' test for API, including previously added test data
    def test_create_case(self):
        url = reverse('api:case_list-list')
        data = {'disease_name':'fatigue',
                'county':'mendocino',
                'year':2019,
                'sex':'female',
                'number_of_cases':10,
                'population':10000,
                'rate':0.1,
                'CI_lower':0.2,
                'CI_upper':0.3
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Disease.objects.count(), 2)
        self.assertEqual(Disease.objects.get(pk=2).disease_name, 'fatigue')

    # 'get' request to test API
    def test_get_all_data(self):
        #call endpoint
        url = reverse('api:case_list-list')
        response = self.client.get(url, format='json')

        #retrieve from DB
        expected = Disease.objects.all()
        serialized = DiseaseSerializer(expected, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serialized.data)
