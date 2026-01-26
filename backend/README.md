# Backend - Journal Mengajar Online & Absensi Siswa

## 📌 Informasi Proyek

**Nama Aplikasi**: Journal Mengajar Online & Absensi Siswa  
**Institusi**: SMK Negeri 1 Lemahabang  
**Departemen**: Teknik Komputer dan Jaringan  
**Tingkat**: Kelas 10, 11, dan 12  
**Bahasa**: Python, Indonesian  
**Database**: Oracle 19c/21c  

---

## 🚀 Teknologi yang Digunakan

- **Framework**: FastAPI (Python)
- **Database**: Oracle Database 19c/21c
- **ORM**: SQLAlchemy 2.0
- **Authentication**: JWT (JSON Web Tokens)
- **API Documentation**: OpenAPI/Swagger
- **Web Server**: Uvicorn

---

## 📋 Fitur Utama

### 1. **Manajemen Pengguna (Authentication)**
- ✅ Registrasi user (Admin, Guru, Siswa)
- ✅ Login dengan JWT
- ✅ Password hashing dengan bcrypt
- ✅ Role-based access control (RBAC)
- ✅ Profile management

### 2. **Journal Mengajar (Teaching Journal)**
- ✅ Buat/edit/hapus journal harian
- ✅ Lampirkan KI/KD dan Modul Pembelajaran
- ✅ Rekam metode pembelajaran dan kegiatan
- ✅ Catat achievement dan challenges
- ✅ Submit dan verifikasi journal
- ✅ Filter dan search dengan tanggal range

### 3. **Absensi Siswa (Attendance)**
- ✅ Catat absensi per siswa
- ✅ Catat absensi massal (bulk)
- ✅ Status: Hadir, Sakit, Izin, Alfa, Libur
- ✅ Surat izin ketidakhadiran (dengan approval flow)
- ✅ Summary absensi per bulan
- ✅ Laporan attendance rate

### 4. **Kurikulum (Curriculum Management)**
- ✅ **KI/KD (Kompetensi Inti & Dasar)** - Kurikulum 2013
- ✅ **ATP (Alur Tujuan Pembelajaran)** - Kurikulum Merdeka
- ✅ **Modul Pembelajaran** - Structured learning modules
- ✅ **Pembelajaran Mendalam** - Deep learning programs
- ✅ Kelola untuk semua tingkat kelas (10, 11, 12)

### 5. **Dashboard**
- ✅ Dashboard Admin (statistik sistem)
- ✅ Dashboard Guru (ringkasan mengajar)
- ✅ Dashboard Siswa (absensi & informasi)
- ✅ Real-time data aggregation

---

## 🔧 Setup & Installation

### Prasyarat
- Python 3.8+
- Oracle Database 19c atau 21c
- pip (Python Package Manager)
- Git

### Langkah 1: Clone Repository
```bash
cd /workspaces
git clone <repository-url>
cd jurnalyabegitulahyangpentingbisa.github.io
```

### Langkah 2: Buat Virtual Environment
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# atau untuk Windows: venv\Scripts\activate
```

### Langkah 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Langkah 4: Setup Environment Variables
```bash
cp .env.example .env
# Edit .env dengan konfigurasi Oracle Anda
```

**Isi file .env:**
```env
# Oracle Database
ORACLE_USER=smk_admin
ORACLE_PASSWORD=your_password
ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SID=XE

# Security
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Server
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
DEBUG=True
```

### Langkah 5: Inisialisasi Database
```bash
# Buat semua tables
python scripts/init_database.py

# (Optional) Insert data awal
python scripts/seed_data.py
```

### Langkah 6: Jalankan Server
```bash
python run.py
# atau
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server akan berjalan di: **http://localhost:8000**

---

## 📚 Struktur Direktori

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point aplikasi
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── models.py           # User, Department, Class, Student models
│   │   ├── schemas.py          # Pydantic schemas untuk request/response
│   │   ├── crud.py             # Database operations
│   │   └── routes.py           # Authentication endpoints
│   ├── journal/
│   │   ├── __init__.py
│   │   ├── models.py           # TeachingJournal model
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── routes.py
│   ├── attendance/
│   │   ├── __init__.py
│   │   ├── models.py           # Attendance models
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── routes.py
│   ├── curriculum/
│   │   ├── __init__.py
│   │   ├── models.py           # KI/KD, ATP, Modul, Deep Learning models
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── routes.py
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── routes.py           # Dashboard endpoints
│   │   └── schemas.py
│   └── core/
│       ├── __init__.py
│       ├── config.py           # Konfigurasi aplikasi
│       ├── database.py         # Database setup
│       └── security.py         # Security utilities
│
├── scripts/
│   ├── init_database.py        # Setup database tables
│   └── seed_data.py            # Insert initial data
│
├── tests/
│   └── ...                     # Unit & integration tests
│
├── requirements.txt             # Python dependencies
├── .env.example                # Environment template
├── .gitignore
├── run.py                      # Application runner
└── README.md
```

---

## 📖 Dokumentasi API

Dokumentasi lengkap API tersedia di:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **File**: [docs/API_DOCUMENTATION.md](../docs/API_DOCUMENTATION.md)

### Contoh Request

#### Login
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=guru@smk.ac.id&password=guru123456"
```

#### Buat Journal
```bash
curl -X POST "http://localhost:8000/api/journal" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "class_id": 1,
    "date": "2024-01-20T08:00:00",
    "subject": "Sistem Bilangan Digital",
    "material_summary": "..."
  }'
```

---

## 🗄️ Model Database

### Tabel Utama
1. **users** - Data pengguna sistem
2. **departments** - Departemen/Jurusan
3. **classes** - Kelas/Rombongan Belajar
4. **students** - Data siswa
5. **kompetensi_inti** - KI (Kurikulum 2013)
6. **kompetensi_dasar** - KD (Kurikulum 2013)
7. **alur_tujuan_pembelajaran** - ATP (Kurikulum Merdeka)
8. **teaching_modules** - Modul Pembelajaran
9. **pembelajaran_mendalam** - Program Deep Learning
10. **teaching_journals** - Journal Mengajar
11. **attendance** - Absensi Siswa
12. **attendance_summary** - Ringkasan Absensi
13. **attendance_permits** - Surat Izin

Lihat [docs/DATABASE_DESIGN.md](../docs/DATABASE_DESIGN.md) untuk detail lengkap.

---

## 🔐 Security

### Implementasi Keamanan
- ✅ Password hashing dengan bcrypt
- ✅ JWT token untuk authentication
- ✅ Role-based access control (RBAC)
- ✅ CORS protection
- ✅ Rate limiting (planned)
- ✅ Input validation dengan Pydantic
- ✅ SQL injection protection (SQLAlchemy ORM)

### Role & Permissions

| Role | Akses |
|------|-------|
| **Admin** | Full akses, manajemen user, verifikasi journal |
| **Guru** | Buat/edit journal, catat absensi, lihat data siswa |
| **Siswa** | Lihat absensi sendiri, ajukan surat izin |
| **Kepala Sekolah** | View dashboard, verifikasi journal |

---

## 🧪 Testing

### Jalankan Tests
```bash
pip install pytest pytest-asyncio
pytest tests/
```

### Coverage
```bash
pytest --cov=app tests/
```

---

## 🐛 Troubleshooting

### Error: "ImportError: No module named 'cx_Oracle'"
```bash
pip install cx_Oracle
```

### Error: "Connection refused" pada Oracle
1. Pastikan Oracle Database sudah running
2. Cek konfigurasi di `.env`
3. Verifikasi username dan password
4. Gunakan SQL*Plus untuk test koneksi:
   ```bash
   sqlplus smk_admin/password@localhost:1521/XE
   ```

### Error: "Module not found"
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Database Errors
- Hapus file `.env` dan buat yang baru dari `.env.example`
- Drop all tables dan inisialisasi ulang: `python scripts/init_database.py`

---

## 📝 Development Guidelines

### Code Style
- Ikuti PEP 8
- Gunakan type hints
- Tambahkan docstrings

### Commit Message Format
```
feat: tambah endpoint journal mengajar
fix: perbaiki bug login
docs: update API documentation
style: format kode
refactor: refactor database module
test: tambah unit test untuk auth
```

### Branch Naming
```
feature/nama-fitur
bugfix/nama-bug
docs/nama-dokumentasi
```

---

## 📚 Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com
- **SQLAlchemy Documentation**: https://docs.sqlalchemy.org
- **Oracle Database**: https://www.oracle.com/database/
- **Python Documentation**: https://docs.python.org

---

## 👨‍💼 Tim Pengembang

**SMK Negeri 1 Lemahabang**  
Departemen Teknik Komputer dan Jaringan

---

## 📄 Lisensi

Proprietary - SMK Negeri 1 Lemahabang

---

## 📞 Support

Untuk pertanyaan atau laporan bug, hubungi tim IT SMK Negeri 1 Lemahabang.

---

**Last Updated**: 2026-01-26  
**Version**: 1.0.0  
**Status**: ✅ Development Phase
