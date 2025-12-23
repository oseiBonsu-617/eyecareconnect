from rest_framework.test import APITestCase
from django.urls import reverse
from accounts.models import User
from patients.models import Patient
from exams.models import Examination


class AnalyticsBaseTest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin",
            password="pass1234",
            role="admin"
        )

        self.assistant = User.objects.create_user(
            username="assistant",
            password="pass1234",
            role="assistant"
        )

        self.patient = Patient.objects.create(
            first_name="John",
            last_name="Doe"
        )

        self.exam = Examination.objects.create(
            patient=self.patient,
            examiner=self.admin
        )


class OverviewAnalyticsTests(AnalyticsBaseTest):

    def test_admin_can_access_overview(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.get("/analytics/overview/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("total_patients", response.data)

    def test_assistant_cannot_access_analytics(self):
        self.client.force_authenticate(user=self.assistant)

        response = self.client.get("/analytics/overview/")
        self.assertEqual(response.status_code, 403)

    def test_date_filtering(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.get(
            "/analytics/overview/?start_date=2025-01-01&end_date=2025-12-31"
        )
        self.assertEqual(response.status_code, 200)
