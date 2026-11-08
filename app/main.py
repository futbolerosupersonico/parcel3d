from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.projects import router as projects_router

app = FastAPI(
    title="Parcel3D API",
    description="Initial API scaffold for parcel-based 3D design projects.",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(projects_router, prefix="/api/v1")
