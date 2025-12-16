from django.db import models
from django.conf import settings
from patients.models import Patient

# Create your models here.
class Examination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='examinations')
    examiner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    exam_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Exam {self.id} - {self.patient}"
    

class VisualAcuity(models.Model):
    examination = models.OneToOneField(Examination, on_delete=models.CASCADE, related_name='visual_acuity')
    distance_va_right = models.CharField(max_length=10)
    distance_va_left = models.CharField(max_length=10)
    near_va_right = models.CharField(max_length=10, blank=True)
    near_va_left = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"VA - Exam {self.examination.id}"

class Refraction(models.Model):
    examination = models.OneToOneField(
        Examination,
        on_delete=models.CASCADE,
        related_name="refraction"
    )

    sphere_right = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    cylinder_right = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    axis_right = models.PositiveIntegerField(null=True, blank=True)

    sphere_left = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    cylinder_left = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    axis_left = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Refraction - Exam {self.examination.id}"

class OcularAssessment(models.Model):
    examination = models.OneToOneField(
        Examination,
        on_delete=models.CASCADE,
        related_name="ocular_assessment"
    )

    anterior_segment = models.TextField(blank=True)
    posterior_segment = models.TextField(blank=True)

    glaucoma_suspect = models.BooleanField(default=False)
    cataract_present = models.BooleanField(default=False)

    def __str__(self):
        return f"Ocular Assessment - Exam {self.examination.id}"
