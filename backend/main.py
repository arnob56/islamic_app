from fastapi import FastAPI
from backend.prayer import router

app = FastAPI(
    title="Islamic Companion API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health():
    return {"status": "running"}
