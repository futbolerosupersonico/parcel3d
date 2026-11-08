# Visualization module

**Responsibility:** render the scene and provide camera/navigation controls.

Candidate web stack:
- React + TypeScript
- MapLibre GL JS for 2D geospatial context
- Three.js / React Three Fiber for 3D rendering

The renderer consumes scene contracts; it must not contain domain rules for parcel acquisition, reconstruction or object pricing. Consider 3D Tiles only when scene scale justifies it.
