#!/bin/bash

echo "🚀 AI Learning Machine - Setup Script"
echo "======================================="
echo ""

# Check Python
echo "📌 Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi
echo "✅ Python $(python3 --version) found"

# Check Node
echo "📌 Checking Node.js..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed"
    exit 1
fi
echo "✅ Node $(node --version) found"

# Create virtual environment
echo ""
echo "📌 Setting up Python environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null

# Install Python dependencies
echo "📌 Installing Python dependencies..."
pip install --upgrade pip
pip install -r backend/requirements.txt
echo "✅ Python dependencies installed"

# Install Node dependencies
echo "📌 Installing Node dependencies..."
cd frontend
npm install
cd ..
echo "✅ Node dependencies installed"

# Copy environment files
echo "📌 Setting up environment files..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ .env file created"
else
    echo "✅ .env file already exists"
fi

if [ ! -f "frontend/.env" ]; then
    cp frontend/.env.example frontend/.env
    echo "✅ frontend/.env file created"
else
    echo "✅ frontend/.env file already exists"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎉 Next steps:"
echo "1. Update .env file with your configuration"
echo "2. Start backend: cd backend && python run.py"
echo "3. Start frontend: cd frontend && npm start"
echo "4. Open http://localhost:3000 in your browser"
echo ""
echo "📚 Documentation: See QUICK_START.md"
