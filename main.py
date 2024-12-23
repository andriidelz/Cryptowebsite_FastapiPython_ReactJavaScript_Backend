from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router as router_crypto
from init import init_cmc_client, cmc_client
from config import settings

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_cmc_client()

@app.get("/")
def test_key():
    return {"CMC_API_KEY": settings.CMC_API_KEY}

app.include_router(router_crypto)

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
