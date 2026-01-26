from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
from app.core.config import settings

# Create SQLAlchemy engine untuk Oracle
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    poolclass=pool.QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,  # Test koneksi sebelum digunakan
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

# Base class untuk semua models
Base = declarative_base()


def get_db():
    """
    Dependency untuk mendapatkan database session
    Gunakan dalam FastAPI endpoints
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_context():
    """
    Context manager untuk database session
    Gunakan dalam scripts atau background tasks
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Inisialisasi database - buat semua tables
    Jalankan sekali saat pertama kali setup
    """
    Base.metadata.create_all(bind=engine)


def drop_all_tables():
    """
    Drop semua tables - gunakan dengan hati-hati!
    """
    Base.metadata.drop_all(bind=engine)
