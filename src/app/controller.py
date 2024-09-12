from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl, FtpUrl

from . import service

app = FastAPI()

class Url(BaseModel):
    longUrl: HttpUrl | FtpUrl

@app.post("/")
def create_short_url(body: Url):
    return service.create_short_hash(str(body.longUrl))

@app.get("/{short_hash}")
def get_long_url(short_hash: str):
    long_url = service.get_long_url(short_hash)
    return RedirectResponse(url=long_url, status_code=302)
