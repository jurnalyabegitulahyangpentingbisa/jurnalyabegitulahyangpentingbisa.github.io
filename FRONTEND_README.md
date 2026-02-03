// Frontend API Client
// Provides abstraction layer for all API communication
// Compatible with GitHub Pages static hosting

class APIClient {
  constructor(baseURL = 'http://localhost:8000/api') {
    this.baseURL = baseURL;
    this.token = localStorage.getItem('token');
  }

  // ===== Authentication =====
  async login(email, password) {
    const response = await fetch(`${this.baseURL}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Login failed');
    }

    const data = await response.json();
    this.token = data.access_token;
    localStorage.setItem('token', this.token);
    return data;
  }

  logout() {
    this.token = null;
    localStorage.removeItem('token');
  }

  // ===== User Profile =====
  async getProfile() {
    return this._get('/auth/me');
  }

  async updateProfile(data) {
    return this._put('/auth/me', data);
  }

  async changePassword(oldPassword, newPassword) {
    return this._post('/auth/change-password', { old_password: oldPassword, new_password: newPassword });
  }

  // ===== Teaching Journal =====
  async createJournal(journalData) {
    return this._post('/journal', journalData);
  }

  async getJournals(filters = {}) {
    const params = new URLSearchParams(Object.fromEntries(
      Object.entries(filters).filter(([_, v]) => v !== null && v !== undefined)
    ));
    return this._get(`/journal?${params.toString()}`);
  }

  async getJournal(journalId) {
    return this._get(`/journal/${journalId}`);
  }

  async updateJournal(journalId, journalData) {
    return this._put(`/journal/${journalId}`, journalData);
  }

  async deleteJournal(journalId) {
    return this._delete(`/journal/${journalId}`);
  }

  async submitJournal(journalId) {
    return this._post(`/journal/${journalId}/submit`, {});
  }

  async verifyJournal(journalId, verificationData) {
    return this._post(`/journal/${journalId}/verify`, verificationData);
  }

  // ===== Attendance =====
  async recordAttendance(attendanceData) {
    return this._post('/attendance', attendanceData);
  }

  async bulkRecordAttendance(classId, date, records) {
    return this._post('/attendance/bulk', {
      class_id: classId,
      date: date,
      records: records
    });
  }

  async getAttendance(filters = {}) {
    const params = new URLSearchParams(Object.fromEntries(
      Object.entries(filters).filter(([_, v]) => v !== null && v !== undefined)
    ));
    return this._get(`/attendance?${params.toString()}`);
  }

  async getStudentAttendanceHistory(studentId = null) {
    const endpoint = studentId ? `/attendance/student/${studentId}` : '/attendance/my-history';
    return this._get(endpoint);
  }

  async getAttendanceSummary(classId, month, year) {
    return this._get(`/attendance/summary?class_id=${classId}&month=${month}&year=${year}`);
  }

  // ===== Permits =====
  async submitPermit(permitData) {
    return this._post('/attendance/permits', permitData);
  }

  async getStudentPermits() {
    return this._get('/attendance/permits/my');
  }

  async approvePermit(permitId, notes = '') {
    return this._post(`/attendance/permits/${permitId}/approve`, { notes });
  }

  async rejectPermit(permitId, notes = '') {
    return this._post(`/attendance/permits/${permitId}/reject`, { notes });
  }

  // ===== Curriculum =====
  async getKompetensiInti(grade = null) {
    const url = grade ? `/curriculum/ki?grade=${grade}` : '/curriculum/ki';
    return this._get(url);
  }

  async getKompetensiDasar(kiId = null, grade = null) {
    let url = '/curriculum/kd';
    const params = [];
    if (kiId) params.push(`ki_id=${kiId}`);
    if (grade) params.push(`grade=${grade}`);
    if (params.length) url += '?' + params.join('&');
    return this._get(url);
  }

  async getAturanTujuanPembelajaran(grade = null, fase = null) {
    let url = '/curriculum/atp';
    const params = [];
    if (grade) params.push(`grade=${grade}`);
    if (fase) params.push(`fase=${fase}`);
    if (params.length) url += '?' + params.join('&');
    return this._get(url);
  }

  async getTeachingModules(atpId = null, kdId = null) {
    let url = '/curriculum/modules';
    const params = [];
    if (atpId) params.push(`atp_id=${atpId}`);
    if (kdId) params.push(`kd_id=${kdId}`);
    if (params.length) url += '?' + params.join('&');
    return this._get(url);
  }

  async getPembelajaranMendalam(grade = null) {
    const url = grade ? `/curriculum/deep-learning?grade=${grade}` : '/curriculum/deep-learning';
    return this._get(url);
  }

  // ===== Classes =====
  async getClasses() {
    return this._get('/classes');
  }

  async getClass(classId) {
    return this._get(`/classes/${classId}`);
  }

  async getClassStudents(classId) {
    return this._get(`/classes/${classId}/students`);
  }

  async createClass(classData) {
    return this._post('/classes', classData);
  }

  async updateClass(classId, classData) {
    return this._put(`/classes/${classId}`, classData);
  }

  async deleteClass(classId) {
    return this._delete(`/classes/${classId}`);
  }

  // ===== Students =====
  async getStudents(classId = null) {
    const url = classId ? `/students?class_id=${classId}` : '/students';
    return this._get(url);
  }

  async getStudent(studentId) {
    return this._get(`/students/${studentId}`);
  }

  async getStudentProfile() {
    return this._get('/students/me');
  }

  // ===== Dashboards =====
  async getAdminDashboard() {
    return this._get('/dashboard/admin/summary');
  }

  async getTeacherDashboard() {
    return this._get('/dashboard/teacher/my-summary');
  }

  async getStudentDashboard() {
    return this._get('/dashboard/student/my-summary');
  }

  // ===== Internal Methods =====
  async _get(endpoint) {
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      method: 'GET',
      headers: this._getHeaders()
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.detail || `HTTP Error: ${response.status}`);
    }

    const data = await response.json();
    return data;
  }

  async _post(endpoint, body) {
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      method: 'POST',
      headers: this._getHeaders(),
      body: JSON.stringify(body)
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.detail || `HTTP Error: ${response.status}`);
    }

    const data = await response.json();
    return data;
  }

  async _put(endpoint, body) {
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      method: 'PUT',
      headers: this._getHeaders(),
      body: JSON.stringify(body)
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.detail || `HTTP Error: ${response.status}`);
    }

    const data = await response.json();
    return data;
  }

  async _delete(endpoint) {
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      method: 'DELETE',
      headers: this._getHeaders()
    });

    if (!response.ok && response.status !== 204) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.detail || `HTTP Error: ${response.status}`);
    }

    const data = response.status === 204 ? {} : await response.json();
    return data;
  }

  _getHeaders() {
    const headers = {
      'Content-Type': 'application/json'
    };

    const token = localStorage.getItem('token');
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    return headers;
  }
}

// Global instance
const api = new APIClient();
