from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Examination)
class ExaminationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'examiner', 'exam_date', 'notes']


@admin.register(models.VisualAcuity)
class VisualAcuityAdmin(admin.ModelAdmin):
    list_display = ['distance_va_right', 'distance_va_left', 'near_va_right', 'near_va_left']

@admin.register(models.Refraction)
class RefractionAdmin(admin.ModelAdmin):
    list_display = ['sphere_right', 'cylinder_right', 'axis_right', 'sphere_left', 'cylinder_left', 'axis_left']


@admin.register(models.OcularAssessment)
class OcularAssessmentAdmin(admin.ModelAdmin):
    list_display = ['anterior_segment', 'posterior_segment', 'glaucoma_suspect', 'cataract_present']