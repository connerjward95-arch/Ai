.PHONY: help install dev prod build clean docker-up docker-down docker-logs

help:
	@echo "AI Learning Machine - Make Commands"
	@echo "==================================="
	@echo "make install      - Install all dependencies"
	@echo "make dev          - Run in development mode"
	@echo "make prod         - Run in production mode"
	@echo "make build        - Build for production"
	@echo "make clean        - Clean build artifacts"
	@echo "make docker-up    - Start Docker containers"
	@echo "make docker-down  - Stop Docker containers"
	@echo "make docker-logs  - View Docker logs"

install:
	@echo "Installing dependencies..."
	pip install -r backend/requirements.txt
	cd frontend && npm install && cd ..

dev:
	@echo "Starting development environment..."
	@echo "Backend: http://localhost:5000"
	@echo "Frontend: http://localhost:3000"
	@echo "Docs: http://localhost:5000/docs"

docker-up-dev:
	docker-compose -f docker-compose.dev.yml up -d

dev-backend:
	cd backend && python run.py

dev-frontend:
	cd frontend && npm start

prod:
	@echo "Starting production environment..."
	docker-compose up -d

build:
	@echo "Building frontend production assets..."
	cd frontend && npm install && npm run build

build-full:
	@echo "Building frontend production assets and validating backend..."
	cd frontend && npm install && npm run build
	python -m compileall backend/app backend/run.py

android-build:
	@echo "Building Android APK using Capacitor..."
	cd frontend && npm install && npm run android:build

probe:
	@echo "Building production images..."
	docker-compose build

clean:
	@echo "Cleaning build artifacts..."
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name *.pyc -delete
	rm -rf frontend/build
	rm -rf backend/dist

docker-up:
	docker-compose up -d
	@echo "Containers started:"
	@docker-compose ps

docker-down:
	docker-compose down
	@echo "Containers stopped"

docker-logs:
	docker-compose logs -f

docker-logs-backend:
	docker-compose logs -f backend

docker-logs-frontend:
	docker-compose logs -f frontend
