"""
Script untuk inisialisasi database
Jalankan ini sekali di awal untuk membuat semua tables
"""

import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import init_db, engine, SessionLocal, Base
from app.core.config import settings

# Import all models to register them
from app.auth.models import User, Department, Class, Student, UserRole
from app.curriculum.models import (
    KompetensiInti,
    KompetensiDasar,
    AturanTujuanPembelajaran,
    TeachingModule,
    PembelajaranMendalam,
)
from app.journal.models import TeachingJournal
from app.attendance.models import Attendance, AttendanceSummary, AttendancePermit


def init_database():
    """Initialize database - create all tables"""
    print("=" * 60)
    print("🔧 Database Initialization Script")
    print("=" * 60)
    print(f"📍 Database: Oracle")
    print(f"🔗 Connection: {settings.ORACLE_USER}@{settings.ORACLE_HOST}")
    print("=" * 60)

    try:
        print("✋ Checking if tables already exist...")
        # Check if tables exist
        inspector_results = engine.dialect.get_table_names(
            connection=engine.connect()
        )

        if inspector_results:
            print(
                f"⚠️  Found {len(inspector_results)} existing tables:"
            )
            for table in inspector_results:
                print(f"   - {table}")
            response = input("\n❓ Drop all existing tables? (yes/no): ").strip().lower()
            if response == "yes":
                print("🗑️  Dropping existing tables...")
                Base.metadata.drop_all(bind=engine)
                print("✅ Tables dropped")
            else:
                print("⏭️  Skipping table creation")
                return

        print("\n🚀 Creating database tables...")
        init_db()
        print("✅ Database tables created successfully!")

        print("\n" + "=" * 60)
        print("📋 Tables created:")
        tables = [
            "users",
            "departments",
            "classes",
            "students",
            "kompetensi_inti",
            "kompetensi_dasar",
            "alur_tujuan_pembelajaran",
            "teaching_modules",
            "pembelajaran_mendalam",
            "teaching_journals",
            "attendance",
            "attendance_summary",
            "attendance_permits",
        ]
        for table in tables:
            print(f"   ✓ {table}")

        print("=" * 60)
        print("✅ Database initialization completed successfully!")
        print("\nNext steps:")
        print("1. Run 'python scripts/seed_data.py' to insert initial data")
        print("2. Start the application with 'python run.py'")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error during database initialization:")
        print(f"   {type(e).__name__}: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Check Oracle Database is running")
        print("2. Verify credentials in .env file")
        print("3. Verify network connectivity to Oracle server")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    init_database()
