from rest_framework import serializers
from healthdata_api.models import Disease

class DiseaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disease
        fields = '__all__'
