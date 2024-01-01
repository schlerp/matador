import fastapi
import fastapi.routing
from matador.models.dataset import Dataset as DatasetModel
from matador.persist.database import get_db
from matador.schemas import dataset
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

router = fastapi.routing.APIRouter()


@router.get("/dataset/[dataset_id]", response_model=dataset.DatasetOut, status_code=200)
async def get_dataset(
    dataset_id: int,
    db: Session = fastapi.Depends(get_db),
) -> None | dataset.DatasetOut:
    try:
        result = db.query(DatasetModel).filter(DatasetModel.id == dataset_id)
        return dataset.DatasetOut.model_validate(result)
    except NoResultFound:
        return None
