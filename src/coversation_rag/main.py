# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import index, query, edit, repos
import uvicorn

app = FastAPI()

# Allow CORS for all origins (frontend interaction)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(index.router)
app.include_router(query.router)
app.include_router(edit.router)
app.include_router(repos.router)

# Optional root health check
@app.get("/")
def read_root():
    return {"status": "Java Code Assistant Backend Running"}

# ✅ Add this so app can be run directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
