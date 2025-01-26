# server/sensitivity_analysis_api.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from server.bbn_inference.examples.example_for_sensitivity_analysis import run_example_for_sensitivity_analysis
from server.utils.func import ResponseHandler

# APIRouter 객체 생성
router = APIRouter()

# 요청 본문 데이터 모델 정의
class SensitivityRequest(BaseModel):
    pfd_goal: str
    confidence_goal: str

# Sensitivity Analysis 엔드포인트 정의
@router.post("/sensitivity-analysis")
def sensitivity_analysis(request: SensitivityRequest):
    response_handler = ResponseHandler()
    try:
        # run_example_for_sensitivity_analysis 함수 호출
        result = run_example_for_sensitivity_analysis(request.pfd_goal, request.confidence_goal)
        response_handler.add_data({"num_tests": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return response_handler.get_response()
