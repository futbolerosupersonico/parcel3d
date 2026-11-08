# Architecture overview

## Architectural style

The initial backend follows a lightweight layered architecture:

- **Domain:** entities and repository abstractions.
- **Application:** use cases and orchestration.
- **Infrastructure:** persistence and external-system adapters.
- **API:** transport layer, validation and HTTP mapping.

The `app/modules/` directory documents future capability boundaries. These are not yet independently deployable services.

## Target capability map

| Module | Owns | Must not own |
|---|---|---|
| Geospatial | Parcel and terrain providers, CRS operations | 3D editor UI |
| Reconstruction | Image processing and reconstruction pipeline | Parcel business rules |
| Scene | Layer composition and transforms | Rendering implementation |
| Editor | Design-object lifecycle and parameters | Source-data ingestion |
| Visualization | 2D/3D presentation | Persistence and domain decisions |
| Project data | Project lifecycle and asset references | Reconstruction algorithms |

## Dependency direction

HTTP routes call application services. Application services depend on domain contracts. Infrastructure implements those contracts. Domain code must not import FastAPI, database drivers, GIS providers or rendering libraries.

## First implementation trade-offs

The repository uses an in-memory adapter to keep the prototype runnable without external services. It is intentionally replaceable. The next persistence implementation should use PostgreSQL/PostGIS behind the same repository contract.
