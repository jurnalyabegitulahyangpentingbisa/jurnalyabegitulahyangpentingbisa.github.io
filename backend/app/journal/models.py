"""
Models untuk Teaching Journal (Journal Mengajar)
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class TeachingJournal(Base):
    """
    Model untuk Journal Mengajar
    Guru mencatat rincian mengajar setiap hari
    """
    __tablename__ = "teaching_journals"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign keys
    teacher_id = Column(Integer, nullable=False)  # User ID guru
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    kd_id = Column(Integer, ForeignKey("kompetensi_dasar.id"), nullable=True)
    module_id = Column(Integer, ForeignKey("teaching_modules.id"), nullable=True)
    
    # Basic info
    date = Column(DateTime, nullable=False, index=True)
    subject = Column(String(255), nullable=False)
    
    # Content detail
    material_summary = Column(Text, nullable=False)  # Ringkasan materi yang diajarkan
    learning_method = Column(String(255), nullable=True)  # Metode pembelajaran (Ceramah, Diskusi, Praktik, dll)
    learning_activities = Column(Text, nullable=True)  # Aktivitas pembelajaran detail
    
    # Student engagement
    student_attendance = Column(Integer, nullable=True)  # Jumlah siswa hadir
    student_notes = Column(Text, nullable=True)  # Catatan tentang siswa
    
    # Assessment & outcomes
    assessment_method = Column(String(255), nullable=True)  # Cara penilaian
    achievement_notes = Column(Text, nullable=True)  # Catatan pencapaian
    challenges = Column(Text, nullable=True)  # Kendala/hambatan yang dihadapi
    
    # Resources
    media_used = Column(String(500), nullable=True)  # Media pembelajaran yang digunakan
    reference_materials = Column(Text, nullable=True)  # Bahan referensi
    
    # File attachments
    attachment_path = Column(String(500), nullable=True)
    attachment_filename = Column(String(255), nullable=True)
    
    # Follow-up
    follow_up_notes = Column(Text, nullable=True)  # Rencana tindak lanjut
    next_class_plan = Column(Text, nullable=True)  # Rencana pembelajaran berikutnya
    
    # Status
    is_submitted = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    verified_by = Column(Integer, nullable=True)  # Admin/Kepala Sekolah yang verifikasi
    verified_at = Column(DateTime, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    teacher = relationship("User", back_populates="journal_entries")
    class_ = relationship("Class", back_populates="journal_entries")
    kompetensi_dasar = relationship("KompetensiDasar", back_populates="journal_entries")
    module = relationship("TeachingModule", back_populates="journal_entries")

    def __repr__(self):
        return f"<TeachingJournal(id={self.id}, date={self.date}, class_id={self.class_id})>"
