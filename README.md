# Restaurant POS Backend (FastAPI Learning Project

A production-grade FastAPI backend for a Restaurant POS system — designed as a complete hands-on learning journey from beginner → advanced.
Covers authentication, async DB, WebSockets, background jobs, testing, deployment, and observability.

### Core features (each maps to important FastAPI concepts):
- User & Role Auth — JWT, OAuth2 password flow, roles (admin/staff/waiter).
- Menu & Categories — CRUD, validation (Pydantic), relationships.
- Orders — create, update, order status, realtime updates (WebSocket for kitchen display).
- Payments — background tasks (simulate payment processing), webhooks.
- Inventory — transactions, optimistic concurrency handling.
- Reporting — background jobs, CSV / PDF export endpoints.
- Admin APIs — pagination, filtering, sorting, bulk imports.
- Docs & OpenAPI — custom schemas, examples, security schemes.
- Testing & CI — pytest unit & integration tests; coverage.
- Deployment — Docker, compose, nginx reverse proxy, systemd or cloud deploy; logs & monitoring.
- Observability — structured logging, metrics endpoint (Prometheus), error tracking.
- Rate limiting & throttling — protect public endpoints.
- Database — async DB usage (Postgres), migrations (Alembic), connection pooling.
- Best practices — dependency injection, services layer, DTOs, validation, consistent error handling.

This project will expose you to nearly every FastAPI concept used in production.

### Suggested tech stack
| Category   | Technology                                      |
| ---------- | ----------------------------------------------- |
| Language   | Python 3.12+                                    |
| Framework  | [FastAPI](https://fastapi.tiangolo.com)         |
| Database   | PostgreSQL (with SQLAlchemy Async / SQLModel)   |
| Migrations | Alembic                                         |
| Testing    | Pytest, HTTPX / TestClient                      |
| Deployment | Docker, Docker Compose, Nginx, Gunicorn/Uvicorn |
| Monitoring | Prometheus, Logging, Metrics                    |
| Auth       | OAuth2 + JWT (roles: admin, staff, waiter)      |

### Learning Goal
By the end of this journey, you’ll:
- ✅ Understand how FastAPI works under the hood (routing, dependency injection, async, middleware).
- ✅ Build a real production-grade backend for a Restaurant POS system.
- ✅ Learn to use SQLAlchemy / Pydantic / JWT / Docker / CI / Testing.
- ✅ Deploy your app like a pro (Docker + Nginx + Uvicorn + PostgreSQL).

### Setup and Run
```bash
# Clone repository
git clone https://github.com/<your-username>/restaurant-pos-backend.git
cd restaurant-pos-backend
```

```bash
# Create virtual environment
python -m venv venv        # python3 -m venv venv on Linux
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

```bash
# Install dependencies
pip install -r requirements.txt    # pip3 on Linux
```

```bash
# Run app
uvicorn app.main:app --reload
```

## Roadmap (task-based, from basics → advanced)
### Module 0 — Getting Started
- Create venv, install fastapi[standard], uvicorn, pytest, httpx. Create Git repo.
- Exercise: make a single-file main.py with a /health endpoint and run with uvicorn main:app --reload.

### Module 1 — Routing & Models
- Learn routing, path & query params, request bodies, responses.
- Pydantic models and validation.
- Auto docs: Swagger UI / Redoc.
- Exercise: CRUD endpoints for MenuItem (in-memory dict or simple SQLite).

### Module 2 — Database Integration
- Move to Postgres (or SQLite for dev). Integrate SQLAlchemy async or SQLModel. Add Alembic migrations.
- Project structure: app/main.py, app/api/, app/models/, app/schemas/, app/services/.
- Exercise: Implement Category and MenuItem DB models with relations, add pagination.
- Docs: [Bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications) guide for structuring.

### Module 3 — Authentication
- OAuth2 password flow, JWT, password hashing (bcrypt), role checks via dependencies.
- Secure docs with API key/JWT where needed.
- Exercise: Login endpoint that returns JWT; restrict create/update to admin.

### Module 4 — Async & Background Tasks
- Convert DB access to async; understand when to use async def and when to keep sync.
- Implement background tasks for long-running jobs (e.g., sending email or processing payment).
- Implement a WebSocket endpoint for real-time order updates to kitchen display.
- Exercise: Background job that marks unpaid orders after X minutes and emits an event via WebSocket.

### Module 5 — Middleware & Error Handling
- Custom middleware (timing, request ID), centralized exception handlers, structured logging.
- Exercise: Add middleware to log request duration and return `X-Request-ID`.

### Module 6 — Testing
- Unit tests for services, integration tests for endpoints using TestClient / httpx + pytest.
- Mock external services (payment gateway), use fixtures for DB setup/teardown.
- Add GitHub Actions to run tests and linting.
- Exercise: Write tests for login and order lifecycle. [Docs](https://fastapi.tiangolo.com/tutorial/testing)

### Module 7 — Docker & Deployment
- Dockerize app, use multi-stage build, add docker-compose with Postgres.
- Deploy locally behind Nginx. Add systemd or cloud deployment instructions.
- Exercise: Create Dockerfile and docker-compose.yml and deploy locally.

### Module 8 — Observability & Scaling (Optional)
- Add Prometheus metrics endpoint, structured logs, Sentry (or similar) error tracking.
- Horizontal scale advice: run multiple Uvicorn workers, use Nginx for slow clients.
- Exercise: Expose a /metrics endpoint and test scraping.

### Module 9 — Advanced & Final Project
- GraphQL with FastAPI (strawman), background scheduler (APScheduler), CQRS/event sourcing patterns, rate limiting, API versioning. (Optional)
- Add RBAC, export reports, audit logs.
- Read community best-practice repo for conventions.

## Contributing
Feel free to fork this repo and open PRs — this project is meant to be educational and community-driven.
If you improve a module or add a feature, document it and submit a pull request.
