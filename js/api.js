/**
 * API Client untuk Journal Mengajar Online & Absensi Siswa
 * Menghubungkan frontend dengan backend Python FastAPI
 */

class APIClient {
  constructor(baseURL = 'http://localhost:8000/api') {
    this.baseURL = baseURL;
    // support both 'token' and 'access_token' keys (some pages use one or the other)
    this.token = localStorage.getItem('token') || localStorage.getItem('access_token');
    this.user = JSON.parse(localStorage.getItem('user') || '{}');
    // Demo mode for GitHub Pages / static hosting
    this.demo = location.hostname.includes('github.io') || location.protocol === 'file:';

    if (this.demo) {
      this._initDemoData();
    }
  }

  /**
   * Set API base URL (untuk production)
   */
  setBaseURL(url) {
    this.baseURL = url;
  }

  /**
   * Get headers untuk API request
   */
  getHeaders() {
    const headers = {
      'Content-Type': 'application/json',
    };

    if (this.token) {
      headers['Authorization'] = `Bearer ${this.token}`;
    }

    return headers;
  }

  /**
   * Handle API response
   */
  async handleResponse(response) {
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || error.message || 'API Error');
    }
    return await response.json();
  }

  /**
   * LOGIN
   */
  async login(email, password) {
    const params = new URLSearchParams();
    params.append('email', email);
    params.append('password', password);

    if (this.demo) {
      const users = this._loadDemo('demo_users');
      const user = users.find(u => u.email === email && u.password === password);
      if (!user) throw new Error('Email atau password salah');

      const data = {
        access_token: `demo-token-${user.id}`,
        user: Object.assign({}, user, { password: undefined })
      };

      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('token', data.access_token);
      localStorage.setItem('user', JSON.stringify(data.user));
      this.token = data.access_token;
      this.user = data.user;
      return data;
    }

    const response = await fetch(`${this.baseURL}/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: params,
    });

    const data = await this.handleResponse(response);
    
    // Store token & user
    localStorage.setItem('access_token', data.access_token);
    localStorage.setItem('user', JSON.stringify(data.user));
    this.token = data.access_token;
    this.user = data.user;
    return data;
  }

  /**
   * LOGOUT
   */
  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    this.token = null;
    this.user = {};
  }

  /**
   * Get current user profile
   */
  async getProfile() {
    if (this.demo) {
      return this.user || null;
    }
    const response = await fetch(`${this.baseURL}/auth/me`, {
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  /**
   * JOURNAL ENDPOINTS
   */
  async createJournal(journalData) {
    if (this.demo) {
      const journals = this._loadDemo('demo_journals');
      const id = this._nextId('journal');
      const newJournal = Object.assign({ id: id, is_verified: false, created_by: this.user.email }, journalData);
      journals.unshift(newJournal);
      this._saveDemo('demo_journals', journals);
      return newJournal;
    }

    const response = await fetch(`${this.baseURL}/journal`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(journalData),
    });
    return await this.handleResponse(response);
  }

  async getJournals(filters = {}) {
    if (this.demo) {
      const journals = this._loadDemo('demo_journals');
      let result = journals.slice();

      if (filters.class_id) {
        result = result.filter(j => String(j.class_id) === String(filters.class_id));
      }
      if (filters.date || filters.start_date || filters.end_date) {
        const start = filters.start_date || filters.date;
        const end = filters.end_date || filters.date;
        if (start) result = result.filter(j => j.date === start || j.date >= start);
        if (end) result = result.filter(j => j.date <= end);
      }

      const total = result.length;
      const skip = parseInt(filters.skip) || 0;
      const limit = parseInt(filters.limit) || 10;
      const page = result.slice(skip, skip + limit);
      return { journals: page, total: total };
    }

    const params = new URLSearchParams();
    if (filters.skip) params.append('skip', filters.skip);
    if (filters.limit) params.append('limit', filters.limit);
    if (filters.start_date) params.append('start_date', filters.start_date);
    if (filters.end_date) params.append('end_date', filters.end_date);
    if (filters.class_id) params.append('class_id', filters.class_id);

    const response = await fetch(`${this.baseURL}/journal?${params}`, {
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  async getJournal(id) {
    if (this.demo) {
      const journals = this._loadDemo('demo_journals');
      return journals.find(j => String(j.id) === String(id));
    }
    const response = await fetch(`${this.baseURL}/journal/${id}`, {
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  async updateJournal(id, journalData) {
    if (this.demo) {
      const journals = this._loadDemo('demo_journals');
      const idx = journals.findIndex(j => String(j.id) === String(id));
      if (idx === -1) throw new Error('Jurnal tidak ditemukan');
      journals[idx] = Object.assign(journals[idx], journalData);
      this._saveDemo('demo_journals', journals);
      return journals[idx];
    }

    const response = await fetch(`${this.baseURL}/journal/${id}`, {
      method: 'PUT',
      headers: this.getHeaders(),
      body: JSON.stringify(journalData),
    });
    return await this.handleResponse(response);
  }

  async deleteJournal(id) {
    if (this.demo) {
      let journals = this._loadDemo('demo_journals');
      journals = journals.filter(j => String(j.id) !== String(id));
      this._saveDemo('demo_journals', journals);
      return true;
    }
    const response = await fetch(`${this.baseURL}/journal/${id}`, {
      method: 'DELETE',
      headers: this.getHeaders(),
    });
    return response.ok;
  }

  async submitJournal(id) {
    const response = await fetch(`${this.baseURL}/journal/${id}/submit`, {
      method: 'POST',
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  /**
   * ATTENDANCE ENDPOINTS
   */
  async recordAttendance(attendanceData) {
    if (this.demo) {
      const records = this._loadDemo('demo_attendance');
      records.push(attendanceData);
      this._saveDemo('demo_attendance', records);
      return attendanceData;
    }
    const response = await fetch(`${this.baseURL}/attendance`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(attendanceData),
    });
    return await this.handleResponse(response);
  }

  async bulkRecordAttendance(classId, date, records) {
    if (this.demo) {
      const store = this._loadDemo('demo_attendance');
      records.forEach(r => store.push(r));
      this._saveDemo('demo_attendance', store);
      return { ok: true };
    }

    const response = await fetch(`${this.baseURL}/attendance/bulk`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify({
        class_id: classId,
        date: date,
        records: records,
      }),
    });
    return await this.handleResponse(response);
  }

  async getStudentAttendance(studentId, filters = {}) {
    const params = new URLSearchParams();
    if (filters.start_date) params.append('start_date', filters.start_date);
    if (filters.end_date) params.append('end_date', filters.end_date);
    const response = await fetch(
      `${this.baseURL}/attendance/${studentId}?${params}`,
      {
        headers: this.getHeaders(),
      }
    );
    return await this.handleResponse(response);
  }

  // Demo helper endpoints used by frontend pages
  async getClassStudents(classId) {
    if (this.demo) {
      const students = this._loadDemo('demo_students');
      return students.filter(s => String(s.class_id) === String(classId));
    }
    const response = await fetch(`${this.baseURL}/classes/${classId}/students`, { headers: this.getHeaders() });
    return await this.handleResponse(response);
  }

  async getClasses() {
    if (this.demo) {
      return this._loadDemo('demo_classes');
    }
    const response = await fetch(`${this.baseURL}/classes`, { headers: this.getHeaders() });
    return await this.handleResponse(response);
  }

  async getKompetensiDasar() {
    if (this.demo) return this._loadDemo('demo_kds');
    const response = await fetch(`${this.baseURL}/curriculum/kd`, { headers: this.getHeaders() });
    return await this.handleResponse(response);
  }

  async getTeachingModules() {
    if (this.demo) return this._loadDemo('demo_modules');
    const response = await fetch(`${this.baseURL}/curriculum/modules`, { headers: this.getHeaders() });
    return await this.handleResponse(response);
  }

  async getStudentDashboard() {
    if (this.demo) {
      // compute basic stats for logged in user
      const attendance = this._loadDemo('demo_attendance').filter(a => String(a.student_id) === String(this.user.id));
      const present = attendance.filter(a => a.status === 'hadir').length;
      const sick = attendance.filter(a => a.status === 'sakit').length;
      const permit = attendance.filter(a => a.status === 'izin').length;
      const absent = attendance.filter(a => a.status === 'alfa').length;
      const total = present + sick + permit + absent || 1;
      return {
        present_days: present,
        sick_days: sick,
        permit_days: permit,
        absent_days: absent,
        attendance_percentage: (present / total) * 100,
        recent_attendance: attendance.slice(-10)
      };
    }
    const response = await fetch(`${this.baseURL}/dashboard/student/my-summary`, { headers: this.getHeaders() });
    return await this.handleResponse(response);
  }

  async getStudentAttendanceHistory() {
    if (this.demo) {
      return this._loadDemo('demo_attendance').filter(a => String(a.student_id) === String(this.user.id));
    }
    const response = await fetch(`${this.baseURL}/attendance/me/history`, { headers: this.getHeaders() });
    return await this.handleResponse(response);
  }

  async getStudentPermits() {
    if (this.demo) return this._loadDemo('demo_permits').filter(p => String(p.student_id) === String(this.user.id));
    const response = await fetch(`${this.baseURL}/attendance/permits`, { headers: this.getHeaders() });
    return await this.handleResponse(response);
  }

  async submitPermit(permitData) {
    if (this.demo) {
      const permits = this._loadDemo('demo_permits');
      const id = this._nextId('permit');
      const record = Object.assign({ id: id, student_id: this.user.id, status: 'pending' }, permitData);
      permits.push(record);
      this._saveDemo('demo_permits', permits);
      return record;
    }
    const response = await fetch(`${this.baseURL}/attendance/permits`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(permitData),
    });
    return await this.handleResponse(response);
  }

  async getAdminDashboard() {
    if (this.demo) {
      const users = this._loadDemo('demo_users');
      const classes = this._loadDemo('demo_classes');
      const teachers = users.filter(u => u.role === 'Guru').length;
      const students = users.filter(u => u.role === 'Siswa').length;
      return {
        total_teachers: teachers,
        total_students: students,
        total_classes: classes.length,
        recent_users: users.slice(-10).reverse(),
        classes: classes
      };
    }
    const response = await fetch(`${this.baseURL}/dashboard/admin/summary`, { headers: this.getHeaders() });
    return await this.handleResponse(response);
  }

  async getTeacherDashboard() {
    if (this.demo) {
      const journals = this._loadDemo('demo_journals').filter(j => j.created_by === this.user.email);
      const classes = this._loadDemo('demo_classes').filter(c => c.teacher_email === this.user.email).length;
      const verified = journals.filter(j => j.is_verified).length;
      return {
        total_journals: journals.length,
        verified_journals: verified,
        classes_count: classes,
        recent_journals: journals.slice(0,5)
      };
    }
    const response = await fetch(`${this.baseURL}/dashboard/teacher/my-summary`, { headers: this.getHeaders() });
    return await this.handleResponse(response);
  }

  // Demo data helpers
  _loadDemo(key) {
    try {
      return JSON.parse(localStorage.getItem(key) || 'null') || [];
    } catch (e) {
      return [];
    }
  }

  _saveDemo(key, val) {
    localStorage.setItem(key, JSON.stringify(val));
  }

  _nextId(namespace) {
    const key = `demo_next_${namespace}`;
    const cur = parseInt(localStorage.getItem(key) || '1', 10);
    localStorage.setItem(key, String(cur + 1));
    return cur;
  }

  _initDemoData() {
    // Seed classes
    if (!localStorage.getItem('demo_classes')) {
      const classes = [
        { id: 1, name: 'X TKJ 1', grade: 10, department_name: 'TKJ', teacher_email: 'guru1@smk.ac.id' },
        { id: 2, name: 'XI TKJ 1', grade: 11, department_name: 'TKJ', teacher_email: 'guru1@smk.ac.id' },
        { id: 3, name: 'XII TKJ 1', grade: 12, department_name: 'TKJ', teacher_email: 'guru2@smk.ac.id' }
      ];
      this._saveDemo('demo_classes', classes);
    }

    // Seed students
    if (!localStorage.getItem('demo_students')) {
      const students = [
        { id: 101, nis: '1001', full_name: 'Ahmad Fauzi', class_id: 1 },
        { id: 102, nis: '1002', full_name: 'Siti Aminah', class_id: 1 },
        { id: 201, nis: '2001', full_name: 'Budi Santoso', class_id: 2 },
        { id: 301, nis: '3001', full_name: 'Rina Kusuma', class_id: 3 }
      ];
      this._saveDemo('demo_students', students);
    }

    // Seed KD
    if (!localStorage.getItem('demo_kds')) {
      const kds = [
        { id: 1, code: 'KD1', description: 'Memahami konsep jaringan' },
        { id: 2, code: 'KD2', description: 'Menginstal sistem operasi' }
      ];
      this._saveDemo('demo_kds', kds);
    }

    // Seed modules
    if (!localStorage.getItem('demo_modules')) {
      const mods = [
        { id: 1, title: 'Pengenalan Jaringan' },
        { id: 2, title: 'Instalasi Windows' }
      ];
      this._saveDemo('demo_modules', mods);
    }

    // Seed users
    if (!localStorage.getItem('demo_users')) {
      const users = [
        { id: 1, email: 'admin@smk.ac.id', password: 'admin123456', role: 'Admin', full_name: 'Administrator' },
        { id: 2, email: 'guru1@smk.ac.id', password: 'guru123456', role: 'Guru', full_name: 'Guru 1' },
        { id: 3, email: 'siswa1@smk.ac.id', password: 'siswa123456', role: 'Siswa', full_name: 'Siswa 1' }
      ];
      this._saveDemo('demo_users', users);
    }

    // Seed journals
    if (!localStorage.getItem('demo_journals')) {
      const journals = [
        { id: 1, date: new Date().toISOString().split('T')[0], class_id: 1, class_name: 'X TKJ 1', kd_description: 'Memahami konsep jaringan', learning_method: 'ceramah', is_verified: true, created_by: 'guru1@smk.ac.id', subject: 'Jaringan' }
      ];
      this._saveDemo('demo_journals', journals);
      localStorage.setItem('demo_next_journal', '2');
    }

    if (!localStorage.getItem('demo_attendance')) this._saveDemo('demo_attendance', []);
    if (!localStorage.getItem('demo_permits')) this._saveDemo('demo_permits', []);
  }

  async getClassAttendance(classId, date) {
    const response = await fetch(
      `${this.baseURL}/attendance/class/${classId}?date=${date}`,
      {
        headers: this.getHeaders(),
      }
    );
    return await this.handleResponse(response);
  }

  async submitPermit(permitData) {
    const response = await fetch(`${this.baseURL}/attendance/permits`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(permitData),
    });
    return await this.handleResponse(response);
  }

  async getPermits() {
    const response = await fetch(`${this.baseURL}/attendance/permits`, {
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  async approvePermit(permitId, notes = '') {
    const response = await fetch(
      `${this.baseURL}/attendance/permits/${permitId}/approve`,
      {
        method: 'POST',
        headers: this.getHeaders(),
        body: JSON.stringify({ approval_notes: notes }),
      }
    );
    return await this.handleResponse(response);
  }

  /**
   * CURRICULUM ENDPOINTS
   */
  async getKIKD(filters = {}) {
    const params = new URLSearchParams();
    if (filters.grade) params.append('grade', filters.grade);
    if (filters.kd_number) params.append('kd_number', filters.kd_number);

    const response = await fetch(`${this.baseURL}/curriculum/ki-kd?${params}`, {
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  async getATP(filters = {}) {
    const params = new URLSearchParams();
    if (filters.grade) params.append('grade', filters.grade);
    if (filters.fase) params.append('fase', filters.fase);

    const response = await fetch(`${this.baseURL}/curriculum/atp?${params}`, {
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  async getTeachingModules(filters = {}) {
    const params = new URLSearchParams();
    if (filters.atp_id) params.append('atp_id', filters.atp_id);
    if (filters.difficulty) params.append('difficulty_level', filters.difficulty);

    const response = await fetch(
      `${this.baseURL}/curriculum/modules?${params}`,
      {
        headers: this.getHeaders(),
      }
    );
    return await this.handleResponse(response);
  }

  async getDeepLearning(filters = {}) {
    const params = new URLSearchParams();
    if (filters.grade) params.append('grade', filters.grade);

    const response = await fetch(
      `${this.baseURL}/curriculum/deep-learning?${params}`,
      {
        headers: this.getHeaders(),
      }
    );
    return await this.handleResponse(response);
  }

  /**
   * DASHBOARD ENDPOINTS
   */
  async getAdminDashboard() {
    const response = await fetch(`${this.baseURL}/dashboard/admin/summary`, {
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  async getTeacherDashboard() {
    const response = await fetch(
      `${this.baseURL}/dashboard/teacher/my-summary`,
      {
        headers: this.getHeaders(),
      }
    );
    return await this.handleResponse(response);
  }

  async getStudentDashboard() {
    const response = await fetch(
      `${this.baseURL}/dashboard/student/my-summary`,
      {
        headers: this.getHeaders(),
      }
    );
    return await this.handleResponse(response);
  }

  /**
   * Health check
   */
  async healthCheck() {
    try {
      const response = await fetch(`${this.baseURL.replace('/api', '')}/api/health`);
      return response.ok;
    } catch (error) {
      return false;
    }
  }
}

// Create global API client instance
const api = new APIClient();
