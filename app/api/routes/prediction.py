from fastapi import APIRouter
from starlette.requests import Request

from app.models.payload import TextPayload
from app.models.prediction import TrollPredictionResult
from app.services.models import TrollDetectionModel

router = APIRouter()


@router.post("/predict", response_model=TrollPredictionResult, name="predict")
def post_predict(
    request: Request, data: TextPayload = None,
) -> TrollPredictionResult:

    model: TrollDetectionModel = request.app.state.model
    prediction: TrollPredictionResult = model.predict(data)

    return prediction
