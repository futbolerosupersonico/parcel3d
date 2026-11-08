from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_project_service
from app.api.schemas import (
    GeoReferenceInput,
    ProjectCreate,
    ProjectRead,
    SceneObjectCreate,
)
from app.application.project_service import ProjectNotFoundError, ProjectService
from app.domain.entities import GeoReference, SceneObject

router = APIRouter(prefix="/projects", tags=["projects"])


def _project_response(project) -> ProjectRead:
    return ProjectRead(
        id=project.id,
        name=project.name,
        description=project.description,
        created_at=project.created_at,
        georeference=GeoReferenceInput(
            crs=project.georeference.crs,
            longitude=project.georeference.longitude,
            latitude=project.georeference.latitude,
        ),
        scene_objects=[
            {
                "id": item.id,
                "name": item.name,
                "object_type": item.object_type,
                "position": item.position,
                "rotation": item.rotation,
                "scale": item.scale,
                "properties": item.properties,
            }
            for item in project.scene_objects
        ],
    )


@router.post("", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(
    payload: ProjectCreate,
    service: ProjectService = Depends(get_project_service),
):
    reference = GeoReference(**payload.georeference.model_dump())
    project = service.create_project(payload.name, payload.description, reference)
    return _project_response(project)


@router.get("", response_model=list[ProjectRead])
def list_projects(service: ProjectService = Depends(get_project_service)):
    return [_project_response(project) for project in service.list_projects()]


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(
    project_id: UUID,
    service: ProjectService = Depends(get_project_service),
):
    try:
        return _project_response(service.get_project(project_id))
    except ProjectNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post(
    "/{project_id}/scene-objects",
    response_model=ProjectRead,
    status_code=status.HTTP_201_CREATED,
)
def add_scene_object(
    project_id: UUID,
    payload: SceneObjectCreate,
    service: ProjectService = Depends(get_project_service),
):
    scene_object = SceneObject(**payload.model_dump())
    try:
        project = service.add_scene_object(project_id, scene_object)
        return _project_response(project)
    except ProjectNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.delete("/{project_id}/scene-objects/{object_id}", response_model=ProjectRead)
def delete_scene_object(
    project_id: UUID,
    object_id: UUID,
    service: ProjectService = Depends(get_project_service),
):
    try:
        project = service.remove_scene_object(project_id, object_id)
        return _project_response(project)
    except ProjectNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
