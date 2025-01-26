from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.auth.api import router as auth_router
from server.content.api import router as content_router
from server.auth.sensitivity_analysis_api import router as sensitivity_analysis_router
import urllib3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'server')))



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routing
app.include_router(auth_router, prefix="/auth")
app.include_router(content_router, prefix="/content")
app.include_router(sensitivity_analysis_router, prefix="/api")
