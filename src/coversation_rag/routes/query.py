from fastapi import APIRouter, Body
from rag_modules import load_index
from rag_modules import run_query

router = APIRouter()

@router.post("/query")
def query_repo(repo_name: str = Body(...), question: str = Body(...)):
    db = load_index(f"index/{repo_name}")
    return {"answer": run_query(db, question)}
