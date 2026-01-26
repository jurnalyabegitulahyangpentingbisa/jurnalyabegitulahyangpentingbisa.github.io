#!/bin/bash

# ============================================================
# Quick Start Checklist - Journal Mengajar & Absensi Siswa
# ============================================================

echo "📋 QUICK START CHECKLIST"
echo "=================================================="
echo ""

# 1. Prerequisites
echo "✅ STEP 1: Verifikasi Prasyarat"
echo "   Pastikan sudah terinstall:"
echo "   ☐ Python 3.8+ → $(python3 --version)"
echo "   ☐ Git → $(git --version)"
echo "   ☐ Oracle Database (running)"
echo ""
read -p "Lanjut? (y/n): " -n 1 -r && echo ""

# 2. Clone repo
echo "✅ STEP 2: Clone Repository"
echo "   Command: git clone <repo-url>"
echo "   Then: cd jurnalyabegitulahyangpentingbisa.github.io"
echo ""
read -p "Sudah clone? (y/n): " -n 1 -r && echo ""

# 3. Backend setup
echo "✅ STEP 3: Setup Backend"
echo "   cd backend"
echo "   python3 -m venv venv"
echo "   source venv/bin/activate"
echo "   pip install -r requirements.txt"
echo ""
read -p "Sudah setup backend? (y/n): " -n 1 -r && echo ""

# 4. Environment config
echo "✅ STEP 4: Konfigurasi Environment"
echo "   cp .env.example .env"
echo "   Edit .env dengan credential Oracle Anda"
echo ""
read -p "Sudah konfigurasi .env? (y/n): " -n 1 -r && echo ""

# 5. Database init
echo "✅ STEP 5: Inisialisasi Database"
echo "   python scripts/init_database.py"
echo "   python scripts/seed_data.py (optional)"
echo ""
read -p "Sudah inisialisasi database? (y/n): " -n 1 -r && echo ""

# 6. Run server
echo "✅ STEP 6: Jalankan Server"
echo "   python run.py"
echo "   atau: uvicorn app.main:app --reload"
echo ""
echo "   Server akan berjalan di: http://localhost:8000"
echo ""
read -p "Sudah menjalankan server? (y/n): " -n 1 -r && echo ""

# Final
echo ""
echo "=================================================="
echo "🎉 SELAMAT! Aplikasi sudah siap digunakan!"
echo "=================================================="
echo ""
echo "📍 AKSES APLIKASI:"
echo "   • API: http://localhost:8000"
echo "   • Swagger UI: http://localhost:8000/docs"
echo "   • ReDoc: http://localhost:8000/redoc"
echo ""
echo "🔓 LOGIN DEFAULT:"
echo "   • Email: admin@smk.ac.id"
echo "   • Password: admin123456"
echo ""
echo "📚 DOKUMENTASI PENTING:"
echo "   • ./PANDUAN_SETUP.md - Panduan setup lengkap"
echo "   • ./docs/DATABASE_DESIGN.md - Schema database"
echo "   • ./docs/API_DOCUMENTATION.md - API reference"
echo "   • ./docs/USER_GUIDE.md - Panduan pengguna"
echo "   • ./ROADMAP.md - Rencana development"
echo ""
echo "🆘 BANTUAN:"
echo "   • Lihat troubleshooting di PANDUAN_SETUP.md"
echo "   • Email: it@smk1lemahabang.sch.id"
echo ""
echo "=================================================="
