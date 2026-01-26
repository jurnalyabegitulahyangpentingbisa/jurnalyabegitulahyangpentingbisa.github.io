/**
 * Utility functions untuk aplikasi
 */

// Format tanggal ke format Indonesia
function formatDate(date) {
  if (typeof date === 'string') {
    date = new Date(date);
  }
  return new Intl.DateTimeFormat('id-ID', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  }).format(date);
}

// Format tanggal ke format input HTML
function formatDateForInput(date) {
  if (typeof date === 'string') {
    date = new Date(date);
  }
  return date.toISOString().split('T')[0];
}

// Show toast notification
function showToast(message, type = 'info') {
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.textContent = message;
  toast.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 16px 24px;
    background-color: ${getColorByType(type)};
    color: white;
    border-radius: 4px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    z-index: 9999;
    animation: slideIn 0.3s ease;
  `;
  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.animation = 'slideOut 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

function getColorByType(type) {
  const colors = {
    success: '#4CAF50',
    error: '#f44336',
    warning: '#ff9800',
    info: '#2196F3',
  };
  return colors[type] || colors.info;
}

// Check if user is logged in
function isLoggedIn() {
  return !!localStorage.getItem('access_token');
}

// Get logged in user
function getLoggedInUser() {
  const userStr = localStorage.getItem('user');
  return userStr ? JSON.parse(userStr) : null;
}

// Redirect to login if not logged in
function requireLogin() {
  if (!isLoggedIn()) {
    window.location.href = '/frontend/login.html';
  }
}

// Check if user has specific role
function hasRole(role) {
  const user = getLoggedInUser();
  return user && user.role === role;
}

// Format number as currency
function formatCurrency(amount) {
  return new Intl.NumberFormat('id-ID', {
    style: 'currency',
    currency: 'IDR',
  }).format(amount);
}

// Load configuration
async function loadConfig() {
  // Check if backend is available
  const isBackendAvailable = await api.healthCheck();
  
  if (!isBackendAvailable) {
    console.warn('Backend API not available. Using demo mode.');
    showToast('Catatan: Backend tidak tersedia. Mode demo diaktifkan.', 'warning');
  }
  
  return {
    backendAvailable: isBackendAvailable,
    apiUrl: api.baseURL,
  };
}

// Parse query string
function getQueryParam(param) {
  const searchParams = new URLSearchParams(window.location.search);
  return searchParams.get(param);
}

// Add CSS animation styles
const style = document.createElement('style');
style.textContent = `
  @keyframes slideIn {
    from {
      transform: translateX(400px);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }

  @keyframes slideOut {
    from {
      transform: translateX(0);
      opacity: 1;
    }
    to {
      transform: translateX(400px);
      opacity: 0;
    }
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .loading {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 3px solid #f3f3f3;
    border-top: 3px solid #2196F3;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
`;
document.head.appendChild(style);
