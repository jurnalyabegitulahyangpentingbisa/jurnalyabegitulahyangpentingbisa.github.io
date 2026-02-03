# Frontend - Jurnal Mengajar & Absensi Siswa

Frontend aplikasi Jurnal Mengajar & Absensi Siswa yang dibangun dengan vanilla HTML, CSS, dan JavaScript. Fully compatible dengan GitHub Pages untuk static hosting.

## 📁 Struktur Direktori

```
frontend/
├── index.html              # Halaman login (entry point)
├── dashboard.html          # Dashboard utama (Admin/Guru/Siswa)
├── journal.html            # Halaman jurnal mengajar (Guru)
├── attendance.html         # Halaman absensi (Guru & Siswa)
├── admin.html              # Admin panel (Admin saja)
├── settings.html           # Pengaturan profil pengguna
├── css/
│   └── styles.css          # Styling global dan responsive
├── js/
│   ├── api.js              # API client abstraction layer
│   └── utils.js            # Utility functions & helpers
└── assets/                 # Images, icons, dll
```

## 🚀 Quick Start

### 1. Setup Lokal (Development)

```bash
# Clone repository
git clone https://github.com/jurnalyabegitulahyangpentingbisa.github.io.git
cd frontend

# Buka di browser (local server diperlukan)
# Jangan buka file:// langsung karena localStorage limited
python -m http.server 8080
# atau
npx http-server

# Akses: http://localhost:8080
```

### 2. Deploy ke GitHub Pages

```bash
# Pastikan file berada di root repository (atau /docs folder)
git add frontend/*
git commit -m "Add frontend"
git push origin main

# GitHub Pages akan serve dari: https://username.github.io/
```

### 3. Backend Configuration

Edit `frontend/js/api.js` untuk mengubah URL backend:

```javascript
// Default: http://localhost:8000/api
const api = new APIClient('http://your-backend-url/api');
```

## 📄 File Descriptions

### index.html - Login Page
- Entry point aplikasi
- Form login dengan validasi
- Demo credentials untuk testing (development only)
- Session management dengan localStorage
- Redirect berdasarkan role user

**Demo Credentials:**
- Admin: `admin@smk.ac.id` / `admin123456`
- Guru: `guru1@smk.ac.id` / `guru123456`
- Siswa: `siswa1@smk.ac.id` / `siswa123456`

### dashboard.html - Main Dashboard
Role-based interface:
- **Admin**: User management, class management, statistics
- **Guru**: Teaching statistics, recent journals, class overview
- **Siswa**: Attendance summary, recent attendance, permit history

### journal.html - Teaching Journal
**Features:**
- Create/edit/delete teaching journals
- Filter by class, date, status
- Pagination support
- Comprehensive form dengan fields:
  - Tanggal mengajar
  - Kelas & Kompetensi Dasar
  - Metode pembelajaran & media
  - Kehadiran siswa & assessment
  - Challenges & follow-up notes

### attendance.html - Attendance Management
**Teacher View:**
- Select class & date
- Record attendance per student
- Bulk attendance entry
- Notes per student

**Student View:**
- Monthly attendance summary
- Attendance calendar view
- Permit request system
- Detailed history table

### admin.html - Administration Panel
**Sections:**
- Users management
- Classes management
- Curriculum management (KI/KD, ATP, Modules)
- Attendance reports
- Export functionality

### settings.html - User Settings
**Features:**
- Profile management
- Change password
- Notification preferences
- API connection status
- Account management

## 🛠️ API Client (api.js)

Fully-featured API client dengan methods untuk semua endpoints:

```javascript
// Authentication
api.login(email, password)
api.logout()
api.getProfile()
api.updateProfile(data)
api.changePassword(oldPassword, newPassword)

// Teaching Journal
api.createJournal(journalData)
api.getJournals(filters)
api.getJournal(journalId)
api.updateJournal(journalId, data)
api.deleteJournal(journalId)
api.submitJournal(journalId)
api.verifyJournal(journalId, data)

// Attendance
api.recordAttendance(attendanceData)
api.bulkRecordAttendance(classId, date, records)
api.getAttendance(filters)
api.getStudentAttendanceHistory(studentId)
api.getAttendanceSummary(classId, month, year)
api.submitPermit(permitData)
api.getStudentPermits()
api.approvePermit(permitId, notes)
api.rejectPermit(permitId, notes)

// Curriculum
api.getKompetensiInti(grade)
api.getKompetensiDasar(kiId, grade)
api.getAturanTujuanPembelajaran(grade, fase)
api.getTeachingModules(atpId, kdId)
api.getPembelajaranMendalam(grade)

// Classes & Students
api.getClasses()
api.getClass(classId)
api.getClassStudents(classId)
api.createClass(data)
api.updateClass(classId, data)
api.deleteClass(classId)

// Dashboards
api.getAdminDashboard()
api.getTeacherDashboard()
api.getStudentDashboard()
```

## 🛠️ Utility Functions (utils.js)

```javascript
// Date Formatting
formatDate(date)           // Format ke Indonesian locale
formatDateForInput(date)   // Format untuk HTML input

// Authentication
isLoggedIn()               // Check jika user terautentikasi
getLoggedInUser()          // Get user object dari localStorage
requireLogin()             // Guard function (redirect ke login)
hasRole(role)              // Check role permission

// UI Utilities
showToast(message, type)   // Show notification (success/danger/warning/info)
getQueryParam(param)       // Get URL query parameter

// Configuration
loadConfig()               // Load & validate backend URL
```

## 🎨 Styling System

### CSS Architecture
- **Global Styles**: `css/styles.css` (900+ lines)
- **CSS Variables**: Color scheme, shadows, spacing
- **Responsive Design**: Mobile-first approach
- **No Build Process**: Pure CSS, no preprocessors

### Color Scheme
```css
--primary-color: #2196F3      (Blue)
--secondary-color: #FF9800    (Orange)
--success-color: #4CAF50      (Green)
--danger-color: #f44336       (Red)
--warning-color: #ff9800      (Orange)
--info-color: #2196F3         (Blue)
```

### Components
- Cards, badges, tables, forms, buttons
- Modals, alerts, notifications
- Grid system (responsive)
- Stat cards, sidebar navigation

## 🔐 Authentication Flow

```javascript
// Login
1. User submits email/password
2. api.login() sends to /auth/login
3. Backend returns { access_token, user }
4. Token stored in localStorage
5. User object stored in localStorage
6. Redirect to appropriate dashboard

// Logout
1. api.logout() clears token
2. localStorage cleared
3. Redirect to login page

// Protected Routes
- requireLogin() checks isLoggedIn()
- If not logged in, redirect to index.html
- If logged in but wrong role, show error
```

## 📱 Responsive Design

```css
/* Mobile First */
- Base styles untuk mobile (< 768px)
- Tablet styles (768px - 1024px)
- Desktop styles (> 1024px)

Key Breakpoints:
@media (max-width: 768px)
  - Single column grid
  - Stack navigation
  - Smaller fonts & padding
```

## 🚀 Deployment

### GitHub Pages
1. Push frontend files ke repository root atau `/docs`
2. Enable GitHub Pages di settings
3. Access via `https://username.github.io`

### Custom Domain
1. Add CNAME file dengan domain
2. Configure DNS to point ke GitHub Pages
3. Enable HTTPS di repository settings

### CORS Configuration
Backend harus enable CORS untuk frontend origin:
```python
# FastAPI
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "https://username.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🔍 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 Error Handling

```javascript
try {
  const response = await api.login(email, password);
  // Success handling
} catch (error) {
  showToast(error.message, 'danger');
  // Error message displayed to user
}
```

## 💾 Local Storage Usage

```javascript
// Token
localStorage.getItem('token')          // JWT token
localStorage.setItem('token', token)

// User Profile
localStorage.getItem('user')           // User object JSON
localStorage.setItem('user', JSON.stringify(user))

// Notification Settings
localStorage.getItem('notificationSettings')

// Clear on logout
localStorage.removeItem('token')
localStorage.removeItem('user')
```

## 🔌 API Integration Checklist

- [x] API client fully implemented (api.js)
- [x] Authentication flow ready
- [x] Error handling setup
- [ ] Backend API endpoints (Next phase)
- [ ] Database implementation (Next phase)
- [ ] Testing suite (Future)

## 🚨 Known Limitations & TODO

### Current Implementation Status
- ✅ Frontend UI complete (7 pages)
- ✅ Responsive design implemented
- ✅ API client ready
- ✅ Utility functions complete
- ⏳ Backend API endpoints (to be implemented)
- ⏳ CRUD operations (dependent on backend)
- ⏳ Real data loading (dependent on backend)
- ⏳ File upload (for documents)
- ⏳ Export functionality (Excel/PDF)
- ⏳ Advanced filtering (dependent on backend)

### Testing Recommendations
1. Test with backend running on http://localhost:8000
2. Verify CORS is configured
3. Test authentication flow
4. Verify role-based access
5. Test responsive design on mobile

## 📚 Documentation

- [Backend Documentation](../PANDUAN_SETUP.md)
- [API Documentation](../docs/API_DOCUMENTATION.md)
- [Database Design](../docs/DATABASE_DESIGN.md)
- [User Guide](../docs/USER_GUIDE.md)

## 👨‍💻 Development Tips

### Adding New Pages
1. Create `pagename.html` in frontend/
2. Import `css/styles.css`, `js/api.js`, `js/utils.js`
3. Add navigation links in navbar
4. Implement authentication check with `requireLogin()`
5. Use `api.*` methods for data
6. Use `showToast()` for notifications

### Adding API Methods
1. Add method to `APIClient` class in `api.js`
2. Follow existing naming convention
3. Use `_get()`, `_post()`, `_put()`, `_delete()` helpers
4. Include proper error handling
5. Document method in README

### Styling Best Practices
1. Use CSS variables for colors
2. Mobile-first approach
3. Use grid/flex for layouts
4. Follow component structure
5. Maintain responsive design

## 📞 Support

For issues or questions:
- Check browser console for errors
- Verify backend API is running
- Check network tab for API calls
- Review error messages in showToast()

## 📄 License

Part of Jurnal Mengajar & Absensi Siswa project.
