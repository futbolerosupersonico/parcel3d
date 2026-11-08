from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class SceneObjectType(str, Enum):
    TREE = "tree"
    SHRUB = "shrub"
    POOL = "pool"
    TERRACE = "terrace"
    PERGOLA = "pergola"
    WALL = "wall"
    PATH = "path"
    GENERIC = "generic"


@dataclass(frozen=True)
class GeoReference:
    """Geographic anchor. Coordinate transformations belong to the geospatial module."""

    crs: str = "EPSG:4326"
    longitude: float | None = None
    latitude: float | None = None


@dataclass
class SceneObject:
    name: str
    object_type: SceneObjectType
    position: tuple[float, float, float] = (0.0, 0.0, 0.0)
    rotation: tuple[float, float, float] = (0.0, 0.0, 0.0)
    scale: tuple[float, float, float] = (1.0, 1.0, 1.0)
    properties: dict = field(default_factory=dict)
    id: UUID = field(default_factory=uuid4)


@dataclass
class ParcelProject:
    name: str
    description: str = ""
    georeference: GeoReference = field(default_factory=GeoReference)
    scene_objects: list[SceneObject] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def add_scene_object(self, scene_object: SceneObject) -> None:
        self.scene_objects.append(scene_object)

    def remove_scene_object(self, object_id: UUID) -> bool:
        for index, item in enumerate(self.scene_objects):
            if item.id == object_id:
                del self.scene_objects[index]
                return True
        return False
