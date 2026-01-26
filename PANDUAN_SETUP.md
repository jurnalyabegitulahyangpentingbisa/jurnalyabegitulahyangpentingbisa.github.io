# Panduan Setup - Aplikasi Journal Mengajar Online & Absensi Siswa
## SMK Negeri 1 Lemahabang - Departemen Teknik Komputer dan Jaringan

---

## 📋 Daftar Isi
1. [Persyaratan Sistem](#persyaratan-sistem)
2. [Arsitektur Aplikasi](#arsitektur-aplikasi)
3. [Langkah-Langkah Setup](#langkah-langkah-setup)
4. [Struktur Database](#struktur-database)
5. [Panduan Pengembangan](#panduan-pengembangan)

---

## 🖥️ Persyaratan Sistem

### Software yang Diperlukan:
- **Python 3.8+** - Backend development
- **Oracle Database 19c atau 21c** - Database management system
- **Git** - Version control
- **Virtual Environment** - Python environment isolation
- **pip** - Python package manager

### Tools Tambahan:
- **Oracle SQL Developer** - Database management
- **Postman** - API testing
- **VS Code atau PyCharm** - Code editor

---

## 🏗️ Arsitektur Aplikasi

### Tech Stack yang Direkomendasikan:
```
┌─────────────────────────────────────────────┐
│         Frontend (HTML/CSS/JavaScript)      │
│     Dashboard Admin & Dashboard Guru        │
└──────────────────┬──────────────────────────┘
                   │ REST API
┌──────────────────▼──────────────────────────┐
│    Backend (Python FastAPI/Flask)           │
│  - Authentication & Authorization           │
│  - Business Logic                           │
│  - API Endpoints                            │
└──────────────────┬──────────────────────────┘
                   │ SQL
┌──────────────────▼──────────────────────────┐
│      Oracle Database 19c/21c                │
│  - Master Data (KI/KD, ATP, Modul)         │
│  - Transaksi (Journal, Absensi)            │
│  - User Management                         │
└─────────────────────────────────────────────┘
```

### Alasan Pemilihan Stack:

| Komponen | Pilihan | Alasan |
|----------|---------|--------|
| Backend | FastAPI | Performa tinggi, built-in async, dokumentasi auto (Swagger) |
| Database | Oracle | Skalabilitas, keandalan, support enterprise |
| ORM | SQLAlchemy | Support Oracle, fleksibel, production-ready |
| Auth | JWT | Stateless, scalable, standard industry |

---

## 📦 Langkah-Langkah Setup

### Step 1: Persiapan Awal

#### 1.1 Clone Repository
```bash
cd /path/to/project
git clone <repository-url>
cd jurnalyabegitulahyangpentingbisa.github.io
```

#### 1.2 Buat Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# atau untuk Windows:
# venv\Scripts\activate
```

#### 1.3 Upgrade pip
```bash
pip install --upgrade pip setuptools wheel
```

### Step 2: Instalasi Dependencies Python

#### 2.1 Buat file requirements.txt
```
FastAPI==0.104.1
uvicorn==0.24.0
SQLAlchemy==2.0.23
cx_Oracle==8.3.0
python-dotenv==1.0.0
pydantic==2.4.2
pydantic-settings==2.0.3
python-multipart==0.0.6
PyJWT==2.8.1
bcrypt==4.1.1
python-jose==3.3.0
email-validator==2.1.0
cors==1.0.1
```

#### 2.2 Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Konfigurasi Database Oracle

#### 3.1 Setup Koneksi Database

**File: `config/database.py`**

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Konfigurasi Oracle Database
ORACLE_USER = os.getenv('ORACLE_USER', 'system')
ORACLE_PASSWORD = os.getenv('ORACLE_PASSWORD', 'password')
ORACLE_HOST = os.getenv('ORACLE_HOST', 'localhost')
ORACLE_PORT = os.getenv('ORACLE_PORT', '1521')
ORACLE_SID = os.getenv('ORACLE_SID', 'XE')

# Connection String untuk Oracle
DATABASE_URL = f"oracle+cx_oracle://{ORACLE_USER}:{ORACLE_PASSWORD}@{ORACLE_HOST}:{ORACLE_PORT}/{ORACLE_SID}"

# Create Engine
engine = create_engine(DATABASE_URL, echo=True)

# Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### 3.2 Buat File .env

**File: `.env`**

```
# Oracle Database Configuration
ORACLE_USER=smk_admin
ORACLE_PASSWORD=your_secure_password_here
ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SID=XE

# App Configuration
SECRET_KEY=your_super_secret_key_change_this_in_production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Server
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
DEBUG=True
```

### Step 4: Struktur Direktori Proyek

```
jurnalyabegitulahyangpentingbisa.github.io/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # Entry point aplikasi
│   │   ├── config.py               # Konfigurasi aplikasi
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── models.py           # Model User, Role
│   │   │   ├── schemas.py          # Pydantic schemas
│   │   │   ├── crud.py             # Database operations
│   │   │   └── routes.py           # Auth endpoints
│   │   ├── journal/
│   │   │   ├── __init__.py
│   │   │   ├── models.py           # Model Journal Mengajar
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   └── routes.py
│   │   ├── attendance/
│   │   │   ├── __init__.py
│   │   │   ├── models.py           # Model Absensi
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   └── routes.py
│   │   ├── curriculum/
│   │   │   ├── __init__.py
│   │   │   ├── models.py           # KI/KD, ATP, Modul
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   └── routes.py
│   │   ├── dashboard/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # Dashboard endpoints
│   │   │   └── schemas.py
│   │   ├── database.py             # Database configuration
│   │   └── dependencies.py         # Dependency injection
│   ├── requirements.txt
│   ├── .env
│   ├── .env.example
│   └── run.py                      # Script untuk menjalankan server
│
├── frontend/
│   ├── index.html
│   ├── dashboard-admin.html
│   ├── dashboard-guru.html
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   ├── app.js
│   │   ├── auth.js
│   │   └── api.js
│   └── assets/
│
├── docs/
│   ├── DATABASE_DESIGN.md
│   ├── API_DOCUMENTATION.md
│   └── USER_GUIDE.md
│
├── scripts/
│   ├── init_database.py            # Setup database tables
│   └── seed_data.py                # Insert data awal
│
├── .gitignore
├── README.md
└── PANDUAN_SETUP.md (file ini)
```

### Step 5: Jalankan Aplikasi

```bash
# Pastikan virtual environment aktif
source venv/bin/activate

# Jalankan server
python run.py

# atau dengan uvicorn langsung:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server akan berjalan di: `http://localhost:8000`
Dokumentasi API (Swagger): `http://localhost:8000/docs`

---

## 📊 Struktur Database

### Tabel Master Data

#### 1. Users (Pengguna)
- ID, Email, Password (Hashed), Nama, Role (Admin/Guru/Siswa)
- Aktif/Non-aktif, Created_at, Updated_at

#### 2. KI_KD (Kompetensi Inti & Kompetensi Dasar - Kurikulum 13)
- ID, Kelas, KI, KD, Deskripsi, Created_at

#### 3. ATP (Alur Tujuan Pembelajaran - Kurikulum Merdeka)
- ID, Kelas, Fase, ATP_Content, Created_at

#### 4. Teaching_Modules (Modul Pembelajaran)
- ID, Nama_Modul, Deskripsi, File_Path, Created_at

#### 5. Classes (Kelas)
- ID, Nama_Kelas, Tingkat (10/11/12), Jurusan, Created_at

#### 6. Students (Siswa)
- ID, NIS, Nama, Kelas_ID, Email, Created_at

### Tabel Transaksi

#### 7. Teaching_Journal (Journal Mengajar)
- ID, Guru_ID, Kelas_ID, Tanggal, KI_KD_ID, Materi, Metode, File_Attach
- Catatan, Created_at, Updated_at

#### 8. Attendance (Absensi)
- ID, Siswa_ID, Tanggal, Status (Hadir/Sakit/Izin/Alfa), Catatan
- Created_at, Updated_at

#### 9. Attendance_Summary (Ringkasan Absensi)
- ID, Siswa_ID, Bulan, Tahun, Hadir, Sakit, Izin, Alfa

---

## 🚀 Panduan Pengembangan

### Best Practices:

1. **Version Control**: Commit secara teratur dengan pesan yang jelas
   ```bash
   git add .
   git commit -m "feat: tambah endpoint journal mengajar"
   git push origin main
   ```

2. **API Development**: Ikuti RESTful conventions
   - GET `/api/journal` - List journals
   - POST `/api/journal` - Create journal
   - GET `/api/journal/{id}` - Get detail
   - PUT `/api/journal/{id}` - Update
   - DELETE `/api/journal/{id}` - Delete

3. **Error Handling**: Return proper HTTP status codes
   - 200: OK
   - 201: Created
   - 400: Bad Request
   - 401: Unauthorized
   - 404: Not Found
   - 500: Server Error

4. **Testing**: Gunakan Postman atau pytest
   ```bash
   pip install pytest pytest-asyncio
   pytest tests/
   ```

5. **Documentation**: Update docs saat ada perubahan API

---

## 📝 Checklist Setup

- [ ] Install Python 3.8+
- [ ] Setup Oracle Database
- [ ] Clone repository
- [ ] Buat virtual environment
- [ ] Install dependencies (pip install -r requirements.txt)
- [ ] Konfigurasi .env file
- [ ] Setup database schema
- [ ] Test koneksi database
- [ ] Jalankan aplikasi
- [ ] Akses http://localhost:8000/docs
- [ ] Mulai development

---

## ❓ Troubleshooting

### Error: "ImportError: No module named 'cx_Oracle'"
```bash
pip install cx_Oracle
```

### Error: "Connection refused" pada Oracle
- Pastikan Oracle Database sudah running
- Cek konfigurasi di file `.env`
- Verifikasi username dan password

### Error: "Module not found"
```bash
pip install -r requirements.txt
source venv/bin/activate
```

---

## 📞 Support & Dokumentasi Tambahan

- FastAPI Docs: https://fastapi.tiangolo.com
- SQLAlchemy Docs: https://docs.sqlalchemy.org
- Oracle Database: https://www.oracle.com/database/

---

**Last Updated**: 2026-01-26
**Version**: 1.0.0
