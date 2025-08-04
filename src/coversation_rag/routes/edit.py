#from coversation_rag.app import filepath, instruction
from fastapi import APIRouter, Body
from rag_modules import edit_code
from pydantic import BaseModel

router = APIRouter()

class IndexRequest(BaseModel):
    filepath: str
    instruction: str

@router.post("/edit")
def edit_file(request: IndexRequest):
    filepath=request.filepath
    instruction=request.instruction
    print(filepath,"----",instruction)

    return {"result": edit_code(filepath, instruction)}
