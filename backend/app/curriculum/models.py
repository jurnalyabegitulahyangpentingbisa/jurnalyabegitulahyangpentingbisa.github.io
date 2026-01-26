"""
Models untuk Curriculum Management (KI/KD, ATP, Teaching Modules)
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class KompetensiInti(Base):
    """
    Model untuk Kompetensi Inti (KI) - Kurikulum 2013
    KI adalah kelompok kompetensi yang harus dicapai siswa
    """
    __tablename__ = "kompetensi_inti"

    id = Column(Integer, primary_key=True, index=True)
    grade = Column(Integer, nullable=False)  # 10, 11, 12
    ki_number = Column(Integer, nullable=False)  # 1, 2, 3, 4
    description = Column(Text, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    kompetensi_dasar = relationship("KompetensiDasar", back_populates="kompetensi_inti")

    def __repr__(self):
        return f"<KompetensiInti(grade={self.grade}, ki={self.ki_number})>"


class KompetensiDasar(Base):
    """
    Model untuk Kompetensi Dasar (KD) - Kurikulum 2013
    KD adalah penjabaran lebih spesifik dari KI
    """
    __tablename__ = "kompetensi_dasar"

    id = Column(Integer, primary_key=True, index=True)
    ki_id = Column(Integer, ForeignKey("kompetensi_inti.id"), nullable=False)
    kd_number = Column(String(50), nullable=False)  # 3.1, 4.1, dll
    description = Column(Text, nullable=False)
    
    # Indikator pencapaian
    learning_indicators = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    kompetensi_inti = relationship("KompetensiInti", back_populates="kompetensi_dasar")
    journal_entries = relationship("TeachingJournal", back_populates="kompetensi_dasar")

    def __repr__(self):
        return f"<KompetensiDasar(kd={self.kd_number})>"


class AturanTujuanPembelajaran(Base):
    """
    Model untuk Alur Tujuan Pembelajaran (ATP) - Kurikulum Merdeka
    ATP menjabarkan tujuan pembelajaran secara bertahap
    """
    __tablename__ = "alur_tujuan_pembelajaran"

    id = Column(Integer, primary_key=True, index=True)
    grade = Column(Integer, nullable=False)  # 10, 11, 12
    fase = Column(String(10), nullable=False)  # D, E, F (sesuai kurikulum merdeka)
    subject_code = Column(String(20), nullable=False)  # Kode mata pelajaran
    subject_name = Column(String(255), nullable=False)  # Nama mata pelajaran
    
    # Content dan tujuan pembelajaran
    learning_objectives = Column(Text, nullable=False)
    content_description = Column(Text, nullable=True)
    
    # Duration
    duration_weeks = Column(Integer, nullable=True)
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    teaching_modules = relationship("TeachingModule", back_populates="atp")

    def __repr__(self):
        return f"<ATP(grade={self.grade}, subject={self.subject_name})>"


class TeachingModule(Base):
    """
    Model untuk Modul Pembelajaran
    Modul berisi materi pembelajaran yang terstruktur
    """
    __tablename__ = "teaching_modules"

    id = Column(Integer, primary_key=True, index=True)
    atp_id = Column(Integer, ForeignKey("alur_tujuan_pembelajaran.id"), nullable=True)
    
    module_number = Column(String(20), nullable=False)  # Modul 1, Modul 2, dll
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    # Content
    learning_outcomes = Column(Text, nullable=True)
    key_concepts = Column(Text, nullable=True)
    learning_activities = Column(Text, nullable=True)
    assessment_method = Column(Text, nullable=True)
    
    # File attachment
    file_path = Column(String(500), nullable=True)
    file_name = Column(String(255), nullable=True)
    
    # Metadata
    duration_hours = Column(Integer, nullable=True)
    difficulty_level = Column(String(50), nullable=True)  # Mudah, Sedang, Sulit
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    atp = relationship("AturanTujuanPembelajaran", back_populates="teaching_modules")
    journal_entries = relationship("TeachingJournal", back_populates="module")

    def __repr__(self):
        return f"<TeachingModule(id={self.id}, title={self.title})>"


class PembelajaranMendalam(Base):
    """
    Model untuk Pembelajaran Mendalam (Deep Learning)
    Program ekstensif dengan fokus pada mastery dan aplikasi praktis
    """
    __tablename__ = "pembelajaran_mendalam"

    id = Column(Integer, primary_key=True, index=True)
    grade = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=nullable)
    
    # Learning structure
    phase_one = Column(Text, nullable=True)  # Fase 1: Problem Understanding
    phase_two = Column(Text, nullable=True)  # Fase 2: Knowledge Construction
    phase_three = Column(Text, nullable=True)  # Fase 3: Application & Reflection
    
    # Resources
    required_materials = Column(Text, nullable=True)
    reference_materials = Column(Text, nullable=True)
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<PembelajaranMendalam(id={self.id}, title={self.title})>"
