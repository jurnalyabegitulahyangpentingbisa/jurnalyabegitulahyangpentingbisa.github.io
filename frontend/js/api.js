/**
 * API Client untuk Journal Mengajar Online & Absensi Siswa
 * Menghubungkan frontend dengan backend Python FastAPI
 */

class APIClient {
  constructor(baseURL = 'http://localhost:8000/api') {
    this.baseURL = baseURL;
    this.token = localStorage.getItem('access_token');
    this.user = JSON.parse(localStorage.getItem('user') || '{}');
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
    localStorage.removeItem('user');
    this.token = null;
    this.user = {};
  }

  /**
   * Get current user profile
   */
  async getProfile() {
    const response = await fetch(`${this.baseURL}/auth/me`, {
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  /**
   * JOURNAL ENDPOINTS
   */
  async createJournal(journalData) {
    const response = await fetch(`${this.baseURL}/journal`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(journalData),
    });
    return await this.handleResponse(response);
  }

  async getJournals(filters = {}) {
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
    const response = await fetch(`${this.baseURL}/journal/${id}`, {
      headers: this.getHeaders(),
    });
    return await this.handleResponse(response);
  }

  async updateJournal(id, journalData) {
    const response = await fetch(`${this.baseURL}/journal/${id}`, {
      method: 'PUT',
      headers: this.getHeaders(),
      body: JSON.stringify(journalData),
    });
    return await this.handleResponse(response);
  }

  async deleteJournal(id) {
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
    const response = await fetch(`${this.baseURL}/attendance`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(attendanceData),
    });
    return await this.handleResponse(response);
  }

  async bulkRecordAttendance(classId, date, records) {
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
