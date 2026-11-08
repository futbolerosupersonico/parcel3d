# Geospatial module

**Responsibility:** parcel lookup, coordinate reference systems, terrain and public geospatial data providers.

Planned adapters:
- Parcel boundary provider (national or regional cadastral source).
- Orthophoto provider.
- Elevation provider (DTM/DSM and point-cloud products).

Rules:
- Keep provider-specific API details inside adapters.
- Return normalized domain contracts.
- Record source, acquisition date, CRS and resolution as metadata.
- Never label cadastral cartography as a legally verified boundary.
- Do not assume EPSG:4326 is suitable for metric geometry operations; select an appropriate projected CRS per area.
