from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.models.payload import TextPayload
from app.models.prediction import TrollDetectionModel
from app.services.models import TrollPredictionResult

router = APIRouter()


@router.post("/predict", response_model=TrollPredictionResult, name="predict")
def post_predict(
    request: Request, data: TextPayload = None,
) -> TrollPredictionResult:

    model:  TrollDetectionModel = request.app.state.model
    prediction: TrollPredictionResult = model.predict(data)

    return prediction
