from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from snagem.route.v1.router import router as v1_router

app = FastAPI(docs_url="/", redoc_url=None, title="Snagem")
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"],
)
app.include_router(v1_router, prefix="/v1", tags=["v1"])

__all__: list[str] = ["app"]
