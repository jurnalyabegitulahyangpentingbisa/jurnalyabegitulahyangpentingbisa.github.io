# Deployment Guide - Jurnal Mengajar & Absensi Siswa

Complete guide for deploying the application to production.

## 🌍 Deployment Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     GitHub Pages                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           Frontend (Static Files)                    │  │
│  │  - HTML, CSS, JavaScript                            │  │
│  │  - API Client (talks to backend)                    │  │
│  │  - No backend server needed on GitHub Pages         │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           ↓
                    (CORS enabled)
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              Backend Server (Separate Host)                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  FastAPI Application                                │  │
│  │  - REST API endpoints                               │  │
│  │  - Authentication (JWT)                             │  │
│  │  - Business logic                                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                           ↓                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Oracle Database                                    │  │
│  │  - User management                                  │  │
│  │  - Journal entries                                  │  │
│  │  - Attendance records                               │  │
│  │  - Curriculum data                                  │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## 📦 Phase 1: Frontend Deployment (GitHub Pages)

### Option A: Root Directory Deployment

```bash
# 1. Ensure frontend files are in repository root
cd /your/repo
cp -r frontend/* .

# 2. Update index.html to point to production backend
# Edit frontend/js/api.js or create config file

# 3. Commit and push
git add .
git commit -m "Deploy frontend to GitHub Pages"
git push origin main

# 4. Enable GitHub Pages
# - Go to repository Settings
# - Scroll to "GitHub Pages" section
# - Source: main branch / root directory
# - Custom domain (optional)

# 5. Access your site
# https://username.github.io/
```

### Option B: /docs Directory Deployment

```bash
# 1. Move frontend files to /docs
mkdir -p docs
cp -r frontend/* docs/

# 2. Create docs/index.html as entry point
# (Already created if following this guide)

# 3. Commit and push
git add docs/
git commit -m "Deploy frontend to /docs"
git push origin main

# 4. Enable GitHub Pages
# - Settings → GitHub Pages
# - Source: main branch / /docs folder

# 5. Access your site
# https://username.github.io/
```

### Option C: Separate Repository

```bash
# 1. Create new repository: username.github.io
git clone https://github.com/username/username.github.io.git
cd username.github.io

# 2. Copy frontend files
cp -r /path/to/frontend/* .

# 3. Push
git add .
git commit -m "Initial commit - frontend"
git push origin main

# 4. Site automatically available at:
# https://username.github.io/
```

## 🔧 Phase 2: Backend Deployment

### Option A: Heroku Deployment

```bash
# 1. Create Heroku account and install CLI
brew tap heroku/brew && brew install heroku

# 2. Login to Heroku
heroku login

# 3. Create Heroku app
heroku create your-app-name

# 4. Add Oracle addon (or use external database)
heroku addons:create oracle-premium

# 5. Set environment variables
heroku config:set ORACLE_HOST=your-host
heroku config:set ORACLE_PORT=1521
heroku config:set ORACLE_USER=your-user
heroku config:set ORACLE_PASSWORD=your-password
heroku config:set ORACLE_DATABASE=your-db
heroku config:set SECRET_KEY=your-secret-key

# 6. Create Procfile in backend directory
echo "web: uvicorn app.main:app --host 0.0.0.0 --port $PORT" > Procfile

# 7. Deploy
git push heroku main

# 8. Initialize database
heroku run python scripts/init_database.py
heroku run python scripts/seed_data.py

# 9. Access your backend
# https://your-app-name.herokuapp.com/api
```

### Option B: AWS EC2 Deployment

```bash
# 1. Launch EC2 instance (Ubuntu 20.04+)

# 2. Connect and setup
ssh -i your-key.pem ubuntu@your-instance-ip

# 3. Install dependencies
sudo apt update
sudo apt install -y python3.10 python3-pip python3-venv
sudo apt install -y oracle-instantclient-basic oracle-instantclient-devel

# 4. Clone repository
git clone https://github.com/your-repo.git
cd your-repo/backend

# 5. Setup Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 6. Configure environment
cp .env.example .env
# Edit .env with your database credentials

# 7. Initialize database
python scripts/init_database.py
python scripts/seed_data.py

# 8. Install and configure Gunicorn
pip install gunicorn

# 9. Create systemd service
sudo nano /etc/systemd/system/journal-api.service
# [Unit]
# Description=Jurnal Mengajar API
# After=network.target
# 
# [Service]
# User=ubuntu
# WorkingDirectory=/home/ubuntu/your-repo/backend
# ExecStart=/home/ubuntu/your-repo/backend/venv/bin/gunicorn \
#   -w 4 -b 0.0.0.0:8000 app.main:app
# Restart=always
# 
# [Install]
# WantedBy=multi-user.target

# 10. Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable journal-api
sudo systemctl start journal-api

# 11. Install Nginx as reverse proxy
sudo apt install -y nginx

# 12. Configure Nginx
sudo nano /etc/nginx/sites-available/default
# server {
#     listen 80 default_server;
#     listen [::]:80 default_server;
#     server_name _;
#     
#     location / {
#         proxy_pass http://127.0.0.1:8000;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#     }
# }

# 13. Enable Nginx
sudo systemctl restart nginx

# 14. Setup SSL with Let's Encrypt
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com

# Backend now available at: https://your-domain.com/api
```

### Option C: Docker Deployment

```bash
# 1. Create Dockerfile in backend/
cat > Dockerfile << 'EOF'
FROM python:3.10-slim

WORKDIR /app

# Install Oracle client
RUN apt-get update && apt-get install -y \
    oracle-instantclient-basic \
    oracle-instantclient-devel \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

# 2. Create docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      ORACLE_HOST: ${ORACLE_HOST}
      ORACLE_PORT: ${ORACLE_PORT}
      ORACLE_USER: ${ORACLE_USER}
      ORACLE_PASSWORD: ${ORACLE_PASSWORD}
      ORACLE_DATABASE: ${ORACLE_DATABASE}
      SECRET_KEY: ${SECRET_KEY}
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: oracle/database:21.3.0-se2
    environment:
      ORACLE_SID: XE
      ORACLE_PWD: ${ORACLE_PASSWORD}
    ports:
      - "1521:1521"
    volumes:
      - oracle_data:/opt/oracle/oradata
    restart: unless-stopped

volumes:
  oracle_data:
EOF

# 3. Create .env file
cp backend/.env.example .env
# Edit .env with credentials

# 4. Build and run
docker-compose build
docker-compose up -d

# 5. Initialize database
docker-compose exec api python scripts/init_database.py
docker-compose exec api python scripts/seed_data.py

# Backend available at: http://localhost:8000/api
```

## 🔗 Frontend-Backend Integration

### 1. Update API Base URL

Edit `frontend/js/api.js`:

```javascript
// Development
const api = new APIClient('http://localhost:8000/api');

// Production (GitHub Pages)
const api = new APIClient('https://your-backend-domain.com/api');

// Or dynamic based on environment
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:8000/api'
  : 'https://your-backend-domain.com/api';
const api = new APIClient(API_BASE);
```

### 2. Configure CORS on Backend

Edit `backend/app/main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:3000",
        "https://username.github.io",  # GitHub Pages
        "https://your-custom-domain.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 3. Test Integration

```bash
# 1. Start backend
cd backend
python -m uvicorn app.main:app --reload

# 2. Start local frontend server
cd frontend
python -m http.server 8080

# 3. Login with demo credentials
# Email: admin@smk.ac.id
# Password: admin123456

# 4. Verify API calls in browser console
# Check Network tab for API requests
```

## 🔐 Security Checklist

- [ ] Set strong SECRET_KEY in production
- [ ] Use HTTPS for all connections
- [ ] Enable CORS only for trusted origins
- [ ] Store database credentials in environment variables
- [ ] Configure firewall to allow only necessary ports
- [ ] Regular database backups
- [ ] Enable logging and monitoring
- [ ] Use rate limiting on API endpoints
- [ ] Regular security updates
- [ ] SQL injection prevention (SQLAlchemy handles this)
- [ ] Password hashing (bcrypt implemented)
- [ ] JWT token expiry set appropriately

## 📊 Monitoring & Logging

### Application Logs

```python
# In app/main.py, add logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

### Database Monitoring

```bash
# Check Oracle database connection
sqlplus -l user/password@host:1521/database

# Monitor connections
SELECT COUNT(*) FROM v$session;
```

### API Health Checks

```bash
# Test backend availability
curl https://your-backend-domain.com/api/health

# Expected response
# {"status": "ok", "version": "1.0.0"}
```

## 🚀 Performance Optimization

### Frontend
- Minify HTML/CSS/JS (future)
- Lazy load images
- Cache strategy with service workers (future)
- CDN for static assets (GitHub Pages)

### Backend
- Database query optimization
- Connection pooling
- Caching strategy
- Load balancing (if needed)

### Database
- Proper indexing
- Regular maintenance
- Query optimization

## 📈 Scaling Strategy

### Phase 1: Single Server
- Backend on single EC2/Heroku instance
- Oracle database on managed service (AWS RDS, Azure Database)
- Frontend on GitHub Pages or custom CDN

### Phase 2: Load Balancing
- Multiple backend instances behind load balancer
- Auto-scaling based on traffic
- Managed database service

### Phase 3: Microservices
- Separate services per feature (if needed)
- API Gateway
- Message queue for async tasks
- Distributed caching

## 🔄 Continuous Integration/Deployment

### GitHub Actions Example

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Test Backend
      run: |
        cd backend
        python -m pytest
    
    - name: Deploy to Heroku
      run: |
        echo "Deploy to Heroku"
        # Add deployment steps
      env:
        HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
    
    - name: Deploy to GitHub Pages
      run: |
        echo "GitHub Pages auto-deployed on push"
```

## 🆘 Troubleshooting

### CORS Errors
```
Solution: Check CORS configuration in app/main.py
- Verify frontend origin is in allow_origins
- Check Authorization header is allowed
```

### Database Connection Failed
```
Solution: Verify credentials
- Check .env file has correct values
- Verify firewall allows connection
- Test connection manually with sqlplus
```

### Static Files Not Loading
```
Solution: Check GitHub Pages settings
- Verify files are in correct directory
- Clear browser cache
- Check file paths in HTML
```

### API Timeout
```
Solution: Check backend status
- Verify backend server is running
- Check network connectivity
- Review backend logs for errors
```

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Oracle Database Documentation](https://docs.oracle.com/database/)
- [GitHub Pages Documentation](https://pages.github.com/)
- [Heroku Deployment Guide](https://devcenter.heroku.com/)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)

## 📞 Support

For deployment issues:
1. Check logs (frontend console, backend logs)
2. Verify environment configuration
3. Test API connectivity
4. Review error messages carefully
5. Check documentation above

---

**Last Updated**: 2024
**Status**: Complete (Frontend + Backend Ready)
