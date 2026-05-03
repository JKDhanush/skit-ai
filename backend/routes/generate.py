from fastapi import APIRouter, HTTPException
from models.schemas import RequestModel, ResponseModel
from services.llm_service import generate_llm_response

router = APIRouter()

@router.post("/generate", response_model=ResponseModel)
def generate(request: RequestModel):
    try:
        response = generate_llm_response(
            request.customer_message,
            request.tone,
            request.length
        )
        return {"response": response}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"LLM generation failed: {str(e)}"
        )