from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from app.domain.entities import SceneObjectType


class GeoReferenceInput(BaseModel):
    crs: str = "EPSG:4326"
    longitude: float | None = Field(default=None, ge=-180, le=180)
    latitude: float | None = Field(default=None, ge=-90, le=90)


class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=2000)
    georeference: GeoReferenceInput = Field(default_factory=GeoReferenceInput)


class SceneObjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    object_type: SceneObjectType
    position: tuple[float, float, float] = (0.0, 0.0, 0.0)
    rotation: tuple[float, float, float] = (0.0, 0.0, 0.0)
    scale: tuple[float, float, float] = (1.0, 1.0, 1.0)
    properties: dict = Field(default_factory=dict)


class SceneObjectRead(BaseModel):
    id: UUID
    name: str
    object_type: SceneObjectType
    position: tuple[float, float, float]
    rotation: tuple[float, float, float]
    scale: tuple[float, float, float]
    properties: dict


class ProjectRead(BaseModel):
    id: UUID
    name: str
    description: str
    created_at: datetime
    georeference: GeoReferenceInput
    scene_objects: list[SceneObjectRead]
