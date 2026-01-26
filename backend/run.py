#!/usr/bin/env python3
"""
Script untuk menjalankan aplikasi FastAPI
Journal Mengajar Online & Absensi Siswa
"""

import uvicorn
import sys
from app.core.config import settings

if __name__ == "__main__":
    print("=" * 60)
    print(f"🚀 {settings.APP_NAME}")
    print(f"📌 Version: {settings.APP_VERSION}")
    print(f"🌍 Environment: {settings.ENVIRONMENT}")
    print("=" * 60)
    print(f"🔗 Server: http://{settings.SERVER_HOST}:{settings.SERVER_PORT}")
    print(f"📖 Docs: http://{settings.SERVER_HOST}:{settings.SERVER_PORT}/docs")
    print(f"📚 ReDoc: http://{settings.SERVER_HOST}:{settings.SERVER_PORT}/redoc")
    print("=" * 60)
    
    uvicorn.run(
        "app.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        log_level="info",
    )
