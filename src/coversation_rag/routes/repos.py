from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/repos")
def list_repos():
    return {"repos": [d for d in os.listdir("repos") if os.path.isdir(f"repos/{d}")]}
