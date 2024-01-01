from datetime import datetime
from matador.schemas.base import BaseSchema


def test_base_schema():
    """Test that the base schema has the correct fields."""
    created_at = datetime.now()
    updated_at = datetime.now()
    schema = BaseSchema.model_validate(
        obj={
            "id": 1,
            "created_at": created_at,
            "updated_at": updated_at,
        }
    )
    assert schema.id == 1
    assert schema.created_at == created_at
    assert schema.updated_at == updated_at
