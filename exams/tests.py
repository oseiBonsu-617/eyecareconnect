from django.urls import reverse
from rest_framework.test import APITestCase

from patients.models import Patient
from exams.models import Examination
from accounts.models import User

class BaseExamTest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin",
            password="admin123",
            role="admin"
        )
        self.clinician = User.objects.create_user(
            username="clinician",
            password="clinician123",
            role="clinician"
        )
        self.assistant = User.objects.create_user(
            username="assistant",
            password="assistant123",
            role="assistant"
        )

        self.patient = Patient.objects.create(
            first_name="Test",
            last_name="Patient",
            created_by=self.clinician
        )

        # Login as clinician by default
        token = self.client.post(
            "/auth/jwt/create/",
            {"username": "clinician", "password": "clinician123"}
        ).data["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")


class ExaminationTests(BaseExamTest):

    def test_create_exam(self):
        response = self.client.post("/exams/", {
            "patient": self.patient.id,
            "notes": "Routine eye exam"
        })
        self.assertEqual(response.status_code, 201)

    def test_list_exams_for_patient(self):
        Examination.objects.create(
            patient=self.patient,
            examiner=self.clinician
        )
        response = self.client.get(f"/exams/?patient_id={self.patient.id}")
        self.assertEqual(response.status_code, 200)


class VisualAcuityTests(BaseExamTest):

    def setUp(self):
        super().setUp()
        self.exam = Examination.objects.create(
            patient=self.patient,
            examiner=self.clinician
        )

    def test_add_visual_acuity(self):
        response = self.client.post(
            f"/exams/{self.exam.id}/visual_acuity/",
            {
                "distance_va_right": "6/6",
                "distance_va_left": "6/9"
            }
        )
        self.assertEqual(response.status_code, 201)

    def test_prevent_duplicate_visual_acuity(self):
        self.client.post(
            f"/exams/{self.exam.id}/visual_acuity/",
            {
                "distance_va_right": "6/6",
                "distance_va_left": "6/9"
            }
        )
        response = self.client.post(
            f"/exams/{self.exam.id}/visual_acuity/",
            {
                "distance_va_right": "6/12",
                "distance_va_left": "6/12"
            }
        )
        self.assertEqual(response.status_code, 400)


class PermissionTests(BaseExamTest):

    def setUp(self):
        super().setUp()
        self.exam = Examination.objects.create(
            patient=self.patient,
            examiner=self.clinician
        )

    def test_assistant_cannot_modify_exam(self):
        token = self.client.post(
            "/auth/jwt/create/",
            {"username": "assistant", "password": "assistant123"}
        ).data["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

        response = self.client.delete(f"/exams/{self.exam.id}/")
        self.assertEqual(response.status_code, 403)
