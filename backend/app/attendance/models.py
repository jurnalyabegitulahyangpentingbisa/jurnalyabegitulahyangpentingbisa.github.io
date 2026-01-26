"""
Models untuk Attendance (Absensi Siswa)
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.core.database import Base


class AttendanceStatus(str, enum.Enum):
    """Enum untuk status kehadiran"""
    HADIR = "hadir"
    SAKIT = "sakit"
    IZIN = "izin"
    ALFA = "alfa"  # Absen tanpa keterangan
    LIBUR = "libur"


class Attendance(Base):
    """
    Model untuk Absensi Siswa
    Mencatat kehadiran siswa setiap hari
    """
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign keys
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False, index=True)
    
    # Attendance info
    date = Column(DateTime, nullable=False, index=True)
    status = Column(Enum(AttendanceStatus), default=AttendanceStatus.HADIR, nullable=False)
    notes = Column(String(500), nullable=True)  # Catatan tambahan (misal: izin sakit, dll)
    
    # Recorded by (guru atau admin)
    recorded_by = Column(Integer, nullable=True)  # User ID
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    student = relationship("Student", back_populates="attendance_records")
    class_ = relationship("Class")

    def __repr__(self):
        return f"<Attendance(student_id={self.student_id}, date={self.date}, status={self.status})>"


class AttendanceSummary(Base):
    """
    Model untuk Ringkasan Absensi
    Agregasi data absensi siswa per bulan
    """
    __tablename__ = "attendance_summary"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False, index=True)
    
    # Period
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)  # 1-12
    
    # Attendance counts
    hadir = Column(Integer, default=0)
    sakit = Column(Integer, default=0)
    izin = Column(Integer, default=0)
    alfa = Column(Integer, default=0)
    
    # Percentage
    attendance_percentage = Column(Integer, nullable=True)  # 0-100
    
    # Status
    is_finalized = Column(Boolean, default=False)
    finalized_at = Column(DateTime, nullable=True)
    finalized_by = Column(Integer, nullable=True)  # Admin/Guru
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    student = relationship("Student")

    def __repr__(self):
        return f"<AttendanceSummary(student_id={self.student_id}, {self.year}-{self.month})>"


class AttendancePermit(Base):
    """
    Model untuk Surat Izin Ketidakhadiran
    Sistem untuk memproses izin atau dispensasi ketidakhadiran
    """
    __tablename__ = "attendance_permits"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign keys
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    
    # Permit info
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    reason = Column(String(500), nullable=False)  # Alasan izin
    permit_type = Column(String(50), nullable=False)  # Sakit, Izin Orang Tua, Acara, dll
    
    # Supporting document
    document_path = Column(String(500), nullable=True)  # Path file surat izin
    document_filename = Column(String(255), nullable=True)
    
    # Approval
    status = Column(String(50), default="pending")  # pending, approved, rejected
    approved_by = Column(Integer, nullable=True)  # Guru/Admin yang approve
    approval_notes = Column(String(500), nullable=True)
    approved_at = Column(DateTime, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    submitted_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    student = relationship("Student")

    def __repr__(self):
        return f"<AttendancePermit(student_id={self.student_id}, status={self.status})>"
