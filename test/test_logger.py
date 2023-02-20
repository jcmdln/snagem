from snagem.logger import Logger, logger


def test_logger() -> None:
    log: Logger = logger()
    assert log
    assert isinstance(log, Logger)
