from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.models import ReviewInput, InsightOutput
from app.ai_engine import analyze_reviews

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/analyze", response_model=InsightOutput)
async def analyze(data: ReviewInput):
    result = analyze_reviews(data.reviews)
    return InsightOutput(**result)


@app.get("/")
def home():
    return FileResponse("static/index.html")
