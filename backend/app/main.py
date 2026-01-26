"""
FastAPI Application Main Entry Point
Journal Mengajar Online & Absensi Siswa
SMK Negeri 1 Lemahabang
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import init_db

# Import routes
# from app.auth import routes as auth_routes
# from app.journal import routes as journal_routes
# from app.attendance import routes as attendance_routes
# from app.curriculum import routes as curriculum_routes
# from app.dashboard import routes as dashboard_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application startup dan shutdown
    """
    # Startup
    print("🚀 Starting up application...")
    try:
        init_db()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down application...")


# Create FastAPI instance
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health Check Endpoint
@app.get("/", tags=["Health Check"])
async def root():
    """
    Root endpoint - Health check
    """
    return {
        "message": "Selamat datang di Journal Mengajar Online & Absensi Siswa",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get("/api/health", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint untuk monitoring
    """
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "database": "connected",
    }


# Include routers (uncomment setelah implementasi routers)
# app.include_router(auth_routes.router, prefix="/api/auth", tags=["Authentication"])
# app.include_router(journal_routes.router, prefix="/api/journal", tags=["Journal Mengajar"])
# app.include_router(attendance_routes.router, prefix="/api/attendance", tags=["Absensi"])
# app.include_router(curriculum_routes.router, prefix="/api/curriculum", tags=["Kurikulum"])
# app.include_router(dashboard_routes.router, prefix="/api/dashboard", tags=["Dashboard"])


# Error handling
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """
    Global exception handler
    """
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "message": str(exc) if settings.DEBUG else "An error occurred",
        },
    )


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        log_level="info",
    )
