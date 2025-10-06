# FastAPI Project

> A concise, production-ready FastAPI template with instructions to test locally, deploy, and maintain the service.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Requirements](#requirements)
* [Getting Started](#getting-started)

  * [Install dependencies](#install-dependencies)
  * [Run locally (Test locally)](#run-locally-test-locally)
  * [Interactive API docs](#interactive-api-docs)
* [Configuration & Environment Variables](#configuration--environment-variables)
* [Testing](#testing)

  * [Unit tests](#unit-tests)
  * [Integration tests](#integration-tests)
  * [Test coverage](#test-coverage)
* [Linting & Formatting](#linting--formatting)
* [Type Checking](#type-checking)
* [Security Considerations](#security-considerations)
* [Logging & Monitoring](#logging--monitoring)
* [Deployment](#deployment)

  * [Docker (recommended)](#docker-recommended)
  * [Gunicorn + Uvicorn (Linux)](#gunicorn--uvicorn-linux)
  * [Heroku](#heroku)
  * [AWS Elastic Beanstalk / ECS / EKS (high-level)](#aws-elastic-beanstalk--ecs--eks-high-level)
* [CI/CD Example (GitHub Actions)](#cicd-example-github-actions)
* [Development workflow](#development-workflow)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## Project Overview

A FastAPI project scaffold for building RESTful APIs. This README explains how to run the app locally, test it, deploy it with Docker or other platforms, and follow best practices for development and production.

---

## Features

* FastAPI-based endpoints
* Automatic OpenAPI docs (Swagger UI + ReDoc)
* Async-friendly endpoints
* pydantic models for data validation
* Example database integration (Postgres) via SQLAlchemy or async ORM
* Dockerfile and docker-compose
* Tests with pytest
* CI/CD sample with GitHub Actions

---

## Requirements

* Python 3.10+ (adjust based on your project)
* pip or poetry
* Docker (for containerized local testing and deployment)

---

## Getting Started

### Install dependencies

Using pip and a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.\.venv\Scripts\activate   # Windows (PowerShell)

pip install --upgrade pip
pip install -r requirements.txt
```

If you use Poetry:

```bash
poetry install
poetry shell
```

### Run locally (Test locally)

Use Uvicorn (development):

```bash
# from repository root
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Notes:

* `--reload` enables auto-reload on code changes (dev only).
* `app.main` assumes your FastAPI instance is in `app/main.py` as `app = FastAPI()`.

Test the app with `curl` or HTTP client:

```bash
curl http://localhost:8000/health
# or an endpoint that expects JSON
curl -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"name":"example","price":9.99}'
```

### Interactive API docs

FastAPI provides interactive docs out-of-the-box:

* Swagger UI: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`

---

## Configuration & Environment Variables

Store secrets and configuration outside source control. Example `.env` variables:

```env
# .env
APP_ENV=development
SECRET_KEY=replace-with-secure-value
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/dbname
PORT=8000
```

Use `python-dotenv` or `pydantic.BaseSettings` to load them in your app.

Example with Pydantic settings:

```py
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
```

---

## Testing

This project uses `pytest` for tests. Keep tests under `tests/`.

### Unit tests

Run unit tests locally:

```bash
pytest tests/unit -q
```

### Integration tests

Integration tests often require external services (DB). Use `docker-compose` or test containers to spin up a temporary Postgres instance.

Example using docker-compose for tests:

```bash
docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit
```

### Test coverage

Generate a coverage report with `pytest-cov`:

```bash
pytest --cov=app --cov-report=term-missing
```

Aim for meaningful coverage but prioritize testing critical logic and edge cases.

---

## Linting & Formatting

Recommended tools:

* `black` for formatting
* `isort` for import sorting
* `flake8` or `ruff` for linting

Example commands:

```bash
black .
isort .
flake8
# or ruff check .
```

Add pre-commit hooks to enforce style automatically:

```bash
pip install pre-commit
pre-commit install
```

---

## Type Checking

Use `mypy` to check static types (especially when mixing async code and ORMs):

```bash
mypy app
```

---

## Security Considerations

* Never commit secrets to version control.
* Use HTTPS in production (TLS termination at load balancer or reverse proxy).
* Validate and sanitize all inputs with pydantic models.
* Limit response data to avoid leaking sensitive fields.
* Use proper CORS configuration (only allow origins you trust).
* Keep dependencies up-to-date and scan for vulnerabilities (e.g. `pip-audit`).

---

## Logging & Monitoring

* Use the standard `logging` module. Configure logging handlers for stdout (Docker) and persistent logs.
* Consider structured logging (JSON) for easier parsing in log aggregators.
* Integrate with monitoring and tracing (Prometheus, Grafana, Sentry, OpenTelemetry).

Example simple logger:

```py
import logging

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.INFO)
```

---

## Deployment

### Docker (recommended)

**Dockerfile (example):**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

ENV PORT=8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
```

**docker-compose.yml (example for local dev):**

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: dbname
    ports:
      - "5432:5432"
```

Build and run:

```bash
docker compose up --build
```

### Gunicorn + Uvicorn (Linux)

For higher concurrency and process management, use Gunicorn with Uvicorn workers.

Example command:

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app -w 4 -b 0.0.0.0:8000 --limit-request-line 0
```

Adjust worker count (`-w`) according to CPU cores and memory.

### Heroku

1. Create a `Procfile`:

```
web: gunicorn -k uvicorn.workers.UvicornWorker app.main:app
```

2. Push to Heroku and set environment variables using `heroku config:set`.

### AWS Elastic Beanstalk / ECS / EKS (high-level)

* Use Docker image pushed to ECR for ECS/EKS or Zip for Elastic Beanstalk.
* Use load balancers and autoscaling groups.
* Manage configuration through environment variables, Secrets Manager, and IAM roles.

---

## CI/CD Example (GitHub Actions)

`.github/workflows/ci.yml` (simplified):

```yaml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest --cov=app
```

Add deployment job on `push` to `main` to build Docker image and push to registry or trigger deployment.

---

## Development workflow

* Create a feature branch: `git checkout -b feat/short-description`
* Open a pull request against `main`.
* Ensure tests pass and linters are green.
* Use small, focused commits and clear PR descriptions.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact
