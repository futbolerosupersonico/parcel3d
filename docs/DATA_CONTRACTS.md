# Initial data contracts

## Project

- `id`: UUID
- `name`: human-readable project name
- `description`: optional description
- `created_at`: UTC timestamp
- `georeference`: CRS and optional geographic anchor
- `scene_objects`: user-editable objects

## Scene object

- `id`: UUID
- `name`: display name
- `object_type`: controlled enum
- `position`: local scene coordinates `(x, y, z)`
- `rotation`: Euler angles `(x, y, z)`; convention to be fixed with the renderer
- `scale`: dimensionless scale factors
- `properties`: type-specific parameters

## Geospatial metadata (planned)

Every imported dataset should carry:
- provider and dataset identifier
- acquisition/publication date where available
- horizontal CRS and vertical datum where known
- resolution / point density where applicable
- licence and attribution requirements
- processing history

## Coordinate policy

Do not mix longitude/latitude degrees with local metric scene coordinates. A dedicated geospatial transformation service must define the project-local origin and conversion rules before real geometry is added.
