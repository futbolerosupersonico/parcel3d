# Scene module

**Responsibility:** assemble geospatial terrain, observed/reconstructed content and user-designed objects into a common scene.

The scene should keep three conceptual layers separate:
- `base`: terrain and authoritative source context.
- `observed`: buildings, surfaces and objects inferred from data or imagery.
- `design`: user-created or modified objects.

The scene module owns registration metadata and local-to-world transforms. It should not own the photogrammetry algorithm or the frontend renderer.
