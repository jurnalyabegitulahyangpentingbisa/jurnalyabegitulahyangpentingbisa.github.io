"""
Models untuk Authentication & User Management
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.core.database import Base


class UserRole(str, enum.Enum):
    """Enum untuk role pengguna"""
    ADMIN = "admin"
    GURU = "guru"
    SISWA = "siswa"
    KEPALA_SEKOLAH = "kepala_sekolah"


class User(Base):
    """Model untuk pengguna sistem"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.SISWA, nullable=False)
    
    # Profile information
    nip = Column(String(50), nullable=True)  # NIP untuk guru/admin
    nis = Column(String(50), nullable=True)  # NIS untuk siswa
    phone = Column(String(20), nullable=True)
    
    # Status
    is_active = Column(Boolean, default=True, index=True)
    is_verified = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)

    # Relationships
    journal_entries = relationship("TeachingJournal", back_populates="teacher")
    attendance_records = relationship("Attendance", back_populates="student")

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"


class Department(Base):
    """Model untuk departemen/jurusan"""
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)  # Teknik Komputer dan Jaringan
    code = Column(String(20), unique=True, nullable=False)   # TKJ
    description = Column(String(500), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    classes = relationship("Class", back_populates="department")

    def __repr__(self):
        return f"<Department(id={self.id}, name={self.name})>"


class Class(Base):
    """Model untuk kelas/rombongan belajar"""
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)  # X TKJ A, XI TKJ B, XII TKJ A
    grade = Column(Integer, nullable=False)  # 10, 11, 12
    department_id = Column(Integer, nullable=False)
    
    # Homeroom teacher
    homeroom_teacher_id = Column(Integer, nullable=True)
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    department = relationship("Department", back_populates="classes")
    students = relationship("Student", back_populates="class_")
    journal_entries = relationship("TeachingJournal", back_populates="class_")

    def __repr__(self):
        return f"<Class(id={self.id}, name={self.name}, grade={self.grade})>"


class Student(Base):
    """Model untuk siswa"""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  # Foreign key ke User table
    nis = Column(String(20), unique=True, nullable=False)
    class_id = Column(Integer, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    class_ = relationship("Class", back_populates="students")
    attendance_records = relationship("Attendance", back_populates="student")

    def __repr__(self):
        return f"<Student(id={self.id}, nis={self.nis})>"
