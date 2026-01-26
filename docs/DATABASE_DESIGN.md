# Desain Database Oracle
## Journal Mengajar Online & Absensi Siswa
### SMK Negeri 1 Lemahabang - Teknik Komputer dan Jaringan

---

## 📋 Entity Relationship Diagram (ERD)

```
┌─────────────────────┐
│       Users         │
├─────────────────────┤
│ id (PK)             │
│ email (UNIQUE)      │
│ username (UNIQUE)   │
│ full_name           │
│ hashed_password     │
│ role (ENUM)         │
│ nip/nis             │
│ phone               │
│ is_active           │
│ is_verified         │
│ created_at          │
│ updated_at          │
│ last_login          │
└──────────┬──────────┘
           │
      ┌────┴─────────────────┐
      │                      │
      ▼                      ▼
┌─────────────────┐  ┌──────────────────┐
│  Students       │  │ Teaching Journals│
├─────────────────┤  ├──────────────────┤
│ id (PK)         │  │ id (PK)          │
│ user_id (FK)    │  │ teacher_id (FK)  │
│ nis             │  │ class_id (FK)    │
│ class_id (FK)   │  │ kd_id (FK)       │
└────────┬────────┘  │ module_id (FK)   │
         │           │ date             │
         │           │ subject          │
         │           │ material_summary │
         │           │ ...              │
         │           └──────────────────┘
         │
         ▼
┌─────────────────────┐
│    Attendance       │
├─────────────────────┤
│ id (PK)             │
│ student_id (FK)     │
│ class_id (FK)       │
│ date                │
│ status (ENUM)       │
│ notes               │
│ created_at          │
│ updated_at          │
└─────────────────────┘

┌─────────────────────┐      ┌───────────────────┐
│    Classes          │      │   Departments     │
├─────────────────────┤      ├───────────────────┤
│ id (PK)             │◄─────│ id (PK)           │
│ name                │      │ name              │
│ grade               │      │ code              │
│ department_id (FK)  │      │ description       │
│ homeroom_teacher_id │      └───────────────────┘
│ is_active           │
└─────────────────────┘

┌──────────────────────────┐
│ Kompetensi Inti (KI)     │
├──────────────────────────┤
│ id (PK)                  │
│ grade                    │
│ ki_number                │
│ description              │
│ created_at               │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Kompetensi Dasar (KD)    │
├──────────────────────────┤
│ id (PK)                  │
│ ki_id (FK)               │
│ kd_number                │
│ description              │
│ learning_indicators      │
└──────────────────────────┘

┌──────────────────────────────────┐
│ Alur Tujuan Pembelajaran (ATP)   │
├──────────────────────────────────┤
│ id (PK)                          │
│ grade                            │
│ fase (D/E/F)                     │
│ subject_code                     │
│ subject_name                     │
│ learning_objectives              │
│ content_description              │
│ duration_weeks                   │
│ is_active                        │
└──────┬───────────────────────────┘
       │
       ▼
┌──────────────────────────┐
│   Teaching Modules       │
├──────────────────────────┤
│ id (PK)                  │
│ atp_id (FK)              │
│ module_number            │
│ title                    │
│ description              │
│ learning_outcomes        │
│ key_concepts             │
│ learning_activities      │
│ assessment_method        │
│ file_path                │
│ duration_hours           │
│ difficulty_level         │
│ is_active                │
└──────────────────────────┘

┌──────────────────────────────┐
│ Pembelajaran Mendalam        │
├──────────────────────────────┤
│ id (PK)                      │
│ grade                        │
│ title                        │
│ description                  │
│ phase_one                    │
│ phase_two                    │
│ phase_three                  │
│ required_materials           │
│ reference_materials          │
│ is_active                    │
└──────────────────────────────┘

┌──────────────────────────────┐
│  Attendance Summary          │
├──────────────────────────────┤
│ id (PK)                      │
│ student_id (FK)              │
│ year                         │
│ month                        │
│ hadir                        │
│ sakit                        │
│ izin                         │
│ alfa                         │
│ attendance_percentage        │
│ is_finalized                 │
│ finalized_at                 │
│ finalized_by                 │
└──────────────────────────────┘

┌──────────────────────────────┐
│  Attendance Permits          │
├──────────────────────────────┤
│ id (PK)                      │
│ student_id (FK)              │
│ start_date                   │
│ end_date                     │
│ reason                       │
│ permit_type                  │
│ document_path                │
│ status (pending/approved)    │
│ approved_by                  │
│ approval_notes               │
│ approved_at                  │
└──────────────────────────────┘
```

---

## 📊 Tabel Detail

### 1. USERS (Pengguna Sistem)
```sql
CREATE TABLE users (
    id NUMBER PRIMARY KEY,
    email VARCHAR2(255) NOT NULL UNIQUE,
    username VARCHAR2(100) NOT NULL UNIQUE,
    full_name VARCHAR2(255) NOT NULL,
    hashed_password VARCHAR2(255) NOT NULL,
    role VARCHAR2(50) DEFAULT 'siswa',  -- admin, guru, siswa, kepala_sekolah
    nip VARCHAR2(50),                     -- Nomor Induk Pegawai (guru/admin)
    nis VARCHAR2(50),                     -- Nomor Induk Siswa
    phone VARCHAR2(20),
    is_active CHAR(1) DEFAULT 'Y',
    is_verified CHAR(1) DEFAULT 'N',
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    last_login TIMESTAMP,
    CONSTRAINT chk_role CHECK (role IN ('admin', 'guru', 'siswa', 'kepala_sekolah')),
    CONSTRAINT chk_active CHECK (is_active IN ('Y', 'N'))
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
```

### 2. DEPARTMENTS (Departemen/Jurusan)
```sql
CREATE TABLE departments (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL UNIQUE,
    code VARCHAR2(20) NOT NULL UNIQUE,
    description VARCHAR2(500),
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE
);
```

### 3. CLASSES (Kelas/Rombongan Belajar)
```sql
CREATE TABLE classes (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    grade NUMBER NOT NULL,  -- 10, 11, 12
    department_id NUMBER NOT NULL,
    homeroom_teacher_id NUMBER,
    is_active CHAR(1) DEFAULT 'Y',
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_classes_dept FOREIGN KEY (department_id) 
        REFERENCES departments(id),
    CONSTRAINT chk_grade CHECK (grade IN (10, 11, 12))
);
```

### 4. STUDENTS (Siswa)
```sql
CREATE TABLE students (
    id NUMBER PRIMARY KEY,
    user_id NUMBER NOT NULL,
    nis VARCHAR2(20) NOT NULL UNIQUE,
    class_id NUMBER NOT NULL,
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_students_user FOREIGN KEY (user_id) 
        REFERENCES users(id),
    CONSTRAINT fk_students_class FOREIGN KEY (class_id) 
        REFERENCES classes(id)
);
```

### 5. KOMPETENSI_INTI (KI - Kurikulum 2013)
```sql
CREATE TABLE kompetensi_inti (
    id NUMBER PRIMARY KEY,
    grade NUMBER NOT NULL,  -- 10, 11, 12
    ki_number NUMBER NOT NULL,  -- 1, 2, 3, 4
    description CLOB NOT NULL,
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT chk_ki_num CHECK (ki_number BETWEEN 1 AND 4)
);
```

### 6. KOMPETENSI_DASAR (KD - Kurikulum 2013)
```sql
CREATE TABLE kompetensi_dasar (
    id NUMBER PRIMARY KEY,
    ki_id NUMBER NOT NULL,
    kd_number VARCHAR2(50) NOT NULL,  -- 3.1, 4.1, dll
    description CLOB NOT NULL,
    learning_indicators CLOB,
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_kd_ki FOREIGN KEY (ki_id) 
        REFERENCES kompetensi_inti(id)
);
```

### 7. ALUR_TUJUAN_PEMBELAJARAN (ATP - Kurikulum Merdeka)
```sql
CREATE TABLE alur_tujuan_pembelajaran (
    id NUMBER PRIMARY KEY,
    grade NUMBER NOT NULL,  -- 10, 11, 12
    fase VARCHAR2(10) NOT NULL,  -- D, E, F
    subject_code VARCHAR2(20) NOT NULL,
    subject_name VARCHAR2(255) NOT NULL,
    learning_objectives CLOB NOT NULL,
    content_description CLOB,
    duration_weeks NUMBER,
    is_active CHAR(1) DEFAULT 'Y',
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE
);
```

### 8. TEACHING_MODULES (Modul Pembelajaran)
```sql
CREATE TABLE teaching_modules (
    id NUMBER PRIMARY KEY,
    atp_id NUMBER,
    module_number VARCHAR2(20) NOT NULL,
    title VARCHAR2(255) NOT NULL,
    description CLOB,
    learning_outcomes CLOB,
    key_concepts CLOB,
    learning_activities CLOB,
    assessment_method CLOB,
    file_path VARCHAR2(500),
    file_name VARCHAR2(255),
    duration_hours NUMBER,
    difficulty_level VARCHAR2(50),  -- Mudah, Sedang, Sulit
    is_active CHAR(1) DEFAULT 'Y',
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_modules_atp FOREIGN KEY (atp_id) 
        REFERENCES alur_tujuan_pembelajaran(id)
);
```

### 9. PEMBELAJARAN_MENDALAM (Deep Learning)
```sql
CREATE TABLE pembelajaran_mendalam (
    id NUMBER PRIMARY KEY,
    grade NUMBER NOT NULL,
    title VARCHAR2(255) NOT NULL,
    description CLOB,
    phase_one CLOB,       -- Problem Understanding
    phase_two CLOB,       -- Knowledge Construction
    phase_three CLOB,     -- Application & Reflection
    required_materials CLOB,
    reference_materials CLOB,
    is_active CHAR(1) DEFAULT 'Y',
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE
);
```

### 10. TEACHING_JOURNALS (Journal Mengajar)
```sql
CREATE TABLE teaching_journals (
    id NUMBER PRIMARY KEY,
    teacher_id NUMBER NOT NULL,
    class_id NUMBER NOT NULL,
    kd_id NUMBER,
    module_id NUMBER,
    date TIMESTAMP NOT NULL,
    subject VARCHAR2(255) NOT NULL,
    material_summary CLOB NOT NULL,
    learning_method VARCHAR2(255),
    learning_activities CLOB,
    student_attendance NUMBER,
    student_notes CLOB,
    assessment_method VARCHAR2(255),
    achievement_notes CLOB,
    challenges CLOB,
    media_used VARCHAR2(500),
    reference_materials CLOB,
    attachment_path VARCHAR2(500),
    attachment_filename VARCHAR2(255),
    follow_up_notes CLOB,
    next_class_plan CLOB,
    is_submitted CHAR(1) DEFAULT 'N',
    is_verified CHAR(1) DEFAULT 'N',
    verified_by NUMBER,
    verified_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_journal_class FOREIGN KEY (class_id) 
        REFERENCES classes(id),
    CONSTRAINT fk_journal_kd FOREIGN KEY (kd_id) 
        REFERENCES kompetensi_dasar(id),
    CONSTRAINT fk_journal_module FOREIGN KEY (module_id) 
        REFERENCES teaching_modules(id)
);

CREATE INDEX idx_journal_date ON teaching_journals(date);
CREATE INDEX idx_journal_teacher ON teaching_journals(teacher_id);
```

### 11. ATTENDANCE (Absensi Siswa)
```sql
CREATE TABLE attendance (
    id NUMBER PRIMARY KEY,
    student_id NUMBER NOT NULL,
    class_id NUMBER NOT NULL,
    date TIMESTAMP NOT NULL,
    status VARCHAR2(50) DEFAULT 'hadir',  -- hadir, sakit, izin, alfa, libur
    notes VARCHAR2(500),
    recorded_by NUMBER,
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_att_student FOREIGN KEY (student_id) 
        REFERENCES students(id),
    CONSTRAINT fk_att_class FOREIGN KEY (class_id) 
        REFERENCES classes(id),
    CONSTRAINT chk_att_status CHECK (status IN ('hadir', 'sakit', 'izin', 'alfa', 'libur'))
);

CREATE INDEX idx_att_date ON attendance(date);
CREATE INDEX idx_att_student ON attendance(student_id);
```

### 12. ATTENDANCE_SUMMARY (Ringkasan Absensi)
```sql
CREATE TABLE attendance_summary (
    id NUMBER PRIMARY KEY,
    student_id NUMBER NOT NULL,
    year NUMBER NOT NULL,
    month NUMBER NOT NULL,
    hadir NUMBER DEFAULT 0,
    sakit NUMBER DEFAULT 0,
    izin NUMBER DEFAULT 0,
    alfa NUMBER DEFAULT 0,
    attendance_percentage NUMBER,
    is_finalized CHAR(1) DEFAULT 'N',
    finalized_at TIMESTAMP,
    finalized_by NUMBER,
    created_at TIMESTAMP DEFAULT SYSDATE,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_summ_student FOREIGN KEY (student_id) 
        REFERENCES students(id),
    CONSTRAINT chk_month CHECK (month BETWEEN 1 AND 12)
);
```

### 13. ATTENDANCE_PERMITS (Surat Izin)
```sql
CREATE TABLE attendance_permits (
    id NUMBER PRIMARY KEY,
    student_id NUMBER NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    reason VARCHAR2(500) NOT NULL,
    permit_type VARCHAR2(50) NOT NULL,  -- Sakit, Izin Orang Tua, Acara, dll
    document_path VARCHAR2(500),
    document_filename VARCHAR2(255),
    status VARCHAR2(50) DEFAULT 'pending',  -- pending, approved, rejected
    approved_by NUMBER,
    approval_notes VARCHAR2(500),
    approved_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT SYSDATE,
    submitted_at TIMESTAMP,
    updated_at TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_perm_student FOREIGN KEY (student_id) 
        REFERENCES students(id),
    CONSTRAINT chk_perm_status CHECK (status IN ('pending', 'approved', 'rejected'))
);
```

---

## 🔑 Indexing Strategy

```sql
-- Performance indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_classes_grade ON classes(grade);
CREATE INDEX idx_att_date ON attendance(date);
CREATE INDEX idx_att_student ON attendance(student_id);
CREATE INDEX idx_journal_date ON teaching_journals(date);
CREATE INDEX idx_journal_teacher ON teaching_journals(teacher_id);
CREATE INDEX idx_ki_grade ON kompetensi_inti(grade);
CREATE INDEX idx_atp_grade ON alur_tujuan_pembelajaran(grade);
```

---

## 📈 Data Relationships

| Table | Related To | Relationship |
|-------|-----------|--------------|
| students | users | 1-to-1 |
| students | classes | Many-to-1 |
| classes | departments | Many-to-1 |
| teaching_journals | users (teacher) | Many-to-1 |
| teaching_journals | classes | Many-to-1 |
| teaching_journals | kompetensi_dasar | Many-to-1 |
| teaching_journals | teaching_modules | Many-to-1 |
| attendance | students | Many-to-1 |
| attendance | classes | Many-to-1 |
| attendance_summary | students | Many-to-1 |
| attendance_permits | students | Many-to-1 |
| kompetensi_dasar | kompetensi_inti | Many-to-1 |
| teaching_modules | alur_tujuan_pembelajaran | Many-to-1 |

---

**Last Updated**: 2026-01-26
**Version**: 1.0.0
