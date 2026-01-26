#!/bin/bash

# ============================================================
# Panduan Cepat Setup - Journal Mengajar & Absensi Siswa
# SMK Negeri 1 Lemahabang
# ============================================================

echo "🚀 Memulai Setup Aplikasi..."
echo "=================================================="

# 1. Clone/Navigate to project
echo "📁 Step 1: Navigasi ke direktori project"
cd backend
echo "✅ Berhasil masuk ke direktori backend"

# 2. Create virtual environment
echo ""
echo "🐍 Step 2: Membuat Python Virtual Environment"
python3 -m venv venv
source venv/bin/activate
echo "✅ Virtual environment berhasil dibuat dan diaktifkan"

# 3. Install dependencies
echo ""
echo "📦 Step 3: Install Python Dependencies"
pip install -r requirements.txt
echo "✅ Dependencies berhasil diinstall"

# 4. Setup environment
echo ""
echo "⚙️ Step 4: Setup Environment Configuration"
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  File .env telah dibuat dari template"
    echo "📝 SILAKAN EDIT .env dengan konfigurasi Oracle Anda:"
    echo "   - ORACLE_USER"
    echo "   - ORACLE_PASSWORD"
    echo "   - ORACLE_HOST"
    echo "   - ORACLE_PORT"
    echo "   - ORACLE_SID"
    read -p "Tekan ENTER setelah selesai mengedit .env..."
else
    echo "✅ File .env sudah ada"
fi

# 5. Initialize database
echo ""
echo "🗄️  Step 5: Inisialisasi Database"
echo "📌 Membuat semua database tables..."
python scripts/init_database.py

read -p "Seed data awal? (y/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📌 Menambahkan data awal..."
    python scripts/seed_data.py
    echo "✅ Data awal berhasil ditambahkan"
else
    echo "⏭️  Skip seeding data"
fi

# 6. Ready to run
echo ""
echo "=================================================="
echo "✅ SETUP SELESAI!"
echo "=================================================="
echo ""
echo "🎯 LANGKAH BERIKUTNYA:"
echo "1. Jalankan server:"
echo "   python run.py"
echo ""
echo "2. Akses aplikasi:"
echo "   - API: http://localhost:8000"
echo "   - Swagger Docs: http://localhost:8000/docs"
echo "   - ReDoc: http://localhost:8000/redoc"
echo ""
echo "3. Login dengan default credentials:"
echo "   - Email: admin@smk.ac.id"
echo "   - Password: admin123456"
echo ""
echo "📚 DOKUMENTASI:"
echo "   - Setup: ../PANDUAN_SETUP.md"
echo "   - Database: ../docs/DATABASE_DESIGN.md"
echo "   - API: ../docs/API_DOCUMENTATION.md"
echo "   - User Guide: ../docs/USER_GUIDE.md"
echo "   - Roadmap: ../ROADMAP.md"
echo ""
echo "=================================================="
