old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_attribute = 0xdecafbad
    return record

logging.setLogRecordFactory(record_factory)

import logging

custom_contextual_data = "XYZ"


def main() -> None:
    logging.basicConfig(
        format="[%(asctime)s] [%(custom_contextual_data)s] [%(name)s] %(levelname)s: %(message)s", level=logging.DEBUG
    )

    old_factory = logging.getLogRecordFactory()

    def record_factory(*args: object, **kwargs: object) -> logging.LogRecord:
        global custom_contextual_data
        record = old_factory(*args, **kwargs)

        # mypy: error: "LogRecord" has no attribute "custom_contextual_data"
        record.custom_contextual_data = custom_contextual_data

        # mypy: no error
        # setattr(record, "custom_contextual_data", custom_contextual_data)

        return record

    logging.setLogRecordFactory(record_factory)

    logger = logging.getLogger(__name__)
    logger.info("Hello XYZ world!")
    global custom_contextual_data
    custom_contextual_data = "ABC"
    logger.info("Hello ABC world!")


if __name__ == "__main__":
    main()
