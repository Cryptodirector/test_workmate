from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers.v1.cat_router import router as cat_router
from app.routers.v1.breed_router import router as breed_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cat_router)
app.include_router(breed_router)
