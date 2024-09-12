from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, FtpUrl

import app.service as service

app = FastAPI()

class Url(BaseModel):
    longUrl: HttpUrl | FtpUrl

@app.post("/")
def create_short_url(body: Url):
    return service.create_short_hash(body.longUrl)

@app.get("/{short_hash}")
def get_long_url(short_hash: str):
    print(short_hash)
    return service.get_long_url(short_hash)

@app.get("/")
def redirect_to_docs():
    print('redirect_to_docs')
    return {"message": "Redirecting to /docs"}

# RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)
