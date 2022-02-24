# SPDX-License-Identifier: AGPL-3.0-or-later

from importlib.metadata import version as pkg_version
from sys import exit

import click


@click.command(name="snagctl")
@click.option(
    "--version",
    default=False,
    help="Show snagctl version",
    is_flag=True,
    type=bool,
)
def main(version: bool) -> None:
    if version:
        print("snagctl v{}".format(pkg_version("snagem")))

    exit(0)


if __name__ == "__main__":
    main()
