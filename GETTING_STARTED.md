# 🎓 PANDUAN LENGKAP - MULAI DEVELOPMENT SEKARANG

## 📌 Aplikasi Journal Mengajar Online & Absensi Siswa
**SMK Negeri 1 Lemahabang - Teknik Komputer dan Jaringan**

---

## ⚡ Quick Start (5 Menit)

### 1️⃣ Clone & Navigate
```bash
cd /workspaces/jurnalyabegitulahyangpentingbisa.github.io
cd backend
```

### 2️⃣ Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# atau: venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database
```bash
cp .env.example .env
# Edit .env dengan credential Oracle Anda:
# ORACLE_USER, ORACLE_PASSWORD, ORACLE_HOST, ORACLE_PORT, ORACLE_SID
nano .env
```

### 5️⃣ Initialize Database
```bash
python scripts/init_database.py
python scripts/seed_data.py
```

### 6️⃣ Run Application
```bash
python run.py
```

**Access**:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 📚 File-File Penting (BACA INI DULU!)

Urutan baca yang disarankan:

1. **[README.md](README.md)** ⭐ START HERE
   - Overview aplikasi
   - Tech stack
   - Fitur utama
   - Quick start

2. **[PANDUAN_SETUP.md](PANDUAN_SETUP.md)** 📖 SETUP GUIDE
   - Persyaratan sistem
   - Langkah-langkah setup detail
   - Troubleshooting

3. **[docs/DATABASE_DESIGN.md](docs/DATABASE_DESIGN.md)** 🗄️ DATABASE
   - Schema design
   - 13 tabel dengan SQL
   - ERD diagram
   - Relationships

4. **[docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)** 🔌 API REFERENCE
   - 27+ endpoints yang direncanakan
   - Request/response examples
   - Error handling

5. **[docs/USER_GUIDE.md](docs/USER_GUIDE.md)** 👥 USER MANUAL
   - Panduan untuk Admin, Guru, Siswa
   - Step-by-step instructions
   - FAQ

6. **[ROADMAP.md](ROADMAP.md)** 🛣️ DEVELOPMENT PLAN
   - Implementation checklist
   - Timeline
   - Next steps

7. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** 📋 PROJECT OVERVIEW
   - Fitur yang sudah dikerjakan
   - Technology stack detail
   - Development statistics

---

## 🏗️ Project Structure (Simplified)

```
backend/
├── app/                        # Main application code
│   ├── auth/                  # User authentication
│   │   └── models.py          # User, Department, Class, Student
│   ├── journal/               # Journal mengajar
│   │   └── models.py          # TeachingJournal
│   ├── attendance/            # Absensi
│   │   └── models.py          # Attendance, Summary, Permits
│   ├── curriculum/            # Kurikulum (KI/KD, ATP, Modul)
│   │   └── models.py          # KI, KD, ATP, Module, DeepLearning
│   ├── dashboard/             # Dashboard
│   ├── core/                  # Core config & database
│   │   ├── config.py          # Settings
│   │   ├── database.py        # SQLAlchemy setup
│   │   └── security.py        # Password & JWT
│   └── main.py                # FastAPI app
├── scripts/
│   ├── init_database.py       # Setup database
│   └── seed_data.py           # Insert test data
├── requirements.txt           # Dependencies
├── .env.example               # Environment template
├── run.py                     # Start server
└── README.md                  # Backend docs
```

---

## 🔄 Development Workflow

### Phase 1: ✅ COMPLETE (Foundation)
```
✓ Database design
✓ Models implementation
✓ Security utilities
✓ Documentation
✓ Setup scripts
```

### Phase 2: ⏳ IN PROGRESS (API Implementation)
**Estimated**: 2-3 weeks

**Tasks**:
```
Priority 1 (Week 1-2):
□ Authentication routes
  ├─ POST /auth/register
  ├─ POST /auth/login
  ├─ GET /auth/me
  └─ POST /auth/change-password

□ Journal CRUD
  ├─ POST /journal
  ├─ GET /journal
  ├─ PUT /journal/{id}
  └─ DELETE /journal/{id}

□ Attendance Recording
  ├─ POST /attendance
  ├─ POST /attendance/bulk
  └─ GET /attendance/{student_id}

□ Dashboard
  ├─ GET /dashboard/admin/summary
  ├─ GET /dashboard/teacher/my-summary
  └─ GET /dashboard/student/my-summary
```

**How to Implement**:
```python
# 1. Create routes file
# app/auth/routes.py

from fastapi import APIRouter, Depends
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(email: str, password: str, db = Depends(get_db)):
    # Implementation here
    pass

# 2. Include in main.py
# app/main.py

from app.auth import routes as auth_routes
app.include_router(auth_routes.router, prefix="/api")

# 3. Test in Swagger UI
# http://localhost:8000/docs
```

### Phase 3: ⏳ PLANNED (Frontend)
**Estimated**: 4-5 weeks
- Admin dashboard UI
- Teacher dashboard UI
- Student dashboard UI

### Phase 4: ⏳ PLANNED (Testing & Deployment)
**Estimated**: 2-3 weeks
- Unit tests
- Integration tests
- Production deployment

---

## 💾 Database Quick Reference

### Login Test Data
```
Email: admin@smk.ac.id
Password: admin123456

Email: guru.tkj1@smk.ac.id
Password: guru123456

Email: siswa.001@smk.ac.id
Password: siswa123456
```

### Main Tables
```
users                          → User profiles
departments                    → Departemen (TKJ, TEL, TM)
classes                        → Kelas (X TKJ A, XI TKJ B, XII TKJ C)
students                       → Siswa
kompetensi_inti               → KI (Kurikulum 2013)
kompetensi_dasar              → KD (Kurikulum 2013)
alur_tujuan_pembelajaran      → ATP (Kurikulum Merdeka)
teaching_modules              → Modul Pembelajaran
pembelajaran_mendalam         → Deep Learning Programs
teaching_journals             → Journal Mengajar
attendance                    → Absensi Siswa
attendance_summary            → Summary Absensi
attendance_permits            → Surat Izin
```

---

## 🔧 Common Commands

```bash
# Virtual environment
source venv/bin/activate        # Activate (Linux/macOS)
venv\Scripts\activate           # Activate (Windows)
deactivate                      # Deactivate

# Database
python scripts/init_database.py # Setup tables
python scripts/seed_data.py     # Insert test data

# Server
python run.py                   # Run development server
python run.py --reload          # With auto-reload
python run.py --workers=4       # Multiple workers

# Package management
pip install -r requirements.txt # Install dependencies
pip freeze > requirements.txt   # Update requirements

# Testing
pytest tests/                   # Run tests
pytest --cov=app tests/         # With coverage
```

---

## 📖 API Endpoints Preview

### Authentication (6 endpoints)
```
POST   /api/auth/register              → Register user
POST   /api/auth/login                 → Login & get token
GET    /api/auth/me                    → Get profile
POST   /api/auth/change-password       → Change password
POST   /api/auth/logout                → Logout
GET    /api/auth/refresh               → Refresh token
```

### Journal (7 endpoints)
```
POST   /api/journal                    → Create journal
GET    /api/journal                    → List journals (filter/pagination)
GET    /api/journal/{id}               → Get detail
PUT    /api/journal/{id}               → Update journal
DELETE /api/journal/{id}               → Delete journal
POST   /api/journal/{id}/submit        → Submit for approval
POST   /api/journal/{id}/verify        → Verify (admin only)
```

### Attendance (9 endpoints)
```
POST   /api/attendance                 → Record attendance
POST   /api/attendance/bulk            → Bulk record
GET    /api/attendance/{student_id}    → Get history
GET    /api/attendance/class/{class_id} → Class summary
GET    /api/attendance/summary         → Monthly summary
POST   /api/attendance/permits         → Submit permit
GET    /api/attendance/permits         → List permits
POST   /api/attendance/permits/{id}/approve → Approve
POST   /api/attendance/permits/{id}/reject  → Reject
```

### Curriculum (4 endpoints)
```
GET    /api/curriculum/ki-kd           → Get KI/KD
GET    /api/curriculum/atp             → Get ATP
GET    /api/curriculum/modules         → Get modules
GET    /api/curriculum/deep-learning   → Get deep learning
```

### Dashboard (3 endpoints)
```
GET    /api/dashboard/admin/summary
GET    /api/dashboard/teacher/my-summary
GET    /api/dashboard/student/my-summary
```

**Total**: 27+ endpoints

---

## 🐛 Troubleshooting

### Error: "No module named 'cx_Oracle'"
```bash
pip install cx_Oracle
```

### Error: "Connection refused" (Database)
```bash
# Check Oracle is running
# Verify .env settings
# Test connection: sqlplus user@host:port/sid
```

### Error: "ModuleNotFoundError"
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Database already exists
```bash
# Option 1: Drop all tables (careful!)
# In script: Base.metadata.drop_all(bind=engine)

# Option 2: Use different ORACLE_SID in .env
```

---

## 🎯 Development Tips

### 1. **Code Organization**
```
Keep models in models.py
Keep schemas in schemas.py
Keep CRUD in crud.py
Keep routes in routes.py
```

### 2. **Database Session**
```python
# Use dependency injection
async def get_data(db = Depends(get_db)):
    data = db.query(Model).all()
    return data
```

### 3. **Error Handling**
```python
# Always handle errors gracefully
try:
    result = db.query(Model).first()
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
```

### 4. **Pagination**
```python
# Implement pagination for list endpoints
skip = 0
limit = 10
items = db.query(Model).skip(skip).limit(limit).all()
```

### 5. **Testing**
```bash
# Use Swagger UI to test endpoints
# http://localhost:8000/docs

# Or use curl
curl -X POST http://localhost:8000/api/auth/login \
  -d "email=admin@smk.ac.id&password=admin123456"
```

---

## 📞 Need Help?

### Documentation Files
- **Setup Issues**: See PANDUAN_SETUP.md
- **Database Questions**: See docs/DATABASE_DESIGN.md
- **API Usage**: See docs/API_DOCUMENTATION.md
- **User Guide**: See docs/USER_GUIDE.md
- **Planning**: See ROADMAP.md

### Quick Links
```
FastAPI Docs: https://fastapi.tiangolo.com
SQLAlchemy Docs: https://docs.sqlalchemy.org
Oracle Docs: https://docs.oracle.com
Python Docs: https://docs.python.org
```

### Contact
```
Email: it@smk1lemahabang.sch.id
School: SMK Negeri 1 Lemahabang
Department: Teknik Komputer dan Jaringan
```

---

## 🎉 Ready to Start?

```bash
# 1. Get setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Configure database
cp .env.example .env
# Edit .env with your Oracle credentials

# 3. Initialize
python scripts/init_database.py
python scripts/seed_data.py

# 4. Run
python run.py

# 5. Access
# Open browser to http://localhost:8000/docs
```

**That's it! You're ready to start development! 🚀**

---

## ✅ Completion Checklist

- [ ] Read README.md
- [ ] Read PANDUAN_SETUP.md
- [ ] Setup virtual environment
- [ ] Install dependencies
- [ ] Configure .env
- [ ] Run init_database.py
- [ ] Run seed_data.py
- [ ] Run application
- [ ] Access http://localhost:8000/docs
- [ ] Test login with default credentials
- [ ] Review database schema
- [ ] Review API documentation
- [ ] Start Phase 2 implementation

---

**Version**: 1.0.0  
**Status**: ✅ Ready for Development  
**Last Updated**: 26 Januari 2026  

Welcome to your new Journal Mengajar Online & Absensi Siswa application!
