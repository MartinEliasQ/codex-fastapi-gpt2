from fastapi import FastAPI
from starlette.requests import Request
import uvicorn


from app.core import config
from app.api.api_v1.api import api_router


app = FastAPI(title="gpt", openapi_url="/api/v1/openapi.json")

app.include_router(api_router)

uvicorn.run(app, host="0.0.0.0", port=3333)
