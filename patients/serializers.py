from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Patient
        fields = ['id', 'patient_id', 'first_name', 'last_name', 'age', 'gender', 'contact', 'address', 'created_by']