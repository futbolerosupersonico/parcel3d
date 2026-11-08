# Reconstruction module

**Responsibility:** ingest user imagery and produce scene observations.

Potential pipeline stages:
1. Upload validation and metadata extraction.
2. Image/video frame selection.
3. Feature matching and camera pose estimation.
4. Sparse and dense reconstruction.
5. Mesh / point-cloud generation.
6. Quality assessment and export.

Candidate tools for evaluation: COLMAP, Open3D and photogrammetry services.

The module must report coverage and confidence. Occluded or unobserved geometry must not be silently presented as measured reality. A photorealistic representation (for example, Gaussian splatting) may coexist with editable geometry; they are not interchangeable outputs.
