# SPDX-License-Identifier: AGPL-3.0-or-later

from logging import DEBUG, FileHandler, Formatter, Logger, StreamHandler, getLogger


def Log(title: str, filename: str | None = None) -> Logger:
    """Logging wrapper."""

    log: Logger = getLogger("snagd: {}".format(title))

    if filename:
        try:
            with open(filename, "w+") as fd:
                fd.close()
        except Exception:
            filename = "{}.log".format(filename)

    log.propagate = False
    log.setLevel(DEBUG)
    f = Formatter(
        "%(asctime)s %(name)s: %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if not log.hasHandlers():
        sh = StreamHandler()
        sh.setFormatter(f)
        log.addHandler(sh)

        if filename:
            fh = FileHandler(filename)
            fh.setFormatter(f)
            log.addHandler(fh)

    return log


__all__: list[str] = ["Log", "Logger"]
