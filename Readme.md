# 🏋️ AI Fitness Tracker - Backend API

A comprehensive Flask-based REST API for fitness tracking with AI-powered diet plans and chatbot assistance using Google's Gemini 2.0 Flash model.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing Guide](#testing-guide)
- [Troubleshooting](#troubleshooting)
- [Production Deployment](#production-deployment)

---

## ✨ Features

- 🔐 **JWT Authentication** - Secure user registration, login, and token-based authentication
- 👤 **User Management** - Profile management, role-based access control (Admin/User)
- 🧘 **Yoga Module** - CRUD operations for yoga poses with image uploads
- 💪 **Workout Module** - Exercise library with categories and difficulty levels
- 🥗 **Diet Plans** - AI-generated personalized diet plans using Gemini 2.0 Flash
- 🏃 **Exercise Plans** - Customized workout schedules based on user goals
- 🤖 **AI Chatbot** - Diet and nutrition Q&A powered by Gemini 2.0 Flash
- 📁 **File Storage** - Image uploads using MinIO object storage
- 📊 **User Statistics** - Activity tracking and analytics

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Flask** | 3.0.0 | Web framework |
| **PostgreSQL** | 16 | Primary database |
| **SQLAlchemy** | 3.1.1 | ORM |
| **Flask-JWT-Extended** | 4.5.3 | JWT authentication |
| **Google Gemini AI** | 2.0 Flash | AI-powered features |
| **MinIO** | Latest | Object storage |
| **Docker** | Latest | Containerization |
| **Bcrypt** | 4.1.2 | Password hashing |

---

## 📁 Project Structure

```
fitness-tracker-backend/
│
├── app/
│   ├── __init__.py              # Flask app initialization
│   │
│   ├── models/                  # Database models
│   │   ├── __init__.py
│   │   ├── role.py              # User roles (admin, user, trainer)
│   │   ├── user.py              # User model
│   │   ├── yoga.py              # Yoga poses
│   │   ├── workout.py           # Workout exercises
│   │   ├── diet_plan.py         # Diet plans
│   │   ├── exercise_plan.py     # Exercise plans
│   │   └── chatbot_query.py     # Chatbot history
│   │
│   ├── routes/                  # API endpoints
│   │   ├── __init__.py
│   │   ├── auth.py              # Authentication routes
│   │   ├── user.py              # User management routes
│   │   ├── yoga.py              # Yoga CRUD routes
│   │   ├── workout.py           # Workout CRUD routes
│   │   ├── diet.py              # Diet plan routes
│   │   ├── exercise.py          # Exercise plan routes
│   │   └── chatbot.py           # Chatbot routes
│   │
│   └── services/                # Business logic
│       ├── __init__.py
│       ├── gemini_service.py    # Gemini AI integration
│       └── minio_service.py     # MinIO file storage
│
├── migrations/                  # Database migrations
├── .env                         # Environment variables
├── .env.example                 # Environment template
├── requirements.txt             # Python dependencies
├── docker-compose.yaml          # Docker services
├── config.py                    # App configuration
├── run.py                       # Application entry point
├── create_tables.py             # Database table creation
├── seed_data.py                 # Sample data seeder
├── test_connection.py           # Connection testing
└── README.md                    # This file
```

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+** - [Download](https://www.python.org/downloads/)
- **Docker Desktop** - [Download](https://www.docker.com/products/docker-desktop/)
- **Postman** (optional) - [Download](https://www.postman.com/downloads/)
- **Git** - [Download](https://git-scm.com/downloads)

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/fitness-tracker-backend.git
cd fitness-tracker-backend
```

### Step 2: Create Virtual Environment

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
pip list | grep Flask
```

You should see Flask and related packages installed.

---

## ⚙️ Configuration

### 1. Create Environment File

Copy the example environment file:

```bash
cp .env.example .env
```

Or create `.env` manually with the following content:

### 2. Edit `.env` File

```bash
# ============================================
# AI Fitness Tracker - Environment Variables
# ============================================

# Database Configuration
POSTGRES_USER=hill
POSTGRES_PASSWORD=hill123
POSTGRES_DB=fitness_tracker
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Database Connection URL
DATABASE_URL=postgresql://hill:hill123@localhost:5432/fitness_tracker

# PgAdmin Configuration
PGADMIN_DEFAULT_EMAIL=admin@fitness.com
PGADMIN_DEFAULT_PASSWORD=admin123

# JWT Configuration
JWT_SECRET_KEY=your-super-secret-jwt-key-at-least-32-chars-long
SECRET_KEY=your-flask-secret-key-at-least-32-chars-long

# Gemini AI Configuration
# Get your API key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your-gemini-api-key-here

# MinIO Configuration
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_BUCKET_NAME=fitness-app
MINIO_SECURE=False

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SESSION_COOKIE_SECURE=False
PORT=5000
HOST=0.0.0.0
```

### 3. Generate Secure Keys (Optional)

For production, generate secure keys:

```bash
python generate_secrets.py
```

This will create strong random keys for `JWT_SECRET_KEY` and `SECRET_KEY`.

### 4. Get Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and paste it in `.env` as `GEMINI_API_KEY`

---

## 🗄️ Database Setup

### Step 1: Start Docker Services

```bash
docker-compose up -d postgres minio pgadmin
```

**Wait 10-15 seconds for services to initialize.**

### Step 2: Verify Services are Running

```bash
docker ps
```

You should see:
- `postgres-tsi` (PostgreSQL)
- `fitness-minio` (MinIO)
- `pgadmin-tsi` (PgAdmin)

### Step 3: Test Database Connection

```bash
python test_connection.py
```

Expected output:
```
✅ Environment Variables: PASS
✅ Python Packages: PASS
✅ Database Connection: PASS
```

### Step 4: Create Database Tables

```bash
python create_tables.py
```

This creates all tables:
- `roles`
- `users`
- `yoga`
- `workouts`
- `diet_plans`
- `exercise_plans`
- `chatbot_queries`

### Step 5: Seed Initial Data (Optional)

```bash
python seed_data.py
```

This creates:
- Default roles (admin, user, trainer)
- Admin user (admin@fitness.com / Admin@123)
- Test user (user@fitness.com / User@123)
- 5 sample yoga poses
- 5 sample workouts

---

## 🏃 Running the Application

### Development Mode

```bash
python run.py
```

**Server will start at:** `http://localhost:5000/`

Expected output:
```
🔍 ENVIRONMENT VARIABLES CHECK
✅ DATABASE_URL: postgresql://hill:hill123@localhost:5432/fitness_tracker
✅ JWT_SECRET_KEY: SET
✅ SECRET_KEY: SET

📊 Using database: postgresql://hill:hill123@localhost:5432/fitness_tracker
✓ Registered auth routes
✓ Registered user routes
✓ Registered yoga routes
✓ Registered workout routes
✓ Registered diet routes
✓ Registered exercise routes
✓ Registered chatbot routes

📦 Creating database tables...
✅ Database tables created successfully

✅ SERVER READY!

👉 API: http://localhost:5000/
👉 Health: http://localhost:5000/health
👉 Docs: http://localhost:5000/api/docs
```

### Production Mode

```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

---

## 📚 API Documentation

### Base URL

```
http://localhost:5000/api
```

### Authentication

Most endpoints require JWT authentication. Include the token in the header:

```
Authorization: Bearer <your_jwt_token>
```

---

## 📡 API Endpoints Overview

### 🔐 Authentication Module

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register` | Register new user | ❌ No |
| POST | `/api/auth/login` | Login user | ❌ No |
| POST | `/api/auth/logout` | Logout user | ✅ Yes |
| GET | `/api/auth/profile` | Get current user profile | ✅ Yes |
| PUT | `/api/auth/profile` | Update profile | ✅ Yes |
| POST | `/api/auth/change-password` | Change password | ✅ Yes |
| GET | `/api/auth/verify` | Verify token | ✅ Yes |

### 👥 User Management Module

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/users/` | Get all users | ✅ Admin |
| GET | `/api/users/{id}` | Get user by ID | ✅ Yes |
| PUT | `/api/users/{id}` | Update user | ✅ Yes |
| DELETE | `/api/users/{id}` | Delete user | ✅ Admin |
| GET | `/api/users/{id}/stats` | Get user statistics | ✅ Yes |
| GET | `/api/users/search` | Search users | ✅ Admin |

### 🧘 Yoga Module

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/yoga/` | Get all yoga poses | ❌ No |
| GET | `/api/yoga/{id}` | Get yoga pose by ID | ❌ No |
| POST | `/api/yoga/` | Create yoga pose | ✅ Admin |
| PUT | `/api/yoga/{id}` | Update yoga pose | ✅ Admin |
| DELETE | `/api/yoga/{id}` | Delete yoga pose | ✅ Admin |
| GET | `/api/yoga/difficulty/{level}` | Get by difficulty | ❌ No |

### 💪 Workout Module

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/workouts/` | Get all workouts | ❌ No |
| GET | `/api/workouts/{id}` | Get workout by ID | ❌ No |
| POST | `/api/workouts/` | Create workout | ✅ Admin |
| PUT | `/api/workouts/{id}` | Update workout | ✅ Admin |
| DELETE | `/api/workouts/{id}` | Delete workout | ✅ Admin |

### 🥗 Diet Plan Module

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/diet/generate` | Generate AI diet plan | ✅ Yes |
| GET | `/api/diet/` | Get user's diet plans | ✅ Yes |
| GET | `/api/diet/{id}` | Get specific diet plan | ✅ Yes |
| PUT | `/api/diet/{id}` | Update diet plan | ✅ Yes |
| DELETE | `/api/diet/{id}` | Delete diet plan | ✅ Yes |
| GET | `/api/diet/latest` | Get latest diet plan | ✅ Yes |
| GET | `/api/diet/statistics` | Get diet statistics | ✅ Yes |

### 🏃 Exercise Plan Module

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/exercise/generate` | Generate exercise plan | ✅ Yes |
| GET | `/api/exercise/` | Get user's exercise plans | ✅ Yes |
| GET | `/api/exercise/{id}` | Get specific plan | ✅ Yes |
| PUT | `/api/exercise/{id}` | Update plan | ✅ Yes |
| DELETE | `/api/exercise/{id}` | Delete plan | ✅ Yes |

### 🤖 Chatbot Module

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/chatbot/query` | Send question to AI | ✅ Yes |
| GET | `/api/chatbot/history` | Get chat history | ✅ Yes |
| GET | `/api/chatbot/{id}` | Get specific query | ✅ Yes |
| DELETE | `/api/chatbot/{id}` | Delete query | ✅ Yes |
| DELETE | `/api/chatbot/history` | Clear history | ✅ Yes |
| GET | `/api/chatbot/statistics` | Get statistics | ✅ Yes |
| POST | `/api/chatbot/quick-ask` | Quick ask (no save) | ✅ Yes |

---

## 🧪 API Testing Examples

### 1. Register User

**Request:**
```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "mobile_number": "1234567890"
}
```

**Response (201):**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "role": "user"
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 2. Login

**Request:**
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "role": "user"
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 3. Generate Diet Plan

**Request:**
```http
POST /api/diet/generate
Authorization: Bearer <your_token>
Content-Type: application/json

{
  "age": 25,
  "gender": "male",
  "weight": 70,
  "height": 175,
  "activity_level": "moderate",
  "goal": "weight_loss",
  "diet_type": "vegetarian",
  "duration": "1_month",
  "health_conditions": ["None"]
}
```

**Response (201):**
```json
{
  "message": "Diet plan generated successfully",
  "diet_plan": {
    "id": 1,
    "plan": {
      "user_info": {...},
      "meal_plan": "AI-generated meal plan...",
      "generated_by": "gemini-2.0-flash"
    },
    "created_at": "2025-01-20T10:30:00"
  }
}
```

### 4. Ask Chatbot

**Request:**
```http
POST /api/chatbot/query
Authorization: Bearer <your_token>
Content-Type: application/json

{
  "question": "What foods are high in protein?",
  "query_type": "diet"
}
```

**Response (201):**
```json
{
  "id": 1,
  "question": "What foods are high in protein?",
  "answer": "Foods high in protein include chicken, fish, eggs, beans, lentils, tofu, Greek yogurt, quinoa, and nuts. For a balanced diet...",
  "query_type": "diet",
  "created_at": "2025-01-20T10:30:00"
}
```

### 5. Upload Yoga Pose with Image

**Request:**
```http
POST /api/yoga/
Authorization: Bearer <admin_token>
Content-Type: multipart/form-data

yoga_name: Downward Dog
yoga_description: A foundational yoga pose
difficulty_level: beginner
duration_minutes: 5
benefits: Strengthens arms and legs
photo: [file]
```

**Response (201):**
```json
{
  "message": "Yoga pose created successfully",
  "yoga": {
    "id": 1,
    "yoga_name": "Downward Dog",
    "photo_url": "http://localhost:9000/fitness-app/yoga/uuid_image.jpg",
    "difficulty_level": "beginner"
  }
}
```

---

## 🔧 Gemini AI Integration

### Model Configuration

The application uses **Google Gemini 2.0 Flash** model for AI features.

**Location:** `app/services/gemini_service.py`

```python
import google.generativeai as genai
import os

class GeminiService:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.model = genai.GenerativeModel('models/gemini-2.0-flash')
```

### AI Features

1. **Diet Plan Generation**
   - Personalized meal plans based on user data
   - Calorie calculations
   - Nutritional recommendations

2. **Chatbot**
   - Diet and nutrition Q&A
   - Context-aware responses
   - Only diet-related queries accepted

### AI Query Restrictions

The chatbot is restricted to diet-related queries only:

```python
# Validation in app/routes/chatbot.py
diet_keywords = ['diet', 'food', 'meal', 'nutrition', 'calorie', 
                'protein', 'carb', 'fat', 'vitamin', 'eat', 
                'recipe', 'ingredient']
```

---

## 🗄️ Database Schema

### Tables Overview

#### 1. roles
```sql
id          INTEGER PRIMARY KEY
role_name   VARCHAR(50) UNIQUE NOT NULL
description VARCHAR(200)
```

#### 2. users
```sql
id              INTEGER PRIMARY KEY
username        VARCHAR(80) UNIQUE NOT NULL
email           VARCHAR(120) UNIQUE NOT NULL
password_hash   VARCHAR(255) NOT NULL
mobile_number   VARCHAR(15)
role_id         INTEGER FOREIGN KEY -> roles.id
created_at      TIMESTAMP DEFAULT NOW()
```

#### 3. yoga
```sql
id                 INTEGER PRIMARY KEY
yoga_name          VARCHAR(100) NOT NULL
yoga_description   TEXT
photo_url          VARCHAR(500) UNIQUE
difficulty_level   VARCHAR(20)
duration_minutes   INTEGER
benefits           TEXT
```

#### 4. workouts
```sql
id                   INTEGER PRIMARY KEY
workout_name         VARCHAR(100) NOT NULL
workout_description  TEXT
category             VARCHAR(50)
difficulty_level     VARCHAR(20)
duration_minutes     INTEGER
calories_burned      INTEGER
equipment_needed     TEXT
photo_url            VARCHAR(500)
```

#### 5. diet_plans
```sql
id          INTEGER PRIMARY KEY
user_id     INTEGER FOREIGN KEY -> users.id
diet_plan   JSON NOT NULL
created_at  TIMESTAMP DEFAULT NOW()
goal        VARCHAR(50)
diet_type   VARCHAR(50)
duration    VARCHAR(50)
```

#### 6. exercise_plans
```sql
id               INTEGER PRIMARY KEY
user_id          INTEGER FOREIGN KEY -> users.id
exercise_plan    JSON NOT NULL
created_at       TIMESTAMP DEFAULT NOW()
goal             VARCHAR(50)
difficulty_level VARCHAR(20)
duration_weeks   INTEGER
```

#### 7. chatbot_queries
```sql
id          INTEGER PRIMARY KEY
user_id     INTEGER FOREIGN KEY -> users.id
question    TEXT NOT NULL
answer      TEXT
query_type  VARCHAR(50)
created_at  TIMESTAMP DEFAULT NOW()
```

---

## 🐳 Docker Services

### Services Configuration

#### PostgreSQL (Port 5432)
- **Container:** `postgres-tsi`
- **Image:** `postgres:16`
- **User:** `hill`
- **Password:** `hill123`
- **Database:** `fitness_tracker`

#### MinIO (Ports 9000, 9001)
- **Container:** `fitness-minio`
- **Console:** `http://localhost:9001`
- **Username:** `minioadmin`
- **Password:** `minioadmin`
- **Bucket:** `fitness-app`

#### PgAdmin (Port 5050)
- **Container:** `pgadmin-tsi`
- **URL:** `http://localhost:5050`
- **Email:** `admin@fitness.com`
- **Password:** `7zi844I9qHo`

### Docker Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View running containers
docker ps

# View logs
docker logs postgres-tsi
docker logs fitness-minio
docker logs pgadmin-tsi

# Remove all data and restart fresh
docker-compose down -v
docker-compose up -d
```

---

## 🔍 Troubleshooting

### Issue 1: Database Connection Failed

**Error:**
```
password authentication failed for user "hill"
```

**Solutions:**
1. Check if PostgreSQL container is running:
   ```bash
   docker ps | grep postgres
   ```

2. Verify `.env` credentials match `docker-compose.yaml`

3. Restart PostgreSQL:
   ```bash
   docker-compose restart postgres
   ```

4. Check database exists:
   ```bash
   docker exec -it postgres-tsi psql -U hill -c "\l"
   ```

### Issue 2: Invalid Token Error

**Error:**
```json
{
  "error": "Invalid token",
  "message": "Authentication failed"
}
```

**Solutions:**
1. Ensure Authorization header format:
   ```
   Authorization: Bearer <token>
   ```

2. Check for extra spaces or quotes

3. Token might be expired - login again

4. Verify JWT_SECRET_KEY is set in `.env`

### Issue 3: Gemini API Error

**Error:**
```
google.api_core.exceptions.PermissionDenied
```

**Solutions:**
1. Verify API key is correct in `.env`
2. Check API key at: https://makersuite.google.com/app/apikey
3. Ensure billing is enabled on Google Cloud
4. Check model name: `models/gemini-2.0-flash`

### Issue 4: MinIO Connection Failed

**Error:**
```
Connection refused to localhost:9000
```

**Solutions:**
1. Start MinIO container:
   ```bash
   docker-compose up -d minio
   ```

2. Check MinIO is running:
   ```bash
   curl http://localhost:9000/minio/health/live
   ```

3. Access MinIO Console: http://localhost:9001

### Issue 5: Module Import Error

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solutions:**
1. Activate virtual environment:
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Health Checks

### Application Health

```bash
curl http://localhost:5000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "database": "connected",
  "api": "running"
}
```

### Database Health

```bash
docker exec -it postgres-tsi pg_isready -U hill
```

**Expected:** `accepting connections`

### MinIO Health

```bash
curl http://localhost:9000/minio/health/live
```

**Expected:** `200 OK`

---

## 🚢 Production Deployment

### Environment Variables

**Update `.env` for production:**

```bash
FLASK_ENV=production
FLASK_DEBUG=False
SESSION_COOKIE_SECURE=True

# Use strong random keys
JWT_SECRET_KEY=<64-char-random-string>
SECRET_KEY=<64-char-random-string>

# Update database URL
DATABASE_URL=postgresql://user:pass@prod-db:5432/fitness_tracker

# Update MinIO for cloud storage
MINIO_ENDPOINT=s3.amazonaws.com
MINIO_SECURE=True
```

### Using Gunicorn

```bash
pip install gunicorn

gunicorn -w 4 -b 0.0.0.0:5000 --timeout 120 run:app
```

### Using Docker

**Build image:**
```bash
docker build -t fitness-tracker-api .
```

**Run container:**
```bash
docker run -d \
  -p 5000:5000 \
  --env-file .env \
  --name fitness-api \
  fitness-tracker-api
```

### Security Checklist

- [ ] Change all default passwords
- [ ] Use HTTPS in production
- [ ] Enable CORS only for specific domains
- [ ] Set strong JWT secret keys
- [ ] Enable rate limiting
- [ ] Use environment-specific configs
- [ ] Enable database connection pooling
- [ ] Set up backup strategy
- [ ] Monitor logs and errors
- [ ] Use secrets management (AWS Secrets Manager, etc.)

---

## 📝 Default Credentials

### Admin User
- **Email:** `admin@fitness.com`
- **Password:** `Admin@123`

### Test User
- **Email:** `user@fitness.com`
- **Password:** `User@123`

### PgAdmin
- **URL:** `http://localhost:5050`
- **Email:** `admin@fitness.com`
- **Password:** `7zi844I9qHo`

### MinIO Console
- **URL:** `http://localhost:9001`
- **Username:** `minioadmin`
- **Password:** `minioadmin`

**⚠️ Change all default passwords before production deployment!**

---

## 📞 Support

### Common Commands Quick Reference

```bash
# Start development server
python run.py

# Create database tables
python create_tables.py

# Seed sample data
python seed_data.py

# Test database connection
python test_connection.py

# Generate secure keys
python generate_secrets.py

# Start Docker services
docker-compose up -d

# Stop Docker services
docker-compose down

# View logs
docker logs -f postgres-tsi

# Database shell
docker exec -it postgres-tsi psql -U hill -d fitness_tracker

# Check running containers
docker ps
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

---

## 🙏 Acknowledgments

- Flask framework
- Google Gemini AI
- PostgreSQL database
- MinIO object storage
- Docker containerization

---

**Built with ❤️ by [Your Name]**

**Last Updated:** January 2025

**Version:** 1.0.0