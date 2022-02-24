# SPDX-License-Identifier: AGPL-3.0-or-later

from logging import DEBUG, FileHandler, Formatter, Logger, StreamHandler, getLogger


def Log(title: str, filename: str) -> Logger:
    """Logging wrapper."""

    log: Logger = getLogger("snagd: {}".format(title))
    logfile: str = "/var/log/{}.log".format(filename)

    try:
        with open(logfile, "w+") as fd:
            fd.close()
    except Exception:
        logfile = "{}.log".format(filename)

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

        fh = FileHandler(logfile)
        fh.setFormatter(f)
        log.addHandler(fh)

    return log
