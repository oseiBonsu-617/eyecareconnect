from rest_framework import serializers
from .models import Examination, VisualAcuity, Refraction, OcularAssessment


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = "__all__"
        read_only_fields = ('examiner',)


class VisualAcuitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualAcuity
        fields = "__all__"

    def validate(self, data):
        if not data.get("distance_va_right") or not data.get("distance_va_left"):
            raise serializers.ValidationError(
                "Distance visual acuity is required for both eyes."
            )
        return data


class RefractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refraction
        fields = "__all__"

    def validate_axis_right(self, value):
        if value is not None and not 0 <= value <= 180:
            raise serializers.ValidationError("Axis must be between 0 and 180.")
        return value

    def validate_axis_left(self, value):
        if value is not None and not 0 <= value <= 180:
            raise serializers.ValidationError("Axis must be between 0 and 180.")
        return value


class OcularAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcularAssessment
        fields = "__all__"
