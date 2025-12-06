from pydantic import BaseModel
from typing import List

class ReviewInput(BaseModel):
    reviews: List[str]

class InsightOutput(BaseModel):
    overall_sentiment: str
    key_themes: List[str]
    actionable_feedback: str
