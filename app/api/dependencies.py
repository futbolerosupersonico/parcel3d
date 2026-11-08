from functools import lru_cache

from app.application.project_service import ProjectService
from app.infrastructure.repositories import InMemoryProjectRepository


@lru_cache
def get_project_service() -> ProjectService:
    # A single in-memory repository is sufficient for the first local prototype.
    return ProjectService(InMemoryProjectRepository())
