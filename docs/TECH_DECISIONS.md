# Technical decisions (provisional)

| Topic | Initial direction | Rationale / status |
|---|---|---|
| Backend | Python + FastAPI | Familiar ecosystem; quick API iteration |
| Frontend | React + TypeScript | Modular component model and typed contracts |
| 2D map | MapLibre GL JS | Web map rendering with flexible data sources |
| 3D viewer | Three.js | Browser-native 3D rendering |
| Spatial database | PostgreSQL + PostGIS | Mature spatial storage and querying; not integrated yet |
| Raster processing | GDAL / Rasterio | Standard geospatial processing ecosystem |
| Point clouds | PDAL / Open3D | Candidate tools; evaluate against data needs |
| Reconstruction | COLMAP | Candidate photogrammetry pipeline; not integrated yet |
| Asset format | GLB/glTF | Practical interchange format for web 3D assets |

These are working hypotheses, not irreversible commitments. Record benchmarks and integration findings before locking major choices.
