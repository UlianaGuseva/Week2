from .models import Report, Forecaster
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    forecaster = serializers.HyperlinkedIdentityField(view_name='forecaster')
    class Meta:
        model = Report
        fields = '__all__'
        
class ForecasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Forecaster
        fields = '__all__'