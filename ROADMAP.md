# 🗓️ Roadmap & Implementation Checklist

## 📌 Fase Development

### ✅ Fase 1: Foundation & Setup (COMPLETED)
**Status**: 100% Complete ✅

- [x] Project initialization dengan FastAPI
- [x] Database schema design dengan SQLAlchemy
- [x] Oracle database configuration
- [x] Environment variables setup
- [x] Models untuk semua modules:
  - [x] Authentication (User, Department, Class, Student)
  - [x] Journal Mengajar (TeachingJournal)
  - [x] Attendance (Attendance, AttendanceSummary, AttendancePermit)
  - [x] Curriculum (KI, KD, ATP, TeachingModule, DeepLearning)
- [x] Security utilities (JWT, bcrypt)
- [x] Database initialization scripts
- [x] Data seeding scripts
- [x] Complete documentation

---

### ⏳ Fase 2: API Implementation (IN PROGRESS)
**Estimated Completion**: 2-3 weeks  
**Status**: 0% Complete (Ready to Start)

#### A. Authentication Routes (5-6 endpoints)
- [ ] POST `/auth/register` - Daftar user baru
- [ ] POST `/auth/login` - Login & get JWT token
- [ ] GET `/auth/me` - Get current user profile
- [ ] POST `/auth/change-password` - Change password
- [ ] POST `/auth/logout` - Logout (invalidate token)
- [ ] GET `/auth/refresh` - Refresh token (optional)

**Sub-tasks**:
- [ ] Create AuthSchema (RegisterRequest, LoginResponse)
- [ ] Implement CRUD operations (create_user, get_user_by_email)
- [ ] Add JWT token generation logic
- [ ] Add dependency injection untuk authentication
- [ ] Add route handler logic

#### B. Journal Routes (6-8 endpoints)
- [ ] POST `/journal` - Create new journal entry
- [ ] GET `/journal` - List journals (dengan filtering & pagination)
- [ ] GET `/journal/{id}` - Get detail journal
- [ ] PUT `/journal/{id}` - Update journal
- [ ] DELETE `/journal/{id}` - Delete journal
- [ ] POST `/journal/{id}/submit` - Submit untuk approval
- [ ] GET `/journal/{id}/history` - Get version history (optional)
- [ ] POST `/journal/{id}/verify` - Verify journal (admin only)

**Sub-tasks**:
- [ ] Create JournalSchema (Create, Update, Response)
- [ ] Implement CRUD operations
- [ ] Add filtering (date range, class, teacher)
- [ ] Add pagination (skip, limit)
- [ ] Add role-based access control
- [ ] Add file upload handling (attachment)
- [ ] Add verification workflow

#### C. Attendance Routes (8-10 endpoints)
- [ ] POST `/attendance` - Record single attendance
- [ ] POST `/attendance/bulk` - Record multiple attendance
- [ ] GET `/attendance/student/{student_id}` - Get attendance history
- [ ] GET `/attendance/class/{class_id}` - Get class attendance summary
- [ ] GET `/attendance/summary` - Get monthly summary
- [ ] POST `/attendance/permits` - Submit attendance permit
- [ ] GET `/attendance/permits` - List permits
- [ ] GET `/attendance/permits/{id}` - Get permit detail
- [ ] POST `/attendance/permits/{id}/approve` - Approve permit
- [ ] POST `/attendance/permits/{id}/reject` - Reject permit

**Sub-tasks**:
- [ ] Create AttendanceSchema & PermitSchema
- [ ] Implement CRUD operations
- [ ] Add attendance calculations (percentage, summary)
- [ ] Add permit approval workflow
- [ ] Add file upload untuk permit documents
- [ ] Add status filtering
- [ ] Add date filtering

#### D. Curriculum Routes (4-6 endpoints)
- [ ] GET `/curriculum/ki-kd` - List KI/KD (filtered by grade)
- [ ] GET `/curriculum/ki-kd/{id}` - Get detail KI/KD
- [ ] GET `/curriculum/atp` - List ATP
- [ ] GET `/curriculum/atp/{id}` - Get detail ATP
- [ ] GET `/curriculum/modules` - List teaching modules
- [ ] GET `/curriculum/deep-learning` - List deep learning programs

**Sub-tasks**:
- [ ] Create CurriculumSchema
- [ ] Implement CRUD operations
- [ ] Add filtering (grade, phase, difficulty)
- [ ] Add search functionality
- [ ] Add file download untuk modules

#### E. Dashboard Routes (3 endpoints)
- [ ] GET `/dashboard/admin/summary` - Admin dashboard
- [ ] GET `/dashboard/teacher/my-summary` - Teacher dashboard
- [ ] GET `/dashboard/student/my-summary` - Student dashboard

**Sub-tasks**:
- [ ] Create aggregation queries
- [ ] Calculate statistics
- [ ] Generate charts data
- [ ] Add caching (optional)

#### F. User Management Routes (Admin) (5-6 endpoints)
- [ ] GET `/admin/users` - List users
- [ ] POST `/admin/users` - Create user
- [ ] PUT `/admin/users/{id}` - Update user
- [ ] DELETE `/admin/users/{id}` - Delete/deactivate user
- [ ] POST `/admin/users/{id}/reset-password` - Reset user password
- [ ] GET `/admin/users/{id}/activity` - Get user activity log (optional)

**Sub-tasks**:
- [ ] Create UserManagementSchema
- [ ] Implement CRUD operations
- [ ] Add role assignment
- [ ] Add status management (active/inactive)
- [ ] Add activity logging

---

### ⏳ Fase 3: Frontend Development (PLANNED)
**Estimated Completion**: 4-5 weeks  
**Status**: 0% Complete (Not Started)

#### A. Admin Dashboard
- [ ] User management page
- [ ] Department management page
- [ ] Class management page
- [ ] Curriculum management pages (KI/KD, ATP, Modules)
- [ ] Journal verification page
- [ ] Attendance management page
- [ ] Reports & statistics page
- [ ] System settings page

#### B. Teacher Dashboard
- [ ] Journal entry form
- [ ] Journal list & history
- [ ] Attendance recording (single & bulk)
- [ ] Student list per class
- [ ] Attendance summary per class
- [ ] Reports & statistics
- [ ] Profile management

#### C. Student Dashboard
- [ ] View personal attendance
- [ ] Submit attendance permit
- [ ] View permit status
- [ ] View class information
- [ ] Download modules
- [ ] View learning resources
- [ ] Profile management

#### D. Admin Portal
- [ ] Login page
- [ ] Navigation menu
- [ ] Responsive design
- [ ] User management panel
- [ ] Settings page

---

### ⏳ Fase 4: Testing & Quality Assurance (PLANNED)
**Estimated Completion**: 2-3 weeks  
**Status**: 0% Complete (Not Started)

- [ ] Unit tests untuk setiap endpoint
- [ ] Integration tests untuk workflow
- [ ] Database migration tests
- [ ] Security tests (SQL injection, XSS)
- [ ] Performance tests (load testing)
- [ ] API documentation testing
- [ ] Accessibility testing (WCAG)
- [ ] Browser compatibility testing

---

### ⏳ Fase 5: Deployment & Launch (PLANNED)
**Estimated Completion**: 1-2 weeks  
**Status**: 0% Complete (Not Started)

- [ ] Environment preparation (staging, production)
- [ ] Database migration to production
- [ ] SSL/TLS certificate setup
- [ ] Backup & disaster recovery plan
- [ ] Monitoring & logging setup
- [ ] Documentation finalization
- [ ] User training
- [ ] Go-live & monitoring

---

## 📊 Implementation Priority Matrix

### High Priority (MVP)
**Target**: Week 1-2
```
1. Authentication Routes
2. Journal Routes (CRUD)
3. Attendance Routes (Record)
4. Dashboard Routes
```

### Medium Priority
**Target**: Week 3-4
```
5. Attendance Routes (Summary & Permits)
6. Curriculum Routes
7. User Management Routes
```

### Low Priority (Nice-to-have)
**Target**: Week 5+
```
8. Advanced features
9. Reporting & analytics
10. Export functionality
```

---

## 🛠️ Testing Strategy

### Unit Tests
```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=app tests/

# Run specific test
pytest tests/test_auth.py::test_login
```

### Integration Tests
- Test full workflows (login → journal → submit)
- Test database transactions
- Test error handling

### API Tests
- Test all endpoints dengan Postman collection
- Test request validation
- Test error responses
- Test role-based access

---

## 📈 Success Metrics

| Metric | Target |
|--------|--------|
| API Endpoints | 27+ |
| Code Coverage | > 80% |
| Response Time | < 500ms |
| Database Queries | < 3 per request |
| Uptime | > 99% |
| Documentation | 100% |

---

## 📅 Estimated Timeline

| Phase | Duration | Start | End |
|-------|----------|-------|-----|
| **Phase 1** (Foundation) | 1 week | Jan 20 | Jan 26 ✅ |
| **Phase 2** (API) | 2-3 weeks | Jan 27 | Feb 16 |
| **Phase 3** (Frontend) | 4-5 weeks | Feb 17 | Mar 23 |
| **Phase 4** (Testing) | 2-3 weeks | Mar 24 | Apr 13 |
| **Phase 5** (Deployment) | 1-2 weeks | Apr 14 | Apr 27 |

**Total**: ~3 months untuk full development & deployment

---

## 🎯 Current Status

### ✅ Completed
- [x] Project setup & structure
- [x] Database schema design
- [x] All models implemented
- [x] Security utilities
- [x] Documentation (6 files)
- [x] Setup scripts
- [x] Seed data

### 🔄 In Progress
- [ ] API endpoint implementation

### 📋 To Do
- [ ] Frontend development
- [ ] Testing & QA
- [ ] Deployment preparation
- [ ] User training materials

---

## 🚀 Quick Start untuk Phase 2

### 1. Setup Environment
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Initialize Database
```bash
python scripts/init_database.py
python scripts/seed_data.py
```

### 3. Create First Route
Buat file `app/auth/routes.py`:
```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
async def login(email: str, password: str):
    # Implementation here
    pass
```

### 4. Include Router di main.py
```python
from app.auth import routes as auth_routes
app.include_router(auth_routes.router, prefix="/api")
```

### 5. Test API
```bash
python run.py
# Visit http://localhost:8000/docs
```

---

## 📚 Resources untuk Phase 2

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io)
- [JWT Documentation](https://tools.ietf.org/html/rfc7519)

---

## 🤝 Team Coordination

### Recommended Workflow
1. **Assign endpoints** ke team members
2. **Create branches** untuk setiap feature
3. **Create PR** untuk code review
4. **Test sebelum merge** ke main

### Communication
- Daily standup meetings
- GitHub issues untuk tracking
- Slack/WhatsApp untuk urgent updates

---

## ✅ Deployment Checklist (Phase 5)

- [ ] All endpoints tested & working
- [ ] All tests passing
- [ ] Documentation up-to-date
- [ ] Security audit completed
- [ ] Performance optimized
- [ ] Database backed up
- [ ] Monitoring configured
- [ ] Users trained
- [ ] Go-live checklist completed

---

**Last Updated**: 2026-01-26  
**Version**: 1.0.0  
**Status**: Phase 1 Complete ✅
