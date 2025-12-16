from patients.models import Patient
from exams.models import Examination, Refraction, OcularAssessment
from django.db.models import Count


def get_overview_stats():
    return {
        "total_patients": Patient.objects.count(),
        "total_examinations": Examination.objects.count(),
    }


def get_screening_stats():
    return {
        "glaucoma_suspects": OcularAssessment.objects.filter(
            glaucoma_suspect=True
        ).count(),
        "cataract_cases": OcularAssessment.objects.filter(
            cataract_present=True
        ).count(),
    }


def get_refractive_error_stats():
    myopia = Refraction.objects.filter(
        sphere_right__lte=-0.50
    ).count()

    hyperopia = Refraction.objects.filter(
        sphere_right__gte=0.50
    ).count()

    emmetropia = Refraction.objects.filter(
        sphere_right__gt=-0.50,
        sphere_right__lt=0.50
    ).count()

    return {
        "myopia": myopia,
        "hyperopia": hyperopia,
        "emmetropia": emmetropia,
    }


def get_clinician_activity():
    return (
        Examination.objects
        .values("examiner__username")
        .annotate(total_exams=Count("id"))
        .order_by("-total_exams")
    )
