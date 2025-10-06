# Flask Project

> A clean, production-ready Flask project template with sections for local testing, deployment, and development best practices.

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
* [Linting & Formatting](#linting--formatting)
* [Logging & Monitoring](#logging--monitoring)
* [Deployment](#deployment)

  * [Docker (recommended)](#docker-recommended)
  * [Gunicorn (Linux)](#gunicorn-linux)
  * [Heroku](#heroku)
  * [AWS Elastic Beanstalk / ECS / EKS](#aws-elastic-beanstalk--ecs--eks)
* [CI/CD Example (GitHub Actions)](#cicd-example-github-actions)
* [Development workflow](#development-workflow)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## Project Overview

A Flask-based RESTful API project template built for scalability and maintainability. This README covers local testing, configuration, deployment, and development workflow.

---

## Features

* REST API built with Flask
* Blueprints for modular structure
* Environment-based configuration
* SQLAlchemy ORM and migrations (via Flask-Migrate)
* Testing with pytest
* Docker and docker-compose setup
* CI/CD example (GitHub Actions)

---

## Requirements

* Python 3.10+
* pip or poetry
* Docker (optional but recommended)

---

## Getting Started

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows

pip install --upgrade pip
pip install -r requirements.txt
```

### Run locally (Test locally)

```bash
export FLASK_APP=app:create_app
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

Test the app using curl or Postman:

```bash
curl http://localhost:5000/health
```

### Interactive API docs

For APIs built with `flasgger` or `apispec`, access the Swagger UI:

* Swagger UI: `http://localhost:5000/apidocs`

---

## Configuration & Environment Variables

Example `.env` file:

```env
FLASK_ENV=development
SECRET_KEY=supersecret
SQLALCHEMY_DATABASE_URI=postgresql://user:password@localhost:5432/dbname
DEBUG=True
```

Example configuration structure:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
```

---

## Testing

Use pytest for unit and integration testing.

```bash
pytest -v --cov=app
```

Example structure:

```
app/
 ├── __init__.py
 ├── routes.py
 └── models.py
tests/
 ├── test_routes.py
 └── conftest.py
```

---

## Linting & Formatting

Recommended tools:

* `black` for formatting
* `flake8` or `ruff` for linting

```bash
black .
flake8
```

Add pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
```

---

## Logging & Monitoring

Enable structured logging:

```python
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)
```

Integrate with tools like Sentry or Prometheus for observability.

---

## Deployment

### Docker (recommended)

**Dockerfile**

```dockerfile
FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV FLASK_APP=app:create_app
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]
```

**docker-compose.yml**

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
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

Run locally:

```bash
docker compose up --build
```

### Gunicorn (Linux)

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:create_app()
```

### Heroku

Add a `Procfile`:

```
web: gunicorn app:create_app()
```

Deploy to Heroku and configure environment variables.

### AWS Elastic Beanstalk / ECS / EKS

* Build Docker image and push to ECR.
* Configure load balancer and scaling.
* Manage secrets via AWS Secrets Manager.

---

## CI/CD Example (GitHub Actions)

```yaml
name: Flask CI
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run tests
        run: pytest --cov=app
```

---

## Development workflow

1. Create a branch: `git checkout -b feature/new-endpoint`
2. Write or update tests.
3. Format and lint code.
4. Submit PR to `main`.

---

## License

This project is licensed under the MIT License.

---

## Contact

Author: Landneyker Betancourth