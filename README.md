# AI Learning Machine with Web Capabilities

A full-featured, interactive AI learning machine built with Python, featuring continuous learning capabilities, web interface, and real-time interaction. This system enables persistent learning, conversation memory, and adaptive behavior.

## Features

- **🤖 Intelligent AI Engine** - Advanced machine learning with continuous learning capabilities
- **💬 Interactive Conversations** - Real-time bidirectional communication with persistent memory
- **🌐 Web Interface** - Modern, responsive UI for seamless interaction
- **📚 Continuous Learning** - AI learns from interactions and improves over time
- **💾 Memory Management** - Maintains conversation history and learning context
- **🔄 Adaptive Responses** - Learns user patterns and preferences
- **⚙️ Configurable Models** - Support for multiple AI models and fine-tuning
- **📊 Analytics Dashboard** - Track learning progress and interaction metrics

## Architecture

```
AI Learning Machine (Python)
├── Backend (FastAPI)
│   ├── API Server
│   ├── AI Engine (TensorFlow/PyTorch)
│   ├── Memory Management
│   ├── Learning Module
│   └── WebSocket Server
├── Frontend (React/TypeScript)
│   ├── Interactive Chat Interface
│   ├── Real-time Updates
│   └── Dashboard & Analytics
└── Database
    ├── PostgreSQL (structured data)
    ├── Redis (caching & sessions)
    └── Vector DB (embeddings)
```

## Tech Stack

### Backend
- **FastAPI** - Modern async web framework
- **TensorFlow/PyTorch** - Deep learning models
- **SQLAlchemy** - ORM for database
- **Redis** - In-memory data store
- **Pydantic** - Data validation
- **WebSockets** - Real-time communication

### Frontend
- **React** - UI framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Recharts** - Data visualization

### Database
- **PostgreSQL** - Primary database
- **Redis** - Cache layer
- **Pinecone/Milvus** - Vector storage for embeddings

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Redis 6+

### Installation

1. Clone the repository
```bash
git clone https://github.com/connerjward95-arch/Ai.git
cd Ai
```

2. Set up Python virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies
```bash
pip install -r backend/requirements.txt
```

4. Install frontend dependencies
```bash
cd frontend && npm install && cd ..
```

5. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

6. Start the application
```bash
# Terminal 1: Backend
cd backend && python run.py

# Terminal 2: Frontend
cd frontend && npm start
```

## Project Structure

```
AI/
├── backend/
│   ├── app/
│   │   ├── __init__.py          # FastAPI app initialization
│   │   ├── config.py            # Configuration management
│   │   ├── database.py          # Database setup
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py        # REST API endpoints
│   │   │   └── websocket.py     # WebSocket handlers
│   │   ├── ai/
│   │   │   ├── __init__.py
│   │   │   ├── engine.py        # AI Engine
│   │   │   ├── models.py        # Model definitions
│   │   │   └── learning.py      # Learning logic
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── chat_service.py
│   │   │   └── analytics_service.py
│   │   └── models/              # Database models
│   ├── requirements.txt         # Python dependencies
│   └── run.py                   # Entry point
├── frontend/
│   ├── src/
│   │   ├── components/          # React components
│   │   ├── pages/               # Page components
│   │   ├── hooks/               # Custom hooks
│   │   ├── config/              # API config
│   │   ├── App.tsx              # Main app
│   │   └── index.tsx            # React entry
│   ├── public/                  # Static files
│   └── package.json             # Dependencies
└── .env.example                 # Environment template
```

## Usage

### Interactive Chat

1. Start both backend and frontend servers
2. Open http://localhost:3000 in your browser
3. Type messages to interact with the AI
4. View analytics in the Dashboard tab
5. Configure settings in Settings tab

### API Endpoints

#### Chat Operations
- `POST /api/v1/chat` - Send a message to the AI
- `GET /api/v1/chat/history` - Get conversation history
- `POST /api/v1/chat/clear` - Clear chat history
- `WS /api/v1/ws/chat` - WebSocket for real-time chat

#### Learning & Analytics
- `POST /api/v1/learn/update` - Update AI learning
- `GET /api/v1/analytics/stats` - Get statistics

#### Models
- `GET /api/v1/models` - List available models
- `POST /api/v1/models/select` - Select active model

## Configuration

Edit `.env` to customize:

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost/ai_db
REDIS_URL=redis://localhost:6379/0

# AI Configuration
AI_MODEL_TYPE=advanced
LEARNING_RATE=0.8
MAX_MEMORY_CAPACITY=1000
RESPONSE_TIMEOUT_MS=5000

# API
CORS_ORIGINS=http://localhost:3000
LOG_LEVEL=INFO
```

## Features in Detail

### Continuous Learning

The AI system continuously learns from interactions:
- Analyzes user preferences and patterns
- Updates models based on feedback
- Improves response accuracy over time
- Adapts to user communication style

### Memory System

- **Short-term**: Current conversation context
- **Long-term**: Historical interactions (persistent)
- **Semantic**: Vector embeddings for meaning
- **Pattern Recognition**: Identifies behavior trends

### Web Capabilities

- Real-time WebSocket communication
- RESTful API for all operations
- Async/await for non-blocking operations
- Progressive Web App support
- Responsive design for all devices

## Development

### Run in Development Mode

```bash
# Backend with auto-reload
cd backend && python run.py

# Frontend in dev server (new terminal)
cd frontend && npm start
```

### Run Tests

```bash
# Backend tests
cd backend && pytest

# Frontend tests
cd frontend && npm test
```

### Build for Production

```bash
# Backend
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Frontend
cd frontend && npm run build
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, open an issue on GitHub.

## Roadmap

- [ ] Multi-language NLP support
- [ ] Advanced context understanding
- [ ] Voice interaction support
- [ ] Mobile app integration
- [ ] Cloud deployment (AWS/Azure)
- [ ] Advanced analytics dashboard
- [ ] Custom model training UI
- [ ] Third-party API integrations
- [ ] Federated learning support
- [ ] Model compression & optimization

## Acknowledgments

- Built with FastAPI, React, TensorFlow/PyTorch
- Inspired by modern conversational AI systems
- Community contributions and feedback

---

**Last Updated:** May 29, 2026
