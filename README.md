# API-California-Infections-Disease-Cases
A django/django_rest_framework API outputting JSON data for all instances of infectious diseases in California since 2001

This project creates a REST API serving data for all infectious disease cases in California since 2001 with information on county,
year, disease type, and sex. The data was aquired from https://healthdata.gov/dataset/infectious-disease-cases-county-year-and-sex.

This project implements a SQLite3 database, populated from the db_populate.py script.
The 'healthdata_api' directory contains all relevant python/django files for the functioning API.

The 'views.py' file implements django_rest_framework's ModelViewSet, supporting GET, POST, PUT and DELETE methods. 

The URL configuration implements the following API endpoints:

/api/v1/california-disease-cases                 - list view of all cases
/api/v1/california-disease-cases/<primary key>   - detail view of indiviudal instance
/api/v1/cases-by-year/<year>                     - view of cases in a given year 2001 onward
/api/v1/cases-by-county/<county>                 - view of cases by county name
/api/v1/cases-by-disease/<disease_name>          - view of cases by disease name

Currently, the last three endpoints/views only display the first 10 results for a given query, as custom pagination did
not seem necessary at this time.
