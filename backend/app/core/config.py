from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings(BaseSettings):
    """
    Konfigurasi aplikasi Journal Mengajar Online & Absensi Siswa
    """

    # Database Configuration
    ORACLE_USER: str = os.getenv("ORACLE_USER", "smk_admin")
    ORACLE_PASSWORD: str = os.getenv("ORACLE_PASSWORD", "password")
    ORACLE_HOST: str = os.getenv("ORACLE_HOST", "localhost")
    ORACLE_PORT: int = int(os.getenv("ORACLE_PORT", "1521"))
    ORACLE_SID: str = os.getenv("ORACLE_SID", "XE")
    ORACLE_CHARSET: str = os.getenv("ORACLE_CHARSET", "UTF8")

    @property
    def DATABASE_URL(self) -> str:
        """Generate Oracle connection string"""
        return (
            f"oracle+cx_oracle://{self.ORACLE_USER}:{self.ORACLE_PASSWORD}"
            f"@{self.ORACLE_HOST}:{self.ORACLE_PORT}/{self.ORACLE_SID}"
            f"?charset={self.ORACLE_CHARSET}"
        )

    # Application Configuration
    APP_NAME: str = os.getenv("APP_NAME", "Journal Mengajar Online & Absensi Siswa")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    APP_DESCRIPTION: str = os.getenv(
        "APP_DESCRIPTION",
        "Sistem manajemen journal mengajar dan absensi siswa SMK Negeri 1 Lemahabang"
    )

    # Security
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY", 
        "your_super_secret_key_change_this_in_production"
    )
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
    )

    # Server Configuration
    SERVER_HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
    ]

    # Email Configuration
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")

    class Config:
        env_file = ".env"
        case_sensitive = True


# Instance konfigurasi global
settings = Settings()
