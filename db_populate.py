# A population script used to pull a large csv dataset into a sqlite3 db
import os, csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bwell_challenge.settings")

import django
django.setup()

from healthdata_api.models import Disease

def add_case(item):
    case = Disease.objects.get_or_create(disease_name=item[0],
        county=item[1],
        year=int(item[2]),
        sex = item[3],
        number_of_cases = int(item[4]),
        population = int(item[5]),
        rate = float(item[6]),
        CI_lower = float(item[7]),
        CI_upper = float(item[8])
        )[0]

    case.save()

if __name__ == '__main__':
    print("db population underway")
    count = 0
    with open('infectious-disease-cases-by-county-year-and-sex-2-27-19.csv', 'rb') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                add_case(row)
                count += 1
            except:
                pass
    print('Database population complete. %s records added. 132,927 expected.' % count)
