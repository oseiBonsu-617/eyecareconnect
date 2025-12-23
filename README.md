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

## 🏗 Technology Stack
- **Python 3.10+**  
- **Django 4+**  
- **Django REST Framework**  
- **SimpleJWT (JWT Auth)**  
- **MySQL**  
- **Pillow** (for image uploads)  
- **drf-spectacular** (OpenAPI docs)

---

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
