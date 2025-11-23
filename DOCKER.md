# Docker Deployment Guide

## Overview

The BMW Sales Analysis System can be run in Docker containers for consistent, reproducible deployments across different environments.

## Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.0+
- 4GB RAM minimum
- 10GB disk space

## Quick Start

### 1. Build Image
```bash
docker build -t bmw-sales-analysis:latest .
```

### 2. Run Container
```bash
docker-compose up bmw-analysis
```

## Docker Configuration

### Dockerfile

The `Dockerfile` creates a production-ready image:
- Base: Python 3.12-slim
- Dependencies: Compiled from `requirements.txt`
- Application code: Copied to `/app`
- Volumes: Mounted for data, reports, logs

### docker-compose.yml

Two services defined:

#### 1. Production Service (`bmw-analysis`)
```yaml
services:
  bmw-analysis:
    build: .
    volumes:
      - ./data-bmw:/app/data-bmw:ro
      - ./reports:/app/reports
      - ./logs:/app/logs
    env_file:
      - .env
```

#### 2. Development Service (`bmw-analysis-dev`)
```yaml
services:
  bmw-analysis-dev:
    build: .
    volumes:
      - .:/app  # Mount entire directory
    command: tail -f /dev/null  # Keep container running
    stdin_open: true
    tty: true
```

## Usage

### Production Mode

Run complete analysis:
```bash
docker-compose up bmw-analysis
```

View logs:
```bash
docker-compose logs -f bmw-analysis
```

### Development Mode

Start development container:
```bash
docker-compose up -d bmw-analysis-dev
```

Execute commands inside container:
```bash
docker-compose exec bmw-analysis-dev bash
python analyze_bmw_sales.py
```

Run tests in container:
```bash
docker-compose exec bmw-analysis-dev pytest
```

### One-off Commands

Run analysis once:
```bash
docker run --rm \
  -v $(pwd)/data-bmw:/app/data-bmw:ro \
  -v $(pwd)/reports:/app/reports \
  -v $(pwd)/logs:/app/logs \
  --env-file .env \
  bmw-sales-analysis:latest
```

Clean data:
```bash
docker run --rm \
  -v $(pwd)/data-bmw:/app/data-bmw \
  --env-file .env \
  bmw-sales-analysis:latest \
  python read_bmw_data.py
```

## Environment Variables

Pass environment variables via `.env` file:
```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key
GEMINI_MODEL=gemini-2.5-flash
LLM_TEMPERATURE=0.7
ROLE=Business Chief
```

Or override at runtime:
```bash
docker run --rm \
  -e LLM_PROVIDER=openai \
  -e OPENAI_API_KEY=your_key \
  bmw-sales-analysis:latest
```

## Volume Mounts

### Data Directory (Read-Only)
```
-v ./data-bmw:/app/data-bmw:ro
```
Mount input data as read-only to prevent accidental modification.

### Reports Directory (Read-Write)
```
-v ./reports:/app/reports
```
Reports are written here and persist after container stops.

### Logs Directory (Read-Write)
```
-v ./logs:/app/logs
```
Log files are written here for debugging.

## Building for Different Platforms

### Build for Linux AMD64
```bash
docker build --platform linux/amd64 -t bmw-sales-analysis:amd64 .
```

### Build for Linux ARM64
```bash
docker build --platform linux/arm64 -t bmw-sales-analysis:arm64 .
```

### Multi-platform Build
```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t bmw-sales-analysis:multi \
  --push .
```

## Resource Limits

Limit container resources:
```yaml
services:
  bmw-analysis:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '1'
          memory: 2G
```

## Networking

### Expose Ports (Future Web UI)
```yaml
services:
  bmw-analysis:
    ports:
      - "8080:8080"
```

### Custom Network
```yaml
networks:
  bmw-network:
    driver: bridge

services:
  bmw-analysis:
    networks:
      - bmw-network
```

## Health Checks

Add health check to docker-compose.yml:
```yaml
services:
  bmw-analysis:
    healthcheck:
      test: ["CMD", "python", "-c", "import sys; sys.exit(0)"]
      interval: 30s
      timeout: 10s
      retries: 3
```

## Cleanup

### Stop and Remove Containers
```bash
docker-compose down
```

### Remove Images
```bash
docker rmi bmw-sales-analysis:latest
```

### Clean All Docker Resources
```bash
docker system prune -a
```

## Troubleshooting

### Container Exits Immediately
Check logs:
```bash
docker-compose logs bmw-analysis
```

### Permission Errors
Ensure volumes have correct permissions:
```bash
chmod -R 755 data-bmw reports logs
```

### Out of Memory
Increase Docker memory limit in Docker Desktop settings.

### API Key Not Found
Verify `.env` file exists and contains valid keys:
```bash
cat .env | grep API_KEY
```

## Best Practices

1. **Use .dockerignore** - Exclude unnecessary files from build
2. **Layer caching** - Copy requirements.txt before code for better caching
3. **Non-root user** - Run container as non-root (future improvement)
4. **Read-only volumes** - Mount data as read-only when possible
5. **Resource limits** - Set appropriate CPU and memory limits
6. **Health checks** - Monitor container health
7. **Logging** - Use structured logging for container environments

## Production Deployment

### Docker Swarm
```bash
docker stack deploy -c docker-compose.yml bmw-analysis
```

### Kubernetes
Convert to Kubernetes manifests:
```bash
kompose convert -f docker-compose.yml
kubectl apply -f .
```

### CI/CD Integration
See `.github/workflows/ci.yml` for automated Docker builds.
