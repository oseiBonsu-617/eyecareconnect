from datetime import datetime
from django.db.models import Count
from django.db.models import Q
from django.utils.timezone import make_aware
from patients.models import Patient
from exams.models import Examination, Refraction, OcularAssessment


def parse_dates(start_date, end_date):
    start = make_aware(datetime.strptime(start_date, "%Y-%m-%d")) if start_date else None
    end = make_aware(datetime.strptime(end_date, "%Y-%m-%d")) if end_date else None
    return start, end


def get_overview_stats(start_date=None, end_date=None):
    exams = Examination.objects.all()
    patients = Patient.objects.all()

    if start_date and end_date:
        start, end = parse_dates(start_date, end_date)
        exams = exams.filter(created_at__range=(start, end))
        patients = patients.filter(created_at__range=(start, end))

    return {
        "total_patients": patients.count(),
        "total_examinations": exams.count(),
    }



def get_screening_stats():
    glaucoma = OcularAssessment.objects.filter(
        intraocular_pressure__gte=21,
        cup_disc_ratio__gte=0.5
    ).count()

    cataract = OcularAssessment.objects.filter(
        cataract_present=True
    ).count()

    return {
        "glaucoma_suspects": glaucoma,
        "cataract_cases": cataract,
    }





def get_refractive_error_stats():
    myopia = Refraction.objects.filter(
        Q(sphere_right__lte=-0.50) | Q(sphere_left__lte=-0.50)
    ).count()

    hyperopia = Refraction.objects.filter(
        Q(sphere_right__gte=0.50) | Q(sphere_left__gte=0.50)
    ).count()

    emmetropia = Refraction.objects.filter(
        Q(sphere_right__gt=-0.50, sphere_right__lt=0.50),
        Q(sphere_left__gt=-0.50, sphere_left__lt=0.50)
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
