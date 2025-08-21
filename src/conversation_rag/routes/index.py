from fastapi import APIRouter, Body
from rag_modules import load_java_repo
from rag_modules import create_index
from pydantic import BaseModel


class IndexRequest(BaseModel):
    repo_name: str

router = APIRouter()

@router.post("/index")

def index_repo(request: IndexRequest):
    repo_name = request.repo_name
    print("Loading Repo name--->", repo_name)
    docs = load_java_repo(f"{repo_name}")
    create_index(docs, persist_dir=f"index/{repo_name}")
    return {"status": "indexed"}
