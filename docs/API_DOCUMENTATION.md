# Dokumentasi API
## Journal Mengajar Online & Absensi Siswa
### SMK Negeri 1 Lemahabang

---

## 📋 Daftar Isi
1. [Base URL & Authentication](#base-url--authentication)
2. [Endpoints Authentication](#endpoints-authentication)
3. [Endpoints Journal Mengajar](#endpoints-journal-mengajar)
4. [Endpoints Absensi](#endpoints-absensi)
5. [Endpoints Kurikulum](#endpoints-kurikulum)
6. [Endpoints Dashboard](#endpoints-dashboard)
7. [Response Format](#response-format)
8. [Error Handling](#error-handling)

---

## 🔗 Base URL & Authentication

### Base URL
```
http://localhost:8000/api
```

### Authentication
Semua endpoint (kecuali login/register) memerlukan Bearer Token di header:
```
Authorization: Bearer <access_token>
```

### Dokumentasi Interaktif
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## 🔐 Endpoints Authentication

### 1. Register (Pendaftaran Pengguna)
```http
POST /auth/register
Content-Type: application/json

{
    "email": "guru.baru@smk.ac.id",
    "username": "guru_baru",
    "full_name": "Nama Guru Baru",
    "password": "password123",
    "role": "guru",
    "nip": "198512121987031001"
}
```

**Response 201 (Created):**
```json
{
    "id": 5,
    "email": "guru.baru@smk.ac.id",
    "username": "guru_baru",
    "full_name": "Nama Guru Baru",
    "role": "guru",
    "is_active": true
}
```

### 2. Login (Masuk)
```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

email=guru@smk.ac.id&password=guru123456
```

**Response 200 (OK):**
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "user": {
        "id": 1,
        "email": "guru@smk.ac.id",
        "full_name": "Budi Santoso, S.Kom.",
        "role": "guru"
    }
}
```

### 3. Get Current User Profile
```http
GET /auth/me
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "id": 1,
    "email": "guru@smk.ac.id",
    "username": "guru_tkj_1",
    "full_name": "Budi Santoso, S.Kom.",
    "role": "guru",
    "nip": "198505151010011001",
    "phone": "082123456789",
    "is_active": true,
    "created_at": "2024-01-15T08:30:00"
}
```

### 4. Change Password
```http
POST /auth/change-password
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "old_password": "guru123456",
    "new_password": "guru_password_baru_123"
}
```

**Response 200 (OK):**
```json
{
    "message": "Password berhasil diubah"
}
```

---

## 📚 Endpoints Journal Mengajar

### 1. Create Journal Entry (Buat Entri Journal)
```http
POST /journal
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "class_id": 1,
    "date": "2024-01-20T08:00:00",
    "subject": "Sistem Bilangan Digital",
    "kd_id": 1,
    "module_id": 1,
    "material_summary": "Pembelajaran tentang sistem bilangan biner, oktal, desimal, dan heksadesimal. Siswa melakukan praktik konversi antar sistem bilangan.",
    "learning_method": "Diskusi dan Praktik",
    "learning_activities": "1. Diskusi interaktif 2. Praktik konversi bilangan 3. Latihan soal",
    "student_attendance": 32,
    "assessment_method": "Kuis formatif dan penugasan",
    "achievement_notes": "Siswa sudah memahami konversi bilangan dasar",
    "challenges": "Beberapa siswa masih kesulitan dengan konversi heksadesimal",
    "media_used": "Projector, whiteboard, laptop",
    "follow_up_notes": "Perlu penjelasan lebih lanjut untuk konversi heksadesimal di pertemuan berikutnya"
}
```

**Response 201 (Created):**
```json
{
    "id": 1,
    "teacher_id": 1,
    "class_id": 1,
    "date": "2024-01-20T08:00:00",
    "subject": "Sistem Bilangan Digital",
    "material_summary": "...",
    "learning_method": "Diskusi dan Praktik",
    "student_attendance": 32,
    "is_submitted": false,
    "is_verified": false,
    "created_at": "2024-01-20T09:30:00"
}
```

### 2. Get All Journals (Daftar Semua Journal)
```http
GET /journal?skip=0&limit=10&start_date=2024-01-01&end_date=2024-01-31&class_id=1
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `skip`: Jumlah record yang dilewati (default: 0)
- `limit`: Jumlah record yang ditampilkan (default: 10)
- `start_date`: Filter tanggal awal (format: YYYY-MM-DD)
- `end_date`: Filter tanggal akhir (format: YYYY-MM-DD)
- `class_id`: Filter berdasarkan kelas

**Response 200 (OK):**
```json
{
    "total": 5,
    "items": [
        {
            "id": 1,
            "teacher_id": 1,
            "class_id": 1,
            "date": "2024-01-20T08:00:00",
            "subject": "Sistem Bilangan Digital",
            "material_summary": "...",
            "is_submitted": false,
            "is_verified": false
        }
    ]
}
```

### 3. Get Journal Detail
```http
GET /journal/{journal_id}
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "id": 1,
    "teacher_id": 1,
    "class_id": 1,
    "date": "2024-01-20T08:00:00",
    "subject": "Sistem Bilangan Digital",
    "material_summary": "...",
    "learning_method": "Diskusi dan Praktik",
    "student_attendance": 32,
    "assessment_method": "Kuis formatif dan penugasan",
    "achievement_notes": "Siswa sudah memahami konversi bilangan dasar",
    "challenges": "Beberapa siswa masih kesulitan dengan konversi heksadesimal",
    "media_used": "Projector, whiteboard, laptop",
    "follow_up_notes": "Perlu penjelasan lebih lanjut untuk konversi heksadesimal di pertemuan berikutnya",
    "is_submitted": false,
    "is_verified": false,
    "created_at": "2024-01-20T09:30:00",
    "updated_at": "2024-01-20T09:30:00"
}
```

### 4. Update Journal Entry
```http
PUT /journal/{journal_id}
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "subject": "Sistem Bilangan Digital (Updated)",
    "material_summary": "Updated material summary...",
    "student_attendance": 31
}
```

**Response 200 (OK):**
```json
{
    "id": 1,
    "subject": "Sistem Bilangan Digital (Updated)",
    "material_summary": "Updated material summary...",
    "student_attendance": 31,
    "updated_at": "2024-01-20T10:45:00"
}
```

### 5. Submit Journal
```http
POST /journal/{journal_id}/submit
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "id": 1,
    "is_submitted": true,
    "submitted_at": "2024-01-20T10:50:00"
}
```

### 6. Delete Journal Entry
```http
DELETE /journal/{journal_id}
Authorization: Bearer <access_token>
```

**Response 204 (No Content):**
```
(No response body)
```

---

## 📋 Endpoints Absensi

### 1. Record Attendance (Catat Absensi)
```http
POST /attendance
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "student_id": 1,
    "class_id": 1,
    "date": "2024-01-20",
    "status": "hadir",
    "notes": ""
}
```

**Status Options:** `hadir`, `sakit`, `izin`, `alfa`, `libur`

**Response 201 (Created):**
```json
{
    "id": 1,
    "student_id": 1,
    "class_id": 1,
    "date": "2024-01-20T00:00:00",
    "status": "hadir",
    "created_at": "2024-01-20T08:00:00"
}
```

### 2. Bulk Record Attendance (Catat Absensi Massal)
```http
POST /attendance/bulk
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "class_id": 1,
    "date": "2024-01-20",
    "records": [
        {"student_id": 1, "status": "hadir"},
        {"student_id": 2, "status": "sakit", "notes": "Demam"},
        {"student_id": 3, "status": "izin"}
    ]
}
```

**Response 201 (Created):**
```json
{
    "created": 3,
    "message": "3 attendance records berhasil dibuat"
}
```

### 3. Get Student Attendance (Lihat Absensi Siswa)
```http
GET /attendance/{student_id}?start_date=2024-01-01&end_date=2024-01-31
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "student_id": 1,
    "total_days": 20,
    "hadir": 18,
    "sakit": 1,
    "izin": 1,
    "alfa": 0,
    "attendance_percentage": 90,
    "records": [
        {
            "id": 1,
            "date": "2024-01-20",
            "status": "hadir"
        }
    ]
}
```

### 4. Get Class Attendance Summary (Ringkasan Absensi Kelas)
```http
GET /attendance/class/{class_id}?date=2024-01-20
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "class_id": 1,
    "date": "2024-01-20",
    "total_students": 32,
    "hadir": 30,
    "sakit": 1,
    "izin": 1,
    "alfa": 0,
    "attendance_rate": 93.75,
    "details": [
        {
            "student_id": 1,
            "student_name": "Ahmad Hidayat",
            "status": "hadir"
        }
    ]
}
```

### 5. Submit Attendance Permit (Ajukan Surat Izin)
```http
POST /attendance/permits
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

{
    "student_id": 1,
    "start_date": "2024-01-22",
    "end_date": "2024-01-24",
    "reason": "Sakit dan memerlukan istirahat",
    "permit_type": "Sakit",
    "document": <file>  // optional
}
```

**Response 201 (Created):**
```json
{
    "id": 1,
    "student_id": 1,
    "start_date": "2024-01-22",
    "end_date": "2024-01-24",
    "reason": "Sakit dan memerlukan istirahat",
    "permit_type": "Sakit",
    "status": "pending",
    "created_at": "2024-01-20T10:00:00"
}
```

### 6. Approve Attendance Permit (Setujui Surat Izin)
```http
POST /attendance/permits/{permit_id}/approve
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "approval_notes": "Izin disetujui dengan syarat membawa surat dari orang tua"
}
```

**Response 200 (OK):**
```json
{
    "id": 1,
    "status": "approved",
    "approved_at": "2024-01-20T11:00:00"
}
```

---

## 📖 Endpoints Kurikulum

### 1. Get KI/KD List (Daftar KI/KD)
```http
GET /curriculum/ki-kd?grade=10&kd_number=3.1
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "items": [
        {
            "id": 1,
            "grade": 10,
            "ki": {
                "ki_number": 3,
                "description": "Memahami, menerapkan, dan menganalisis..."
            },
            "kd_number": "3.1",
            "description": "Menjelaskan konsep dasar sistem bilangan digital",
            "learning_indicators": "Siswa dapat menjelaskan sistem bilangan..."
        }
    ]
}
```

### 2. Get ATP List (Daftar ATP)
```http
GET /curriculum/atp?grade=10&fase=D
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "items": [
        {
            "id": 1,
            "grade": 10,
            "fase": "D",
            "subject_code": "TKOM101",
            "subject_name": "Sistem Bilangan Digital",
            "learning_objectives": "Peserta didik dapat memahami...",
            "duration_weeks": 4
        }
    ]
}
```

### 3. Get Teaching Modules (Daftar Modul Pembelajaran)
```http
GET /curriculum/modules?atp_id=1&difficulty_level=Mudah
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "items": [
        {
            "id": 1,
            "atp_id": 1,
            "module_number": "Modul 1",
            "title": "Pengenalan Sistem Bilangan",
            "description": "Modul pembelajaran dasar...",
            "learning_outcomes": "Peserta didik mampu memahami...",
            "duration_hours": 8,
            "difficulty_level": "Mudah"
        }
    ]
}
```

### 4. Get Deep Learning Programs (Daftar Program Pembelajaran Mendalam)
```http
GET /curriculum/deep-learning?grade=10
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "items": [
        {
            "id": 1,
            "grade": 10,
            "title": "Project: Sistem Keamanan Jaringan",
            "description": "Program pembelajaran mendalam tentang...",
            "phase_one": "Problem Understanding: Analisis masalah keamanan jaringan...",
            "phase_two": "Knowledge Construction: Pelajari konsep keamanan...",
            "phase_three": "Application & Reflection: Implementasi solusi..."
        }
    ]
}
```

---

## 📊 Endpoints Dashboard

### 1. Admin Dashboard (Dashboard Admin)
```http
GET /dashboard/admin/summary
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "summary": {
        "total_users": 15,
        "total_teachers": 8,
        "total_students": 96,
        "total_classes": 3,
        "total_journals": 450
    },
    "recent_activities": [
        {
            "timestamp": "2024-01-20T10:50:00",
            "action": "Guru Budi Santoso mengirimkan journal mengajar",
            "actor": "Budi Santoso",
            "type": "journal_submission"
        }
    ],
    "statistics": {
        "journals_this_month": 120,
        "average_attendance_rate": 92.5,
        "pending_permissions": 3
    }
}
```

### 2. Teacher Dashboard (Dashboard Guru)
```http
GET /dashboard/teacher/my-summary
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "teacher_id": 1,
    "teacher_name": "Budi Santoso, S.Kom.",
    "summary": {
        "total_journals_this_month": 20,
        "submitted_journals": 18,
        "pending_journals": 2,
        "verified_journals": 18
    },
    "classes": [
        {
            "class_id": 1,
            "class_name": "X TKJ A",
            "total_students": 32,
            "average_attendance": 91.5
        }
    ],
    "recent_journals": [
        {
            "id": 1,
            "date": "2024-01-20",
            "class_name": "X TKJ A",
            "subject": "Sistem Bilangan Digital",
            "is_submitted": true,
            "is_verified": true
        }
    ]
}
```

### 3. Student Dashboard (Dashboard Siswa)
```http
GET /dashboard/student/my-summary
Authorization: Bearer <access_token>
```

**Response 200 (OK):**
```json
{
    "student_id": 1,
    "student_name": "Ahmad Hidayat",
    "class": "X TKJ A",
    "summary": {
        "attendance_rate": 93.75,
        "hadir": 30,
        "sakit": 1,
        "izin": 1,
        "alfa": 0
    },
    "pending_permissions": [
        {
            "id": 1,
            "reason": "Sakit",
            "start_date": "2024-01-22",
            "end_date": "2024-01-24",
            "status": "pending"
        }
    ]
}
```

---

## 📨 Response Format

### Success Response
```json
{
    "status": "success",
    "code": 200,
    "message": "Data berhasil diambil",
    "data": {
        // response data
    }
}
```

### Error Response
```json
{
    "status": "error",
    "code": 400,
    "message": "Validation error",
    "errors": [
        {
            "field": "email",
            "message": "Email sudah terdaftar"
        }
    ]
}
```

---

## ⚠️ Error Handling

### Common Error Codes

| Code | Message | Description |
|------|---------|-------------|
| 400 | Bad Request | Request tidak valid |
| 401 | Unauthorized | Token tidak valid atau expired |
| 403 | Forbidden | User tidak memiliki akses |
| 404 | Not Found | Resource tidak ditemukan |
| 409 | Conflict | Data sudah ada/conflict |
| 422 | Unprocessable Entity | Validasi gagal |
| 500 | Internal Server Error | Error di server |

### Contoh Error Response
```json
{
    "status": "error",
    "code": 401,
    "message": "Unauthorized",
    "detail": "Token tidak valid atau expired"
}
```

---

## 🔄 Rate Limiting

- **Limit**: 1000 requests per jam per IP
- **Header Response**: 
  - `X-RateLimit-Limit`: 1000
  - `X-RateLimit-Remaining`: Requests tersisa
  - `X-RateLimit-Reset`: Timestamp reset

---

## 📌 Notes

1. Semua endpoint (kecuali `/auth/login` dan `/auth/register`) memerlukan autentikasi
2. Role-based access control diterapkan pada setiap endpoint
3. Semua timestamp menggunakan format ISO 8601 (UTC)
4. File upload maksimal 10MB

---

**Last Updated**: 2026-01-26
**Version**: 1.0.0
