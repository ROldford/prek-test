from pydantic import BaseModel
from loguru import logger


class TestModel(BaseModel):
    id_number: int
    name: str
    value: float


if __name__ == "__main__":
    test_instance = TestModel(id_number=1, name="Test", value=3.14)
    logger.info(test_instance)
    logger.info(test_instance.name)
    logger.info(test_instance.model_dump_json())
