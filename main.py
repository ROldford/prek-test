from loguru import logger

from src.do_thing import do_thing
from src.models import TestModel
from src.polars_test import main as polars_main


def main():
    logger.info("Now running main() in main.py")

    result = do_thing(1.5, 2.5, "The result is:")
    logger.info(result)

    test_instance = TestModel(id_number=1, name="Test", value=3.14)
    logger.info(test_instance)
    logger.info(test_instance.name)
    logger.info(test_instance.model_dump_json())

    polars_main()


if __name__ == "__main__":
    main()
