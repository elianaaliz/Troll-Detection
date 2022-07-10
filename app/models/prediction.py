from pydantic import BaseModel

from app.core.enums import Troll


class TrollPredictionResult(BaseModel):
    label: Troll
    score: float
    elapsed_time: float
