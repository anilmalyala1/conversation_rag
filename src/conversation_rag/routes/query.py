from fastapi import APIRouter
from pydantic import BaseModel
from rag_modules import load_index, run_query


class QueryRequest(BaseModel):
    repo_name: str
    question: str


router = APIRouter()


@router.post("/query")
def query_repo(request: QueryRequest):
    db = load_index(f"index/{request.repo_name}")
    return {"answer": run_query(db, request.question)}
