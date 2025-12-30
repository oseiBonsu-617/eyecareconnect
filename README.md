# EyeCareConnect

## Overview
## Features
## Tech Stack
## Project Architecture
## Authentication
## API Endpoints
## Sprint Breakdown
## Setup Instructions
## Running Tests
## Future Improvements


# 👁️ EyeCareConnect API  
A Clinical Eye Screening & Record Management System  
Built with Django REST Framework & JWT Authentication  

---

## 📌 Overview  
EyeCareConnect is a backend API designed to support small eye clinics, optometry practices, and community-based vision screening teams.

It provides a secure, modular system to manage:  
- Patient records  
- Clinical examinations  
- Visual acuity  
- Refraction  
- Ocular health assessments  
- Screening flags (glaucoma, cataract)  
- Basic analytics  

This project is developed as part of a Capstone Project, following agile sprints and clean backend architecture.

---

## ✨ Features  
### **Authentication & Authorization**
## Authentication

EyeCareConnect uses JWT-based authentication via Djoser and SimpleJWT.

### Login
```http
POST /auth/jwt/create/

Authorization: Bearer <access_token>
```
- JWT-based authentication  
- Custom `User` model with roles: `admin`, `clinician`, `assistant`  
- Role-based access (optional extensions)

### **Patient Management**
- Create, read, update, delete patient records  
- Link patients to the user (examiner/creator)

### **Clinical Examination Module**
- Examination record with nested components:
  - Visual Acuity
  - Refraction
  - Ocular Assessment  
- Optional: upload fundus or anterior segment images

### **Analytics**
- Total number of patients  
- Screening counts for glaucoma/cataract  
- Refractive error distribution  

---

## Project Architecture

EyeCareConnect follows a modular, service-oriented backend architecture using Django and Django REST Framework.

Each domain is isolated into its own Django app:
- `accounts` handles authentication, user roles, and permissions.
- `patients` manages patient demographic records.
- `exams` stores structured clinical examination data.
- `analytics` provides read-only reporting and insights.

Business logic is separated from API views using a service layer (`services.py`) to improve maintainability, testability, and scalability. Views remain thin and focused on request/response handling.

Role-based access control is enforced through custom DRF permissions to ensure data security and clinical integrity.


## 🏗 Technology Stack
- **Python 3.10+**  
- **Django 4+**  
- **Django REST Framework**  
- **SimpleJWT (JWT Auth)**  
- **MySQL**  
- **Pillow** (for image uploads)  
- **drf-spectacular** (OpenAPI docs)

---

## Setup Instructions

```bash
git clone https://github.com/yourusername/eyecareconnect.git
cd eyecareconnect
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/oseiBonsu-617/eyecareconnect.git
cd eyecareconnect

## Sprint 2 – Clinical Examinations Module

### Features Implemented
- Examination creation and management linked to patients
- Visual acuity recording per examination
- Refraction data capture for both eyes
- Ocular assessment recording (e.g., glaucoma and cataract indicators)
- Role-based permissions for clinical data modification

### Technical Highlights
- Modular Django app design (`exams`)
- Nested endpoints using Django REST Framework viewsets
- Custom permissions to restrict modification based on user roles
- Validation logic to prevent duplicate clinical entries per examination
- JWT-authenticated endpoints
- Automated tests covering:
  - Examination creation and retrieval
  - Visual acuity creation and duplication prevention
  - Permission enforcement for assistants vs clinicians

### Key API Endpoints
| Endpoint | Description |
|--------|------------|
| `POST /exams/` | Create a new examination |
| `GET /exams/{id}/` | Retrieve examination details |
| `GET /exams/{id}/visual_acuity/` | View visual acuity results |
| `POST /exams/{id}/visual_acuity/` | Add visual acuity |
| `GET /exams/{id}/refraction/` | View refraction data |
| `POST /exams/{id}/refraction/` | Add refraction data |
| `GET /exams/{id}/ocular_assessment/` | View ocular assessment |
| `POST /exams/{id}/ocular_assessment/` | Add ocular assessment |

### Sprint Outcome
Sprint 2 established the core clinical data layer of EyeCareConnect. The system now supports structured eye examinations with proper validation, permissions, and automated testing, forming the foundation for analytics and reporting in subsequent sprints.


## Sprint 3 – Analytics & Reporting

### Features Implemented
- Clinical analytics dashboard endpoints
- Overview statistics (patients & examinations)
- Screening insights (glaucoma & cataract indicators)
- Refractive error distribution
- Clinician activity tracking

### Technical Highlights
- Service-layer analytics architecture
- Role-based access control (Admin & Clinician only)
- Date-range filtering support
- Automated analytics tests

### Endpoints
| Endpoint | Description |
|--------|------------|
| /analytics/overview/ | Summary statistics |
| /analytics/screening/ | Screening indicators |
| /analytics/refractive-errors/ | Refractive error distribution |
| /analytics/clinicians/ | Exams per clinician |
```