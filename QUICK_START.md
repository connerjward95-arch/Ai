# Quick Start Guide - AI Learning Machine

## Prerequisites

- Python 3.9+ 
- Node.js 16+
- PostgreSQL 13+
- Redis 6+

## Option 1: Local Development Setup (Recommended for Development)

### Step 1: Clone & Setup

```bash
git clone https://github.com/connerjward95-arch/Ai.git
cd Ai
```

### Step 2: Setup Backend

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Copy environment file
cp .env.example .env
```

### Step 3: Setup Frontend

```bash
cd frontend
npm install
cp .env.example .env
cd ..
```

### Step 4: Start Services

**Terminal 1 - Start Backend:**
```bash
cd backend
python run.py
```
Backend runs at: `http://localhost:5000`
API Docs: `http://localhost:5000/docs`

**Terminal 2 - Start Frontend:**
```bash
cd frontend
npm start
```
Frontend runs at: `http://localhost:3000`

## Option 2: Docker Setup (Recommended for Production)

### Prerequisites
- Docker & Docker Compose

### Step 1: Start Everything

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f
```

Services will be available at:
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:5000`
- API Docs: `http://localhost:5000/docs`
- PostgreSQL: `localhost:5432`
- Redis: `localhost:6379`

### Step 2: Stop Services

```bash
docker-compose down
```

## Using Make Commands (Optional)

```bash
# Install dependencies
make install

# Start development with Docker databases
make docker-up-dev

# View help
make help
```

## Testing the Application

### Chat Interface
1. Open `http://localhost:3000` in your browser
2. Type a message in the chat box
3. Press Enter or click Send button
4. AI responds in real-time

### View Dashboard
1. Click "Dashboard" tab
2. View learning metrics and progress
3. See interaction statistics

### Configure Settings
1. Click "Settings" tab
2. Adjust AI model type
3. Configure learning rate
4. Save preferences

## API Endpoints

### Chat
- `POST /api/v1/chat` - Send message
- `GET /api/v1/chat/history` - Get chat history
- `POST /api/v1/chat/clear` - Clear history

### Analytics
- `GET /api/v1/analytics/stats` - Get statistics

### Models
- `GET /api/v1/models` - List models
- `POST /api/v1/models/select` - Select model

## Troubleshooting

### Backend Won't Start
```bash
# Clear Python cache
find . -type d -name __pycache__ -exec rm -rf {} +

# Reinstall requirements
pip install --upgrade --force-reinstall -r backend/requirements.txt

# Check if port 5000 is in use
lsof -i :5000
```

### Frontend Won't Start
```bash
# Clear npm cache
cd frontend
rm -rf node_modules package-lock.json
npm install
npm start
```

### Database Connection Issues
```bash
# Check PostgreSQL is running
psql -U user -d ai_learning_machine

# Check Redis is running
redis-cli ping
```

## Environment Variables

Edit `.env` file:

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ai_learning_machine
REDIS_URL=redis://localhost:6379/0

# AI Configuration
AI_MODEL_TYPE=advanced
LEARNING_RATE=0.8

# API
CORS_ORIGINS=http://localhost:3000
LOG_LEVEL=INFO
```

## Project Structure

```
AI/
├── backend/              # Python FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api/          # REST routes & WebSocket
│   │   ├── ai/           # AI Engine
│   │   ├── services/     # Business logic
│   │   ├── config.py     # Configuration
│   │   └── database.py   # Database setup
│   ├── requirements.txt   # Python dependencies
│   ├── run.py            # Entry point
│   └── Dockerfile        # Docker configuration
├── frontend/             # React TypeScript frontend
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Page components
│   │   ├── hooks/        # Custom hooks
│   │   └── App.tsx       # Main app
│   ├── package.json      # npm dependencies
│   ├── tsconfig.json     # TypeScript config
│   └── Dockerfile        # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .env.example          # Environment template
└── README.md             # Documentation
```

## Next Steps

1. **Customize AI Model**: Edit `backend/app/ai/engine.py`
2. **Add New Features**: Create new routes in `backend/app/api/routes.py`
3. **Style Frontend**: Modify CSS files in `frontend/src`
4. **Deploy**: Use Docker Compose or cloud provider

## Support

For issues or questions:
1. Check troubleshooting section above
2. Review console logs
3. Open issue on GitHub

## Performance Tips

- Use `advanced` model for better accuracy
- Increase `LEARNING_RATE` for faster learning
- Use Docker for production deployment
- Enable Redis caching for faster responses

Happy Learning! 🚀
