@echo off
echo ========================================
echo AI Learning Machine - Setup Script
echo ========================================
echo.

REM Check Python
echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python 3 is not installed
    exit /b 1
)
echo Python found

REM Check Node
echo Checking Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo Node.js is not installed
    exit /b 1
)
echo Node.js found

REM Create virtual environment
echo.
echo Setting up Python environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install Python dependencies
echo Installing Python dependencies...
pip install --upgrade pip
pip install -r backend\requirements.txt
echo Python dependencies installed

REM Install Node dependencies
echo Installing Node dependencies...
cd frontend
call npm install
cd ..
echo Node dependencies installed

REM Copy environment files
echo Setting up environment files...
if not exist ".env" (
    copy .env.example .env
    echo .env file created
) else (
    echo .env file already exists
)

if not exist "frontend\.env" (
    copy frontend\.env.example frontend\.env
    echo frontend\.env file created
) else (
    echo frontend\.env file already exists
)

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Update .env file with your configuration
echo 2. Start backend: cd backend ^&^& python run.py
echo 3. Start frontend: cd frontend ^&^& npm start
echo 4. Open http://localhost:3000 in your browser
echo.
echo Documentation: See QUICK_START.md
