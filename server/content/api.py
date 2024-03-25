import json

import requests
from comm.db import get_db_auto_close
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from utils.func import ResponseHandler

router = APIRouter(prefix="/content")


@router.get("/common2")
def test():
    response_handler = ResponseHandler()

    res = requests.get("http://127.0.0.1:8888/content/common2")
    response = json.loads(res.text)

    print(response)

    return response_handler.get_response()


@router.post("/common")
def pfd_calculation_api(request: dict):
    response_handler = ResponseHandler()
    print(">>>>> api call")

    data = json.loads(request["data"])

    print(data)

    return []
