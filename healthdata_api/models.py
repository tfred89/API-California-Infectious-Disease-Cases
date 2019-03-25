# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Disease(models.Model):
    disease_name = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    year = models.IntegerField()
    sex = models.CharField(max_length=20)
    number_of_cases = models.IntegerField()
    population = models.IntegerField()
    rate = models.FloatField()
    CI_lower = models.FloatField()
    CI_upper = models.FloatField()

    def __str__(self):
        return "{} - {} County - {}".format(self.disease_name, self.county, self.year)

    class Meta:
        ordering = ('year', 'county')
