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
