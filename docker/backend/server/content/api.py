import json

from fastapi import APIRouter
from server.bbn_inference import bbn_utils, whole_model

router = APIRouter(prefix="/content")

@router.post("/common")
def bbn_inference_api(request: dict):
    print(">>>>> api call")

    data = json.loads(request["data"])
    print(data)

    # test code
    bbn_utils.print_pymc_version()

    # respond with dummy data
    result_file = open("dummy_data.json", "r")
    results = result_file.read()

    response = json.loads(results)

    return response
