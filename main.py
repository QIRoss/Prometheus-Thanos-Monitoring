from fastapi import FastAPI, Request
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

GET_REQUESTS = Counter('api_get_requests_total', 'Total number of GET requests to the API')

@app.get("/metrics")
async def metrics():
    return PlainTextResponse(generate_latest(), media_type="text/plain")

@app.get("/")
async def read_item():
    GET_REQUESTS.inc()
    return {"message": "This is a GET request!"}
