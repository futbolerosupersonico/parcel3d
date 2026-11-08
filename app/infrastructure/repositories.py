from uuid import UUID

from app.domain.entities import ParcelProject


class InMemoryProjectRepository:
    """Development adapter. Replace with a persistent adapter without changing use cases."""

    def __init__(self) -> None:
        self._projects: dict[UUID, ParcelProject] = {}

    def add(self, project: ParcelProject) -> None:
        self._projects[project.id] = project

    def get(self, project_id: UUID) -> ParcelProject | None:
        return self._projects.get(project_id)

    def list(self) -> list[ParcelProject]:
        return list(self._projects.values())

    def update(self, project: ParcelProject) -> None:
        self._projects[project.id] = project
