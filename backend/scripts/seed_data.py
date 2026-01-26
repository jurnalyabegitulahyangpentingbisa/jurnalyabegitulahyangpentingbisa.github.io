"""
Script untuk seed data awal ke database
Jalankan ini setelah init_database.py untuk mengisi data contoh
"""

import sys
import os
from datetime import datetime, timedelta
from passlib.context import CryptContext

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal
from app.auth.models import User, Department, Class, Student, UserRole
from app.curriculum.models import (
    KompetensiInti,
    KompetensiDasar,
    AturanTujuanPembelajaran,
    TeachingModule,
)
from app.attendance.models import Attendance, AttendanceStatus

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash password"""
    return pwd_context.hash(password)


def seed_departments(db):
    """Seed departemen data"""
    print("📚 Seeding departments...")
    departments = [
        Department(
            name="Teknik Komputer dan Jaringan",
            code="TKJ",
            description="Departemen untuk program keahlian Teknik Komputer dan Jaringan",
        ),
        Department(
            name="Teknik Elektronika",
            code="TEL",
            description="Departemen untuk program keahlian Teknik Elektronika",
        ),
        Department(
            name="Teknik Mesin",
            code="TM",
            description="Departemen untuk program keahlian Teknik Mesin",
        ),
    ]
    for dept in departments:
        existing = db.query(Department).filter_by(code=dept.code).first()
        if not existing:
            db.add(dept)
            print(f"   ✓ {dept.name}")
    db.commit()


def seed_users(db):
    """Seed user data"""
    print("👥 Seeding users...")

    users = [
        # Admin
        User(
            email="admin@smk.ac.id",
            username="admin",
            full_name="Administrator",
            hashed_password=hash_password("admin123456"),
            role=UserRole.ADMIN,
            is_active=True,
            is_verified=True,
        ),
        # Kepala Sekolah
        User(
            email="kepala@smk.ac.id",
            username="kepala",
            full_name="Dr. H. Kepala Sekolah, S.Pd., M.Pd.",
            hashed_password=hash_password("kepala123456"),
            role=UserRole.KEPALA_SEKOLAH,
            nip="195801011982031001",
            is_active=True,
            is_verified=True,
        ),
        # Guru TKJ
        User(
            email="guru.tkj1@smk.ac.id",
            username="guru_tkj_1",
            full_name="Budi Santoso, S.Kom.",
            hashed_password=hash_password("guru123456"),
            role=UserRole.GURU,
            nip="198505151010011001",
            phone="082123456789",
            is_active=True,
            is_verified=True,
        ),
        User(
            email="guru.tkj2@smk.ac.id",
            username="guru_tkj_2",
            full_name="Siti Nurhaliza, S.Kom.",
            hashed_password=hash_password("guru123456"),
            role=UserRole.GURU,
            nip="198702201010011002",
            phone="082234567890",
            is_active=True,
            is_verified=True,
        ),
        # Siswa
        User(
            email="siswa.001@smk.ac.id",
            username="siswa_001",
            full_name="Ahmad Hidayat",
            hashed_password=hash_password("siswa123456"),
            role=UserRole.SISWA,
            nis="001/2024",
            is_active=True,
            is_verified=True,
        ),
        User(
            email="siswa.002@smk.ac.id",
            username="siswa_002",
            full_name="Dewi Lestari",
            hashed_password=hash_password("siswa123456"),
            role=UserRole.SISWA,
            nis="002/2024",
            is_active=True,
            is_verified=True,
        ),
        User(
            email="siswa.003@smk.ac.id",
            username="siswa_003",
            full_name="Ricky Gunawan",
            hashed_password=hash_password("siswa123456"),
            role=UserRole.SISWA,
            nis="003/2024",
            is_active=True,
            is_verified=True,
        ),
    ]

    for user in users:
        existing = db.query(User).filter_by(email=user.email).first()
        if not existing:
            db.add(user)
            print(f"   ✓ {user.full_name} ({user.role.value})")
    db.commit()


def seed_classes(db):
    """Seed class data"""
    print("🏫 Seeding classes...")

    dept = db.query(Department).filter_by(code="TKJ").first()
    guru = db.query(User).filter_by(username="guru_tkj_1").first()

    classes = [
        Class(
            name="X TKJ A",
            grade=10,
            department_id=dept.id if dept else None,
            homeroom_teacher_id=guru.id if guru else None,
            is_active=True,
        ),
        Class(
            name="XI TKJ A",
            grade=11,
            department_id=dept.id if dept else None,
            is_active=True,
        ),
        Class(
            name="XII TKJ A",
            grade=12,
            department_id=dept.id if dept else None,
            is_active=True,
        ),
    ]

    for cls in classes:
        existing = db.query(Class).filter_by(name=cls.name).first()
        if not existing:
            db.add(cls)
            print(f"   ✓ {cls.name}")
    db.commit()


def seed_students(db):
    """Seed student data"""
    print("🎓 Seeding students...")

    cls = db.query(Class).filter_by(name="X TKJ A").first()
    users = db.query(User).filter(User.username.in_(["siswa_001", "siswa_002", "siswa_003"])).all()

    for idx, user in enumerate(users, 1):
        existing = db.query(Student).filter_by(user_id=user.id).first()
        if not existing and cls:
            student = Student(
                user_id=user.id,
                nis=user.nis,
                class_id=cls.id,
            )
            db.add(student)
            print(f"   ✓ {user.full_name} (NIS: {user.nis})")
    db.commit()


def seed_ki_kd(db):
    """Seed KI/KD data"""
    print("📖 Seeding KI/KD (Kurikulum 2013)...")

    # KI Kelas X
    ki_1 = KompetensiInti(
        grade=10,
        ki_number=1,
        description="Menghayati dan mengamalkan ajaran agama yang dianut",
    )
    ki_3 = KompetensiInti(
        grade=10,
        ki_number=3,
        description="Memahami, menerapkan, dan menganalisis pengetahuan faktual, konseptual, prosedural, dan metakognitif berdasarkan rasa ingin tahunya tentang ilmu pengetahuan, teknologi, seni, budaya, dan humaniora dengan wawasan kemanusiaan, kebangsaan, kenegaraan, dan peradaban terkait penyebab fenomena dan kejadian, serta menerapkan pengetahuan prosedural pada bidang kajian yang spesifik sesuai dengan bakat dan minatnya untuk memecahkan masalah",
    )

    db.add(ki_1)
    db.add(ki_3)
    db.commit()

    # KD untuk KI 3
    kd_data = [
        KompetensiDasar(
            ki_id=ki_3.id,
            kd_number="3.1",
            description="Menjelaskan konsep dasar sistem bilangan digital",
            learning_indicators="Siswa dapat menjelaskan sistem bilangan biner, oktal, desimal, heksadesimal dan konversi antar sistem bilangan",
        ),
        KompetensiDasar(
            ki_id=ki_3.id,
            kd_number="3.2",
            description="Menganalisis gerbang logika digital",
            learning_indicators="Siswa dapat menganalisis fungsi gerbang logika AND, OR, NOT, NAND, NOR, XOR, XNOR dan tabel kebenarannya",
        ),
        KompetensiDasar(
            ki_id=ki_3.id,
            kd_number="3.3",
            description="Menerapkan rangkaian kombinasional dan sekuensial",
            learning_indicators="Siswa dapat merancang dan menganalisis rangkaian kombinasional dan sekuensial",
        ),
    ]

    for kd in kd_data:
        existing = db.query(KompetensiDasar).filter_by(kd_number=kd.kd_number).first()
        if not existing:
            db.add(kd)
            print(f"   ✓ KD {kd.kd_number}: {kd.description}")
    db.commit()


def seed_atp(db):
    """Seed ATP data (Kurikulum Merdeka)"""
    print("🎯 Seeding ATP (Kurikulum Merdeka)...")

    atp_data = [
        AturanTujuanPembelajaran(
            grade=10,
            fase="D",
            subject_code="TKOM101",
            subject_name="Sistem Bilangan Digital",
            learning_objectives="Peserta didik dapat memahami dan menerapkan konsep sistem bilangan digital dalam konteks teknik komputer",
            content_description="Konversi bilangan, operasi aritmatika biner, representasi data",
            duration_weeks=4,
            is_active=True,
        ),
        AturanTujuanPembelajaran(
            grade=10,
            fase="D",
            subject_code="TKOM102",
            subject_name="Gerbang Logika Digital",
            learning_objectives="Peserta didik dapat memahami fungsi gerbang logika dan menerapkannya dalam rangkaian digital",
            content_description="Gerbang logika dasar, tabel kebenaran, aljabar boolean",
            duration_weeks=4,
            is_active=True,
        ),
    ]

    for atp in atp_data:
        existing = db.query(AturanTujuanPembelajaran).filter_by(subject_code=atp.subject_code).first()
        if not existing:
            db.add(atp)
            print(f"   ✓ {atp.subject_name}")
    db.commit()


def seed_teaching_modules(db):
    """Seed teaching modules"""
    print("📚 Seeding teaching modules...")

    atp = db.query(AturanTujuanPembelajaran).filter_by(subject_code="TKOM101").first()

    modules = [
        TeachingModule(
            atp_id=atp.id if atp else None,
            module_number="Modul 1",
            title="Pengenalan Sistem Bilangan",
            description="Modul pembelajaran dasar tentang sistem bilangan digital",
            learning_outcomes="Peserta didik mampu memahami dan mengkonversi berbagai sistem bilangan",
            key_concepts="Bilangan biner, oktal, desimal, heksadesimal",
            learning_activities="Diskusi, praktik konversi, studi kasus",
            assessment_method="Kuis, penugasan, praktik",
            duration_hours=8,
            difficulty_level="Mudah",
            is_active=True,
        ),
    ]

    for module in modules:
        existing = db.query(TeachingModule).filter_by(module_number=module.module_number).first()
        if not existing:
            db.add(module)
            print(f"   ✓ {module.title}")
    db.commit()


def seed_attendance(db):
    """Seed attendance data"""
    print("📋 Seeding attendance records...")

    students = db.query(Student).all()
    today = datetime.now().date()

    attendance_records = []
    for student in students:
        for day_offset in range(1, 21):  # 20 hari terakhir
            date = today - timedelta(days=day_offset)
            # 80% hadir, 10% sakit, 10% izin
            import random

            status_choice = random.choices(
                [
                    AttendanceStatus.HADIR,
                    AttendanceStatus.SAKIT,
                    AttendanceStatus.IZIN,
                ],
                weights=[0.8, 0.1, 0.1],
            )[0]

            attendance_records.append(
                Attendance(
                    student_id=student.id,
                    class_id=student.class_id,
                    date=datetime.combine(date, datetime.min.time()),
                    status=status_choice,
                )
            )

    for record in attendance_records:
        db.add(record)

    db.commit()
    print(f"   ✓ {len(attendance_records)} attendance records created")


def main():
    """Main seed function"""
    print("=" * 60)
    print("🌱 Database Seed Script")
    print("=" * 60)

    db = SessionLocal()

    try:
        seed_departments(db)
        seed_users(db)
        seed_classes(db)
        seed_students(db)
        seed_ki_kd(db)
        seed_atp(db)
        seed_teaching_modules(db)
        seed_attendance(db)

        print("\n" + "=" * 60)
        print("✅ Database seeding completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error during seeding: {str(e)}")
        db.rollback()
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    main()
