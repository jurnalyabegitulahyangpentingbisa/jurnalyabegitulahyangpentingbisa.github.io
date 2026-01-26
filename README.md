# 📚 Journal Mengajar Online & Absensi Siswa
## SMK Negeri 1 Lemahabang - Teknik Komputer dan Jaringan

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)
![Oracle](https://img.shields.io/badge/Oracle-19c+-red)
![Status](https://img.shields.io/badge/Status-Development-yellow)

---

## 📋 Daftar Isi

- [Deskripsi Proyek](#deskripsi-proyek)
- [Fitur Utama](#fitur-utama)
- [Tech Stack](#tech-stack)
- [Struktur Proyek](#struktur-proyek)
- [Quick Start](#quick-start)
- [Dokumentasi](#dokumentasi)
- [Setup Database](#setup-database)
- [API Endpoints](#api-endpoints)
- [Panduan Kontribusi](#panduan-kontribusi)

---

## 📌 Deskripsi Proyek

Aplikasi **Journal Mengajar Online & Absensi Siswa** adalah sistem manajemen terpadu untuk:

- 📝 **Guru**: Mencatat jurnal mengajar harian dengan detail KI/KD, ATP, dan modul pembelajaran
- 📊 **Admin**: Mengelola data kurikulum, verifikasi journal, dan monitoring absensi
- 👥 **Siswa**: Melihat absensi, mengajukan surat izin, dan akses informasi pembelajaran
- 🏫 **Kepala Sekolah**: Dashboard ringkasan dan approval verifikasi

**Tingkat**: Kelas 10, 11, dan 12  
**Departemen**: Teknik Komputer dan Jaringan  
**Institusi**: SMK Negeri 1 Lemahabang

---

## ✨ Fitur Utama

### 🔐 Manajemen Pengguna
- ✅ Registrasi & Login dengan JWT
- ✅ Role-based access control (Admin, Guru, Siswa, Kepala Sekolah)
- ✅ Profile management
- ✅ Password hashing dengan bcrypt

### 📖 Journal Mengajar
- ✅ Buat/edit/hapus journal mengajar harian
- ✅ Integrase dengan KI/KD (Kurikulum 2013)
- ✅ Integrase dengan ATP/Modul (Kurikulum Merdeka)
- ✅ Catat metode pembelajaran, kegiatan, dan pencapaian
- ✅ Lampirkan file dan catatan
- ✅ Submit dan verifikasi journal
- ✅ Filter dan laporan berdasarkan tanggal

### 📋 Absensi Siswa
- ✅ Catat absensi per siswa atau massal
- ✅ Status: Hadir, Sakit, Izin, Alfa, Libur
- ✅ Sistem permohonan surat izin dengan approval flow
- ✅ Summary absensi per bulan
- ✅ Laporan attendance rate dan statistik

### 📚 Manajemen Kurikulum
- ✅ **KI/KD** (Kompetensi Inti & Dasar) - Kurikulum 2013
- ✅ **ATP** (Alur Tujuan Pembelajaran) - Kurikulum Merdeka
- ✅ **Modul Pembelajaran** - Structured learning modules
- ✅ **Pembelajaran Mendalam** - Deep learning programs dengan 3 fase
- ✅ Dukungan semua tingkat kelas (10, 11, 12)

### 📊 Dashboard
- ✅ **Dashboard Admin**: Statistik sistem, monitoring, user management
- ✅ **Dashboard Guru**: Ringkasan journal, data mengajar, kelas yang dibimbing
- ✅ **Dashboard Siswa**: Absensi pribadi, permohonan izin, informasi pembelajaran
- ✅ Real-time data aggregation

---

## 🛠️ Tech Stack

| Komponen | Teknologi | Alasan |
|----------|-----------|--------|
| **Backend** | Python FastAPI | Performa tinggi, async, dokumentasi otomatis |
| **Database** | Oracle 19c/21c | Skalabilitas, keandalan enterprise, multi-user |
| **ORM** | SQLAlchemy 2.0 | Flexible, support Oracle, production-ready |
| **Authentication** | JWT + bcrypt | Stateless, scalable, aman |
| **API Docs** | OpenAPI/Swagger | Dokumentasi interaktif otomatis |
| **Server** | Uvicorn | High-performance ASGI server |

---

## 📁 Struktur Proyek

```
jurnalyabegitulahyangpentingbisa.github.io/
│
├── backend/                          # Backend Python FastAPI
│   ├── app/
│   │   ├── auth/                    # Authentication & User Management
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   └── routes.py
│   │   ├── journal/                 # Journal Mengajar
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   └── routes.py
│   │   ├── attendance/              # Absensi Siswa
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   └── routes.py
│   │   ├── curriculum/              # KI/KD, ATP, Modul, Deep Learning
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   └── routes.py
│   │   ├── dashboard/               # Dashboard Endpoints
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   ├── core/                    # Core Configuration
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   └── main.py                  # Application Entry Point
│   ├── scripts/
│   │   ├── init_database.py         # Database Setup
│   │   └── seed_data.py             # Initial Data
│   ├── tests/                        # Unit & Integration Tests
│   ├── requirements.txt              # Python Dependencies
│   ├── .env.example                 # Environment Template
│   ├── run.py                       # Application Runner
│   └── README.md                    # Backend Documentation
│
├── frontend/                         # Frontend (Frontend - TODO)
│   ├── index.html
│   ├── dashboard-admin.html
│   ├── dashboard-guru.html
│   ├── dashboard-siswa.html
│   ├── css/
│   ├── js/
│   └── assets/
│
├── docs/                            # Dokumentasi
│   ├── DATABASE_DESIGN.md           # Database Schema & ERD
│   ├── API_DOCUMENTATION.md         # API Reference
│   ├── USER_GUIDE.md                # Panduan Pengguna
│   └── SETUP_GUIDE.md               # Panduan Setup
│
├── PANDUAN_SETUP.md                # Panduan Setup Lengkap
├── README.md                        # File ini
└── .gitignore
```

---

## 🚀 Quick Start

### Prasyarat
- Python 3.8+
- Oracle Database 19c atau 21c
- Git
- Virtual Environment

### 1. Clone Repository
```bash
git clone <repository-url>
cd jurnalyabegitulahyangpentingbisa.github.io
```

### 2. Setup Backend

```bash
cd backend

# Buat virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# atau untuk Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env dengan konfigurasi Oracle Anda
nano .env
```

### 3. Inisialisasi Database

```bash
# Buat semua tables
python scripts/init_database.py

# (Optional) Insert data awal
python scripts/seed_data.py
```

### 4. Jalankan Server

```bash
python run.py
# atau
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server akan berjalan di: **http://localhost:8000**

---

## 📚 Dokumentasi

| Dokumen | Deskripsi |
|---------|-----------|
| [PANDUAN_SETUP.md](PANDUAN_SETUP.md) | Panduan lengkap setup aplikasi |
| [backend/README.md](backend/README.md) | Dokumentasi backend |
| [docs/DATABASE_DESIGN.md](docs/DATABASE_DESIGN.md) | Database schema dan ERD |
| [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) | API endpoints reference |
| [docs/USER_GUIDE.md](docs/USER_GUIDE.md) | Panduan pengguna aplikasi |

---

## 🗄️ Setup Database

### Koneksi Oracle

Edit file `backend/.env`:

```env
ORACLE_USER=smk_admin
ORACLE_PASSWORD=your_password
ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SID=XE
ORACLE_CHARSET=UTF8
```

### Inisialisasi Tabel

```bash
cd backend
python scripts/init_database.py
```

### Data Awal (Optional)

```bash
python scripts/seed_data.py
```

### Tabel yang Dibuat

1. **users** - Data pengguna
2. **departments** - Departemen
3. **classes** - Kelas/rombongan belajar
4. **students** - Data siswa
5. **kompetensi_inti** - KI (Kurikulum 2013)
6. **kompetensi_dasar** - KD (Kurikulum 2013)
7. **alur_tujuan_pembelajaran** - ATP (Kurikulum Merdeka)
8. **teaching_modules** - Modul pembelajaran
9. **pembelajaran_mendalam** - Program deep learning
10. **teaching_journals** - Journal mengajar
11. **attendance** - Absensi siswa
12. **attendance_summary** - Ringkasan absensi
13. **attendance_permits** - Surat izin

Lihat [docs/DATABASE_DESIGN.md](docs/DATABASE_DESIGN.md) untuk detail lengkap.

---

## 🔌 API Endpoints

### Base URL
```
http://localhost:8000/api
```

### Dokumentasi Interaktif
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Contoh Endpoints

#### Authentication
```
POST   /auth/register          - Daftar user baru
POST   /auth/login             - Login
GET    /auth/me                - Get profile
POST   /auth/change-password   - Ganti password
```

#### Journal Mengajar
```
POST   /journal                - Buat journal
GET    /journal                - Daftar journal
GET    /journal/{id}           - Detail journal
PUT    /journal/{id}           - Update journal
DELETE /journal/{id}           - Hapus journal
POST   /journal/{id}/submit    - Submit journal
```

#### Absensi
```
POST   /attendance             - Catat absensi
POST   /attendance/bulk        - Catat absensi massal
GET    /attendance/{student_id} - Lihat absensi siswa
GET    /attendance/class/{class_id} - Ringkasan kelas
POST   /attendance/permits     - Ajukan surat izin
POST   /attendance/permits/{id}/approve - Approve izin
```

#### Kurikulum
```
GET    /curriculum/ki-kd       - Daftar KI/KD
GET    /curriculum/atp         - Daftar ATP
GET    /curriculum/modules     - Daftar modul
GET    /curriculum/deep-learning - Program deep learning
```

#### Dashboard
```
GET    /dashboard/admin/summary - Dashboard admin
GET    /dashboard/teacher/my-summary - Dashboard guru
GET    /dashboard/student/my-summary - Dashboard siswa
```

Lihat [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) untuk referensi lengkap.

---

## 🔐 Security

- ✅ Password hashing dengan bcrypt
- ✅ JWT token untuk authentication
- ✅ Role-based access control (RBAC)
- ✅ CORS protection
- ✅ Input validation dengan Pydantic
- ✅ SQL injection protection (SQLAlchemy ORM)

---

## 📊 Default Users (Seed Data)

| Email | Password | Role | Nama |
|-------|----------|------|------|
| admin@smk.ac.id | admin123456 | Admin | Administrator |
| guru.tkj1@smk.ac.id | guru123456 | Guru | Budi Santoso, S.Kom. |
| siswa.001@smk.ac.id | siswa123456 | Siswa | Ahmad Hidayat |

---

## 🛠️ Development

### Running Development Server
```bash
cd backend
source venv/bin/activate
python run.py
```

### Running Tests
```bash
pytest tests/
pytest --cov=app tests/
```

### Code Style
```bash
pip install black flake8
black app/
flake8 app/
```

---

## 🤝 Panduan Kontribusi

1. **Fork** repository ini
2. **Buat branch** fitur: `git checkout -b feature/nama-fitur`
3. **Commit** perubahan: `git commit -am 'feat: tambah fitur baru'`
4. **Push** ke branch: `git push origin feature/nama-fitur`
5. **Buat Pull Request**

### Commit Message Format
```
feat: tambah fitur baru
fix: perbaiki bug
docs: update dokumentasi
style: format kode
refactor: refactor code
test: tambah test
```

---

## 📞 Support & Kontak

**Institusi**: SMK Negeri 1 Lemahabang  
**Departemen**: Teknik Komputer dan Jaringan  
**Email**: it@smk1lemahabang.sch.id  

---

## 📄 Lisensi

Proprietary - SMK Negeri 1 Lemahabang

---

## 🎯 Roadmap

### Phase 1 (Current)
- ✅ Setup backend dengan FastAPI
- ✅ Database schema design
- ✅ Authentication & Authorization
- ⏳ API endpoints implementation

### Phase 2
- ⏳ Frontend development (HTML/CSS/JavaScript)
- ⏳ Dashboard UI
- ⏳ Integration testing

### Phase 3
- ⏳ Production deployment
- ⏳ Performance optimization
- ⏳ Advanced features (export, reporting, analytics)

---

## 📈 Status Pengembangan

| Fitur | Status | Progress |
|-------|--------|----------|
| User Management | ✅ Complete | 100% |
| Journal Mengajar | ✅ Complete | 100% |
| Absensi Siswa | ✅ Complete | 100% |
| Kurikulum (KI/KD) | ✅ Complete | 100% |
| Kurikulum (ATP) | ✅ Complete | 100% |
| Deep Learning | ✅ Complete | 100% |
| Dashboard Admin | ⏳ In Progress | 50% |
| Dashboard Guru | ⏳ In Progress | 50% |
| Dashboard Siswa | ⏳ In Progress | 50% |
| Frontend UI | ⏳ Planned | 0% |
| Mobile App | ⏳ Planned | 0% |

---

## ✅ Checklist Setup

- [ ] Clone repository
- [ ] Setup Python virtual environment
- [ ] Install dependencies
- [ ] Konfigurasi .env
- [ ] Inisialisasi database
- [ ] Jalankan server
- [ ] Akses http://localhost:8000/docs
- [ ] Test login dengan seed data
- [ ] Mulai development

---

**Last Updated**: 2026-01-26  
**Version**: 1.0.0  
**Status**: 🔄 Development Phase
