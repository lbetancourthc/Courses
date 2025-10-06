from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from os.path import dirname, abspath, join
from pydantic import BaseModel

current_dir = dirname(abspath(__file__))
static_path = join(current_dir, "static")

# Create FastAPI application
app = FastAPI()
app.mount("/ui", StaticFiles(directory=static_path), name="ui")

class Body(BaseModel):
    strftime: str

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/generate")
def generate(body: Body):
    """Generate the curremt time given a strftime template, e.g:
    '%Y-%mn-%dT%H:%M:%s.%f'

    Args:
        body (Body): str
    """
    tmpl = body.strftime or "%Y-%mn-%dT%H:%M:%s.%f"
    return {
        "date": datetime.now().strftime(tmpl)
    }