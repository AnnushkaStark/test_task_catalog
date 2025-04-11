import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.v1.router import api_router as catalog_router

app = FastAPI(
    title="Catalog",
    openapi_url="/catalog/openapi.json",
    docs_url="/catalog/docs",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(catalog_router, prefix="/catalog")
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        proxy_headers=True,
    )
