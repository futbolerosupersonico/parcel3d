# Parcel3D

**Status:** early-stage software prototype.

Parcel3D is a modular web platform concept for turning a real-world parcel into an editable 3D environment. The intended workflow combines public geospatial data, user-provided imagery, reconstructed scene content, and parametric design objects.

This repository is an initial engineering scaffold. It demonstrates the proposed module boundaries and a small working API; it does **not** yet connect to cadastral services, process photogrammetry, or render a production 3D scene.

## Current prototype

- FastAPI application with versioned REST endpoints.
- Domain entities for projects and editable scene objects.
- Application services separated from HTTP routes.
- In-memory repository adapter for local development.
- Basic automated tests.
- Architecture and data-contract notes.

## Quick start

Requires Python 3.11+.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

Run tests:

```bash
pytest
```

## API

- `GET /health`
- `POST /api/v1/projects`
- `GET /api/v1/projects`
- `GET /api/v1/projects/{project_id}`
- `POST /api/v1/projects/{project_id}/scene-objects`
- `DELETE /api/v1/projects/{project_id}/scene-objects/{object_id}`

## Repository layout

```text
app/
  api/             HTTP routes and request/response schemas
  application/     Use cases and orchestration
  domain/          Core entities and business rules
  infrastructure/  Repository adapters and external integrations
  modules/         Boundaries for future geospatial and scene capabilities
docs/              Architecture, contracts and roadmap
tests/             Automated tests
```

## Planned development

1. Replace in-memory persistence with PostgreSQL/PostGIS.
2. Add provider adapters for parcel boundaries, orthophotos and elevation data.
3. Define explicit coordinate reference and local-scene transformation contracts.
4. Build a web client using React, TypeScript, MapLibre and Three.js.
5. Add an image-ingestion and photogrammetry pipeline.
6. Add a parametric library for pools, terraces, paths, walls, pergolas and vegetation.

## Engineering principles

- Keep domain logic independent from web frameworks and data providers.
- Communicate across modules through explicit contracts.
- Keep source geospatial data, reconstructed observations and design objects as distinct scene layers.
- Treat approximate visual reconstruction separately from survey-grade measurement.
- Prefer incremental, testable modules over a monolithic implementation.
