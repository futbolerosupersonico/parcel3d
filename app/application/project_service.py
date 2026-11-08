from uuid import UUID

from app.domain.entities import GeoReference, ParcelProject, SceneObject
from app.domain.repositories import ProjectRepository


class ProjectNotFoundError(Exception):
    pass


class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self._repository = repository

    def create_project(
        self,
        name: str,
        description: str = "",
        georeference: GeoReference | None = None,
    ) -> ParcelProject:
        project = ParcelProject(
            name=name,
            description=description,
            georeference=georeference or GeoReference(),
        )
        self._repository.add(project)
        return project

    def list_projects(self) -> list[ParcelProject]:
        return self._repository.list()

    def get_project(self, project_id: UUID) -> ParcelProject:
        project = self._repository.get(project_id)
        if project is None:
            raise ProjectNotFoundError(str(project_id))
        return project

    def add_scene_object(self, project_id: UUID, scene_object: SceneObject) -> ParcelProject:
        project = self.get_project(project_id)
        project.add_scene_object(scene_object)
        self._repository.update(project)
        return project

    def remove_scene_object(self, project_id: UUID, object_id: UUID) -> ParcelProject:
        project = self.get_project(project_id)
        if not project.remove_scene_object(object_id):
            raise ProjectNotFoundError(f"Scene object {object_id} not found")
        self._repository.update(project)
        return project
